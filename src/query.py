import os
from pathlib import Path

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq


VECTORSTORE_DIR = Path("vectorstore")


def load_vectorstore():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.load_local(
        str(VECTORSTORE_DIR),
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vectorstore


def search(query, k=3):
    vectorstore = load_vectorstore()

    return vectorstore.similarity_search_with_score(
        query,
        k=k
    )


def generate_answer(question, results):
    if not results:
        return "I could not find relevant information in the document."

    context_parts = []

    for document, score in results:
        source = document.metadata.get("source", "unknown")

        context_parts.append(
            f"Source: {source}\n"
            f"{document.page_content}"
        )

    context = "\n\n---\n\n".join(context_parts)

    llm = ChatGroq(
        model="openai/gpt-oss-20b",
        temperature=0
    )

    prompt = f"""
You are a helpful question-answering assistant.

Answer the user's question using ONLY the provided context.

If the answer is not present in the context, say:
"I don't have enough information in the provided document."

Always include the source filename at the end of your answer.

Context:
{context}

Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)

    return response.content


if __name__ == "__main__":
    print("====================================")
    print("       Python RAG Chatbot")
    print("====================================")
    print("Type 'exit' to quit.\n")

    while True:
        question = input("Ask a question: ")

        if question.lower() == "exit":
            print("Goodbye!")
            break

        if not question.strip():
            print("Please enter a question.\n")
            continue

        print("\n[1] Retrieving relevant documents...")

        results = search(question)

        if not results:
            print("No relevant information found.\n")
            continue

        print(f"[2] Retrieved {len(results)} chunks.")

        print("\n[3] Generating answer with Groq...")

        answer = generate_answer(question, results)

        print("\n========== ANSWER ==========")
        print(answer)

        print("\n========== SOURCES ==========")

        for i, (document, score) in enumerate(results, start=1):
            source = document.metadata.get("source", "unknown")
            print(f"{i}. {source} (score: {score:.4f})")

        print("\n")