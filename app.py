import streamlit as st
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from groq import Groq
import os

client = Groq(api_key="")#Enter your API key
VECTOR_DIR = "RAG Project\\vectorstore\\ipc_bns_law"
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = FAISS.load_local(VECTOR_DIR, embedding_model, allow_dangerous_deserialization=True)


st.set_page_config(page_title="Indian Law QA", layout="wide")
st.title("Indian Law RAG Assistant (Based on IPC and BNS)")

query = st.text_input("Enter your legal question:", placeholder="e.g., What is the punishment for murder?")

if st.button("Get Answer") and query:
    with st.spinner("Searching law and generating answer..."):

        retrieved_docs = vectorstore.similarity_search(query, k=5)
        context = "\n\n".join(doc.page_content for doc in retrieved_docs)

        system_prompt = (
                    "You are a legal assistant answering questions based on Indian criminal law. "
                    "If possible, include relevant IPC and BNS section numbers. Be precise and cite sources clearly."
                    "Structure the response professionally with clear headings and bullet points where needed."
                    "Attach a note at the end that the response is based on the manually created database last updated on 15th Jul 2025, kindly refer to newer sources for any updates."
                    "Explain any legal terms in a footnote."
                )
        user_prompt = f"Question: {query}\n\nContext:\n{context}\n\nAnswer:"

        response = client.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.2,
            max_completion_tokens=1024,
        )

        answer = response.choices[0].message.content
        st.success("Answer:")
        st.markdown(answer)