"""3.5. Acceessing different LLMs via Langchain**
!pip install -q -U langchain-community
**OpenAI**
!pip install -q -U langchain-openai
import os
from langchain_openai import ChatOpenAI



print(response.content)
# response
**Gemini**
!pip install -q -U langchain-google-genai
import os
from langchain_google_genai import ChatGoogleGenerativeAI

os.environ["GOOGLE_API_KEY"] = "your_api_key"

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
)

response = llm.invoke("What is Machine Learning")

print(response.content)
**Groq**
!pip install -q -U langchain-groq
import os
from langchain_groq import ChatGroq



llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
)

response = llm.invoke("What is Machine Learning")

print(response.content)
**Ollama**
!pip install -q -U langchain-ollama
!ollama list
import os
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="gemma2:2b",
    temperature=0,
)

response = llm.invoke("What is Machine Learning")

print(response.content)
"""