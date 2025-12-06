# app.py

import os
from dotenv import load_dotenv

import streamlit as st

from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain.chat_models import init_chat_model
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.tools import tool

# Load environment variables
load_dotenv()

########################### INITIALIZE EMBEDDINGS MODEL ###########################

embeddings = OllamaEmbeddings(
  model=os.getenv("EMBEDDING_MODEL"),
)

########################### INITIALIZE CHROMA VECTOR STORE ###########################

vector_store = Chroma(
  collection_name=os.getenv("COLLECTION_NAME"),
  embedding_function=embeddings,
  persist_directory=os.getenv("DATABASE_LOCATION"),
)

########################### INITIALIZE CHAT MODEL ###########################

llm = init_chat_model(
  os.getenv("CHAT_MODEL"),
  model_provider=os.getenv("MODEL_PROVIDER"),
  temperature=0  # Keeping temp 0 ensures factual accuracy
)

########################### DEFINE RETRIEVER TOOL ###########################

@tool
def retrieve(query: str):
  """Retrieve relevant information for a query from the vector store."""
  # CHANGED: Increased k to 5.
  # To write a long answer, the AI needs more raw material.
  retrieved_docs = vector_store.similarity_search(query, k=5)

  results = []
  for doc in retrieved_docs:
    source = doc.metadata.get("source", "Unknown")
    content = doc.page_content.replace("\n", " ")
    results.append(f"Content: {content} (Source: {source})")
  return "\n\n".join(results)


########################### DEFINE PROMPT ###########################

# CHANGED: Significantly upgraded the System Prompt to force detail.
prompt = ChatPromptTemplate.from_messages(
  [
    (
      "system",
      "You are an expert researcher and historian. Your goal is to provide **elaborate and descriptive** answers. "
      "Use the 'retrieve' tool to fetch information. \n\n"

      "**Guidelines for Answering:**\n"
      "1. **Be Verbose:** Do not answer in a single sentence. Write a full paragraph (at least 3-4 sentences).\n"
      "2. **Add Context:** When describing locations or people, include details about geography, history, or significance found in the context.\n"
      "3. **Flow:** Ensure the answer reads smoothly like a textbook entry.\n\n"

      "**Formatting Instructions:**\n"
      "- Do not mention the source URL inside the main paragraph.\n"
      "- At the very end, add a section titled '**Sources**'.\n"
      "- List unique Source URLs as bullet points."
    ),
    # Placeholder for Chat History (Memory)
    MessagesPlaceholder(variable_name="chat_history"),

    ("human", "{input}"),

    # Placeholder for Agent Scratchpad (Tool Calls & Outputs)
    MessagesPlaceholder(variable_name="agent_scratchpad"),
  ]
)

########################### CREATE AGENT ###########################

tools = [retrieve]
agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

########################### STREAMLIT APP ###########################

st.set_page_config(page_title="Agentic RAG Chatbot", page_icon="🦜")
st.title("🦜 Agentic RAG Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
  st.session_state.messages = []

# Display previous chat messages
for message in st.session_state.messages:
  if isinstance(message, HumanMessage):
    with st.chat_message("user"):
      st.markdown(message.content)
  elif isinstance(message, AIMessage):
    with st.chat_message("assistant"):
      st.markdown(message.content)

# Input box for user question
user_question = st.chat_input("Ask me anything about Rabindranath or Barrackpore...")

if user_question:
  # Add user message to chat UI
  with st.chat_message("user"):
    st.markdown(user_question)
  # Add to internal history
  st.session_state.messages.append(HumanMessage(user_question))

  # Add a spinner so the user knows the AI is thinking (good for UX when generating long answers)
  with st.spinner("Thinking..."):
    # Call the agent executor with history
    result = agent_executor.invoke({
      "input": user_question,
      "chat_history": st.session_state.messages
    })

    # Get the AI response
    ai_message = result.get("output") or result.get("output_text", "I don't know")

  # Display AI response
  with st.chat_message("assistant"):
    st.markdown(ai_message)
  # Add to internal history
  st.session_state.messages.append(AIMessage(ai_message))
