import streamlit as st

from query import search, generate_answer


st.set_page_config(
    page_title="Python RAG Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Python RAG Chatbot")
if st.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()
st.write("Ask questions about your Python document.")


# Store conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


# Ask a new question
question = st.chat_input("Ask a question...")


if question:

    # Show user question
    with st.chat_message("user"):
        st.write(question)

    st.session_state.messages.append({
        "role": "user",
        "content": question
    })


    # Generate answer
    with st.chat_message("assistant"):

        with st.spinner("Searching the document..."):

            results = search(question)

            if not results:
                answer = (
                    "I don't have enough information "
                    "in the provided document."
                )
            else:
                answer = generate_answer(question, results)

            st.write(answer)


    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })


    # Show sources
    if results:

        st.subheader("📚 Sources")

        for i, (document, score) in enumerate(results, start=1):

            source = document.metadata.get(
                "source",
                "unknown"
            )

            st.write(
                f"{i}. {source} — score: {score:.4f}"
            )