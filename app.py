import streamlit as st
import pandas as pd
 
st.write("""
# My first app
Hello *world!*
""")
st.title('My first app') 
name=st.text_input("Enter your name", "Type Here ...")
if name:
    st.write('Hello, ', name, '!')
    
    # 