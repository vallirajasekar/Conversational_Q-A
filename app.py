from dotenv import load_dotenv
load_dotenv()   # Loading all the environment varaibles 

import streamlit as st 
import os 
import google.generativeai as genai


genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))


## Function to load generative pro model and get response 
model=genai.GenerativeModel('gemini-pro')
def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text

## Initialize our Streamlit app

st.set_page_config(page_title='Q & A demo')

st.header('Gemini LLM application')

input=st.text_input('Input: ',key='input')
submit=st.button('Ask the Question')

## When submit is Clicked 

if submit:
    response=get_gemini_response(input)
    st.subheader('The response is')
    st.write(response)
    

    
 