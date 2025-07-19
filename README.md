Indian Legal Question-Answering with RAG

Why This Project Matters - 

Until recently, the Indian Penal Code (IPC) served as the foundation of India’s criminal justice system, with 511 sections spanning 23 chapters. However, on July 1, 2024, the Bharatiya Nyaya Sanhita (BNS) officially replaced the IPC. The BNS introduces a modernized criminal code that addresses contemporary issues such as organized crime, cyber threats, and economic offenses, while placing greater emphasis on digital identity and authenticity.

With this significant legal transition, I identified a critical gap: How can individuals, legal professionals, and institutions smoothly adapt to BNS when legal precedents and common understanding are still deeply rooted in the IPC? Moreover, the sudden shift poses a risk of confusion and misinterpretation, especially since many legal terms remain complex—and LLMs can hallucinate if not grounded in reliable legal texts.

This project aims to bridge that gap.

It provides a legal query answering system that references both IPC and BNS sections, helping users understand how older cases and precedents relate to the new code. By using a retrieval-augmented generation (RAG) approach powered by Groq LLMs, and grounded in a manually curated database of IPC, BNS, and their mappings, the system minimizes hallucinations and ensures that responses are accurate, traceable, and legally meaningful.Additionally, the app explains complex legal terms in simple language, making legal knowledge accessible to the public, while remaining a valuable resource for legal professionals navigating the IPC–BNS transition.

Use Cases - 

Given its easy-to-use interface, this tool can benefit a broad range of users:

    1. Academia: Law students can use the tool to understand the mapping and evolution between IPC and BNS sections.
    2. Legal Aid: Legal practitioners can use it as a reference tool to explain legal options and cite the appropriate sections from both codes.
    3. General Public: Anyone curious about the law can use the app to understand legal sections, with complex terms explained in footnotes.

The Project -

The project was divided into several subparts:

    1. Data Collection - 
        a. IPC and BNS sections were scraped from official online sources.
        b. A comparison document (“COMPARISON SUMMARY BNS to IPC”) was also scraped.
        c. A final corpus (ipc_bns_dual_tagged.jsonl) was constructed containing IPC-BNS section pairs and their descriptions.
    2. Database Creation - The corpus was chunked and embedded using Hugging Face models, and stored in a FAISS vector database.
    3. Application Development - The app can be run via app.py, which uses a Streamlit interface to accept user queries and return legal answers based on vector retrieval.
    
    ** model.ipynb includes all backend code: data collection, vector store creation, and offline prompting.
    ** app.py is the frontend app. To run locally, update file paths and insert your Groq API key.

Future Work - 
    
    1. Expanding the database to include key judicial decisions and case law precedents.
    2. Improving the frontend interface for a better user experience.

Tech Stack - 

    Model & Inference: Groq API (meta-llama/llama-4-scout-17b-16e-instruct)
    RAG Framework: LangChain
    Vector Store: FAISS
    Embeddings: Hugging Face (all-MiniLM-L6-v2)
    Frontend: Streamlit
    Storage: Local filesystem

If you have any suggestions, please feel free to reach out!
