from dotenv import load_dotenv
load_dotenv()   # Loading all the environment varaibles 

import streamlit as st 
import os 
import google.generativeai as genai


genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

## Function to load gemini pro model 


model=genai.GenerativeModel('gemini-pro')
chat=model.start_chat(history=[])

def get_gemini_response(question):
    response=chat.send_message(question,stream=True)
    return response 

st.set_page_config(page_title='Q & A demo')

st.header('Gemini LLM application')

if 'chat_history' not in st.session_state:
    st.session_state['chat_history']=[]
    
    
input=st.text_input('Input: ',key='input')
submit=st.button('Ask the Question')


if submit and input:
    response=get_gemini_response(input)
    ## Add user query and response to session chat history 
    st.session_state['chat_history'].append(('You',input))
    st.subheader('The response is ')
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(('Bot',chunk.text))
        
        
st.subheader('The chat History is ')

for role,text in st.session_state['chat_history']:
    st.write(f'{role}:{text}')
        