import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA

#Esta linea configura el API KEY
load_dotenv()

#Primer paso: Carga de documentos
loader = TextLoader("data/documentos.txt", encoding="utf-8")
documentos = loader.load()

#Segundo paso: Dividir documentos en fragmentos (chunks)
divisor_texto = CharacterTextSplitter(
    chunk_size = 200,
    chunk_overlap=20
)
docs = divisor_texto.split_documents(documentos)

#Tercer paso: Crear embeddings
embeddings = OpenAIEmbeddings()

#Cuarto paso: Crear base de datos vectorial (FAISS)
base_vectorial = FAISS.from_documents(docs, embeddings)

#Quinto paso: Crear recuperador
recuperador = base_vectorial.as_retriever()

#Sexto paso: Crear modelo de lenguaje
modelo = ChatOpenAI(
    temperature = 0,
    model_name = "gpt-3.5-turbo"
)

#Septimo paso: Crear pipeline RAG
cadena_rag = RetrievalQA.from_chain_type(
    llm=modelo,
    retriever=recuperador,
    return_source_documents=True
)

#Octavo paso: Interaccion con usuarios
print("Asistente Inteligente RetailSmart S. (RAG)")
print("Escribe 'Salir' para terminar \n")

while True:
    pregunta = input("Ingresa tu pregunta: ")

    if pregunta.lower() == "salir":
        break
    
    resultado = cadena_rag(pregunta)

    print("\nRespuesta: ")
    print(resultado["result"])

    print("\nDocumentos utilizados: ")
    for doc in resultado["source_documents"]:
        print("-", doc.page_content[:100])

    print("\n" + "-"*50 + "\n")