import os
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

gemini_key = os.environ.get('GOOGLE_API_KEY')
OPEN_API_KEY = os.environ.get('OPENAI_API_KEY')


models = {
    "open_ai":{
        "llm":ChatOpenAI(openai_api_key=OPEN_API_KEY,temperature=0,model="gpt-4o-mini"),
        "embedding":OpenAIEmbeddings(api_key=OPEN_API_KEY,model="text-embedding-3-large", dimensions=512)
        },
    
    "gemini":{
        "llm":ChatGoogleGenerativeAI(model="gemini-1.5-pro",temperature=0,api_key=gemini_key),
        "embedding": GoogleGenerativeAIEmbeddings(model="models/text-embedding-004",api_key=gemini_key)
    }
}

def get_llm_embedings(type:str):
    return models.get(type,None)