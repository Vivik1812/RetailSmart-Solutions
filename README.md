# Proyecto RetailSmart - Sistema RAG

## Descripción
Este proyecto implementa una solución basada en **Retrieval-Augmented Generation (RAG)** para mejorar el acceso a la información interna en una empresa del sector retail.

El sistema permite a los empleados realizar consultas en lenguaje natural y obtener respuestas basadas en documentos internos de la organización.

---

## Tecnologías utilizadas

- Python
- LangChain
- OpenAI (Modelo de lenguaje - LLM)
- FAISS (Base de datos vectorial)

---

## ¿Cómo funciona el sistema?

El sistema sigue el siguiente flujo:

1. El usuario realiza una pregunta
2. La pregunta se transforma en un vector (embedding)
3. Se realiza una búsqueda en la base vectorial
4. Se recuperan documentos relevantes
5. Se construye un contexto
6. El modelo de lenguaje genera una respuesta basada en ese contexto

---


---

## Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/tuusuario/retailsmart-rag.git
cd retailsmart-rag
Crear entorno virtual (opcional):
python -m venv venv
venv\Scripts\activate
Instalar dependencias:
pip install -r requirements.txt
🔐 Configuración

Debes agregar tu API Key de OpenAI en el archivo app.py:

os.environ["OPENAI_API_KEY"] = "TU_API_KEY_AQUI"
Ejecución del proyecto
python app.py