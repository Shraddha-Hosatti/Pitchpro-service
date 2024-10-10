import openai
import os
import nltk
from langchain import hub
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableWithMessageHistory
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers.json import SimpleJsonOutputParser
from langchain_core.output_parsers.string import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader, UnstructuredWordDocumentLoader, UnstructuredExcelLoader
from langchain_openai import ChatOpenAI
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_community.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferWindowMemory
from langchain.agents import AgentType, initialize_agent
from langchain.tools.retriever import create_retriever_tool
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain


try:
  nltk.download('punkt_tab')
  nltk.download('averaged_perceptron_tagger_eng')
except Exception as e:
  print(f'Error occured {e}')

llm = ChatOpenAI(api_key = openai.api_key, model="gpt-4o-mini")
openaiembedding = OpenAIEmbeddings(api_key = openai.api_key, model="text-embedding-3-large")

folder = "/content/drive/MyDrive/Data"


# Read the .docx files

def load_data(folder_path):
    txt_loader = DirectoryLoader(folder_path, glob="*.docx", loader_cls=UnstructuredWordDocumentLoader)
    xlsx_loader = DirectoryLoader(folder_path, glob="*.xlsx", loader_cls=UnstructuredExcelLoader)

    # DOCX Loader
    textdoc = txt_loader.load()
    # XLSX Loader
    xlsdoc = xlsx_loader.load()
    return {'txt_docs': textdoc, 'excel_docs': xlsdoc}

docs = load_data(folder)
txt_documents = docs['txt_docs']
xlsx_documents = docs['excel_docs']


# Parse xlsx docs and get curriculum details
def parse_curriculum(doc):
    str_prompt = PromptTemplate.from_template(
        """Return a text object that provides only the module information about a program in the following format:
        week - course - module - < description of the learning module >
        generate the description of the learning module
        No irrelevant information should be provided in the output. Make sure the information is complete.
        This is the curriculum : {curriculum}
        """
    )

    # json_prompt = PromptTemplate.from_template(
    #     """Return a text object with an `curriculum` key that provides the module information \
    #     about a program in the format where week is the key and the values are course and module as shown below:
    #     {{"week":"course": value of course,
    #             "module": value of module }}

    #     This is the curriculum : {curriculum}
    #     """
    # )
    str_parser = StrOutputParser()
    json_parser = SimpleJsonOutputParser()
    curriculum_chain = str_prompt | llm | str_parser
    # curriculum_chain = json_prompt | llm | json_parser
    curriculum = curriculum_chain.invoke({"curriculum": doc})
    return curriculum

curriculum = parse_curriculum(xlsx_documents)

txt_documents.append(
    Document(
        page_content = curriculum,
        metadata={"source": "curriculum"}
        )
    )



def load_to_chroma(collection, directory_path, embedding):
    if not os.path.exists(persist_directory):
        os.mkdir(persist_directory)

    vector_store = Chroma(
        collection_name = collection,
        embedding_function = embedding,
        persist_directory = directory_path,  # Where to save data locally, remove if not necessary
    )
    return vector_store

# Chroma parameters
program_name = "epgpds"
collection_name = program_name
persist_directory = "./chroma_langchain_db"

VS = load_to_chroma(collection_name, persist_directory, openaiembedding)



