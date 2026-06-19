import streamlit as st
import pandas as pd
from huggingface_hub import hf_hub_download
st.write("""
# My first app
Hello *world!*
""")
st.title('My first app') 
name=st.text_input("Enter your name", "Type Here ...")
if name:
    st.write('Hello, ', name, '!')
    
client=inferenceClient(
    provider="auto",api_key=os.environ.get["HUGGINGFACEHUB_API_TOKEN"]
)