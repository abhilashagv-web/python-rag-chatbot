# Python RAG Chatbot

## Live Demo
[Open Python RAG Chatbot](https://python-rag-chatbot-k3zfucywfbwystvawpg986.streamlit.app/)

A Retrieval-Augmented Generation (RAG) chatbot that answers questions using a Python programming document.

## Features

- Document-based question answering
- HuggingFace embeddings
- FAISS vector search
- Groq LLM for answer generation
- Source document references
- Streamlit web interface

## Technologies

- Python
- LangChain
- HuggingFace
- FAISS
- Groq
- Streamlit

## How it works

1. The Python guide is loaded as a document.
2. The document is split into smaller chunks.
3. HuggingFace embeddings convert the chunks into vectors.
4. FAISS stores the vectors for similarity search.
5. When a user asks a question, relevant document chunks are retrieved.
6. Groq generates an answer using the retrieved information.
7. The chatbot displays the answer and source document reference.

## Project Structure

```text
python-rag-chatbot/
│
├── data/
│   └── python_guide.txt
│
├── evals/
│
├── src/
│   ├── app.py
│   └── query.py
│
├── vectorstore/
│
├── .gitignore
├── README.md
└── requirements.txt