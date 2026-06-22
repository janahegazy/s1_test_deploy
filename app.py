import streamlit as st
from dotenv import load_dotenv
import os
from huggingface_hub import InferenceClient

load_dotenv()

st.title('My first app') 
name=st.text_input("Enter your name", "Type Here ...")
if name:
    st.write('Hello, ', name, '!')
    
input_text=st.text_input("Enter your text", "Type Here ...")
client = InferenceClient(
    provider="hf-inference",
    api_key=os.environ.get("HF_TOKEN")
)

if input_text:
   output = client.text_classification(
    model="cardiffnlp/twitter-roberta-base-sentiment-latest",
    text=input_text
)
st.write(output)
print(os.environ.get("HF_TOKEN"))

if input_text and input_text != "Type Here ...":
    output = client.text_classification(
        model="cardiffnlp/twitter-roberta-base-sentiment-latest",
        text=input_text
    )
    st.write(output)

