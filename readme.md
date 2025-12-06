# 📜 Itihaas

[![Open Source](https://img.shields.io/badge/Open%20Source-Yes-green.svg)](https://opensource.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)

> **Simple and powerful.** Democratizing access to history and cultural heritage through Agentic RAG technology

## 🌟 About

**Itihaas** (History) is an open-source educational tool that makes local history and cultural knowledge accessible to everyone. Built with Agentic RAG (Retrieval-Augmented Generation), it serves as an interactive museum guide and research assistant for exploring historical heritage.

### The Problem

Local history (like that of Barrackpore) and deep cultural insights (like Tagore's lesser-known works) are often buried in dense books or scattered across Wikipedia pages. Students, researchers, and tourists struggle to find specific, contextual answers quickly. Traditional search engines return generic results, and academic resources are often behind paywalls or written in inaccessible language.

### The Solution

**Itihaas** solves this by:
- 📚 **Centralizing Knowledge**: Aggregates information from multiple sources into a searchable knowledge base
- 🤖 **Intelligent Retrieval**: Uses vector embeddings to find the most relevant context for any question
- 💬 **Natural Conversations**: Provides detailed, contextual answers in a conversational format
- 🎯 **Agentic Architecture**: The AI actively decides when to retrieve information, ensuring accurate and comprehensive responses
- 🆓 **Open Source**: Free and accessible to everyone, with no API costs when using local models

## ✨ Features

- **Agentic RAG**: The AI autonomously retrieves relevant information before answering
- **Local Processing**: Runs entirely on your machine using Ollama (no cloud API costs)
- **Rich Context**: Provides detailed, multi-paragraph answers with source citations
- **Conversational Memory**: Maintains context across the conversation
- **Easy Setup**: Simple installation and data ingestion process

## 🚀 Quick Start

### Prerequisites

- Python 3.11 or higher
- [Ollama](https://ollama.com/) installed and running
- Required Ollama models (will be downloaded automatically on first use):
  - Embedding model: `mxbai-embed-large` (or `nomic-embed-text`)
  - Chat model: `qwen2.5:7b` (or `llama3.2:3b`)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd itihaas
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and configure your settings (defaults work for most setups).

5. **Prepare your data**
   - Create a `data/` folder
   - Add `.txt` or `.pdf` files containing information about:
     - Barrackpore's history
     - Rabindranath Tagore's works
     - Bengal's cultural heritage
     - Any other relevant historical content
   
   **Example**: Copy Wikipedia articles or historical documents into text files.

6. **Build the vector database**
   ```bash
   python ingest.py
   ```
   This will process all files in `data/` and create the searchable knowledge base.

7. **Run the application**
   ```bash
   streamlit run app.py
   ```

8. **Open your browser**
   Navigate to `http://localhost:8501` and start asking questions!

## 📁 Project Structure

```
itihaas/
├── data/                  # Place your source PDFs/TXT files here
├── vector_db/             # ChromaDB database (auto-generated, don't commit)
├── app.py                 # Main Streamlit application
├── ingest.py              # Script to build the vector database
├── requirements.txt       # Python dependencies
├── README.md              # This file
├── LICENSE                # MIT License
├── .env.example           # Environment variables template
└── .env                   # Your actual environment variables (not in git)
```

## 🔧 Configuration

Create a `.env` file with the following variables:

```env
# Ollama Configuration
EMBEDDING_MODEL=mxbai-embed-large
CHAT_MODEL=qwen2.5:7b
MODEL_PROVIDER=ollama

# Database Configuration
DATABASE_LOCATION=vector_db
COLLECTION_NAME=itihaas
```

### Model Recommendations

**For Embeddings:**
- `mxbai-embed-large` (recommended) - Best quality, ~335MB
- `nomic-embed-text` - Good alternative, smaller size

**For Chat:**
- `qwen2.5:7b` (recommended) - Excellent reasoning, ~4.4GB
- `llama3.2:3b` - Faster, smaller, ~2GB
- `mistral:7b` - Good balance

## 📖 Usage Examples

Once the app is running, try asking:

- "Tell me about the historical significance of Barrackpore"
- "What are some lesser-known works by Rabindranath Tagore?"
- "Explain the cultural importance of the Hooghly River"
- "What architectural styles are found in colonial Bengal?"

The AI will retrieve relevant information and provide detailed, contextual answers with source citations.

## 🎓 Educational Impact

This project serves multiple educational purposes:

1. **For Students**: Quick access to historical facts and cultural context
2. **For Researchers**: Efficient information retrieval from multiple sources
3. **For Tourists**: Interactive guide to local heritage sites
4. **For Educators**: Teaching tool for Bengal's history and culture

## 🛠️ Technology Stack

- **LangChain**: Framework for building LLM applications
- **ChromaDB**: Vector database for storing embeddings
- **Ollama**: Local LLM inference engine
- **Streamlit**: Web interface framework
- **Python**: Programming language

## 🤝 Contributing

Contributions are welcome! This is an open-source project aimed at preserving and democratizing access to cultural knowledge.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [LangChain](https://www.langchain.com/) and [ChromaDB](https://www.trychroma.com/)
- Powered by [Ollama](https://ollama.com/) for local AI processing
- UI built with [Streamlit](https://streamlit.io/)

## 📧 Contact

For questions, suggestions, or contributions, please open an issue on GitHub.

---

**Made with ❤️ for preserving and democratizing access to history**
