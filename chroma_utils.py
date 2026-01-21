import os
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Define the persistent directory for ChromaDB
PERSIST_DIRECTORY = "./chroma_persistent_storage"

def get_vectorstore():
    """
    Returns a persistent Chroma vector store instance.
    Ensure OpenAI API key is set in .env
    """
    embedding_function = OpenAIEmbeddings()
    
    vectorstore = Chroma(
        collection_name="langgraph_chatbot_memory",
        embedding_function=embedding_function,
        persist_directory=PERSIST_DIRECTORY
    )
    return vectorstore

def add_documents_to_chroma(texts, metadatas=None):
    """
    Adds texts to the Chroma vector store.
    :param texts: List of strings to add.
    :param metadatas: Optional list of metadata dicts.
    """
    vectorstore = get_vectorstore()
    vectorstore.add_texts(texts=texts, metadatas=metadatas)
    print(f"Added {len(texts)} documents to ChromaDB.")

def query_chroma(query, k=3):
    """
    Queries the Chroma vector store.
    :param query: Query string.
    :param k: Number of results to return.
    :return: List of matching documents.
    """
    vectorstore = get_vectorstore()
    results = vectorstore.similarity_search(query, k=k)
    return results

if __name__ == "__main__":
    # Test the implementation
    print("Initializing ChromaDB...")
    try:
        vs = get_vectorstore()
        print(f"ChromaDB initialized at {PERSIST_DIRECTORY}")
        
        # Uncomment to test adding data
        # add_documents_to_chroma(["This is a test document about LangGraph.", "ChromaDB is great for vector storage."])
        
        # Uncomment to test querying
        # docs = query_chroma("What is ChromaDB?")
        # for doc in docs:
        #     print(f"Found: {doc.page_content}")
            
    except Exception as e:
        print(f"Error initializing ChromaDB: {e}")
