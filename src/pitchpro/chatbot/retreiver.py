from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

from pitchpro.chatbot.secret_manager import get_secret

def get_retriever_object(collection_name):

    openai_embedding = OpenAIEmbeddings(api_key=get_secret('OPENAI_API_KEY'), model="text-embedding-ada-002")

    vector_store = Chroma(
        collection_name=collection_name,
        embedding_function=openai_embedding,
        persist_directory="/app/vector_store/",  # Where to save data locally, remove if not necessary
    )

    return vector_store.as_retriever()
