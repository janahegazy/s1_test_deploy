import streamlit as st
import pandas as pd
import os
from huggingface_hub import inferenceClient


st.write("""
# My first app
Hello *world!*
""")
st.title('My first app') 
name=st.text_input("Enter your name", "Type Here ...")
if name:
    st.write('Hello, ', name, '!')
    
input_text=st.text_input("Enter your text", "Type Here ...")
client=inferenceClient(
    provider="auto",api_key=os.environ.get("HUGGINGFACEHUB_API_TOKEN")
)

if input_text:
    output=client.text_classification(
        model="distilbert-base-uncased-finetuned-sst-2-english",
        inputs=input_text
        
    )   
    st.write(output)