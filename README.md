# Python RAG Chatbot

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
2. The document is split into chunks.
3. HuggingFace embeddings convert the chunks into vectors.
4. FAISS stores the vectors.
5. A user's question is converted into a vector.
6. Relevant document chunks are retrieved.
7. Groq generates an answer using the retrieved context.

## Example

**Question:**

What is a Python function?

**Answer:**

A function is a reusable block of code defined with the `def` keyword. Functions can accept parameters and can return a result using `return`.

## Run locally

Install the dependencies:

```bash
pip install -r requirements.txt
