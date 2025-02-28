#initialize all important keys to connect to environment
import os
from dotenv import load_dotenv
#initialize doteve
load_dotenv()

#langsmith tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANCHAIN_TRACING"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")

#import Ollama Model 
from langchain_community.llms import Ollama

#import steamlit for deployment
import streamlit as st

# chat prompt template 
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


#design prompt template 
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant.Please respond to the question asked"),
        ("user","Question:{question}")
    ]
)

#design streamlit frame work

#app name
st.title("Langchain Demo with LLAMA 3.1")
input_text=st.text_input("What Question you have in mind today?")


# call the llama model 
llm=Ollama(model="llama3.1")
# initialize the output parse
output_parser=StrOutputParser()
#make the chain
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))

