from pathlib import Path

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


DATA_DIR = Path("data")
VECTORSTORE_DIR = Path("vectorstore")


def load_documents():
    documents = []

    for file_path in DATA_DIR.glob("*.txt"):
        text = file_path.read_text(encoding="utf-8")

        documents.append({
            "source": file_path.name,
            "text": text
        })

    return documents


def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = []

    for document in documents:
        text_chunks = splitter.split_text(document["text"])

        for chunk in text_chunks:
            chunks.append({
                "source": document["source"],
                "text": chunk
            })

    return chunks


def create_vectorstore(chunks):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    texts = [chunk["text"] for chunk in chunks]
    metadatas = [{"source": chunk["source"]} for chunk in chunks]

    vectorstore = FAISS.from_texts(
        texts=texts,
        embedding=embeddings,
        metadatas=metadatas
    )

    vectorstore.save_local(str(VECTORSTORE_DIR))

    return vectorstore


if __name__ == "__main__":
    documents = load_documents()
    chunks = split_documents(documents)

    print(f"Loaded {len(documents)} document(s).")
    print(f"Created {len(chunks)} chunks.")

    vectorstore = create_vectorstore(chunks)

    print("Vector store created successfully!")
    print(f"Saved to: {VECTORSTORE_DIR}")