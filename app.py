import streamlit as st
from langchain.llms import Cohere
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()


# Function to return the response
def load_answer(question):
    llm = Cohere(temperature=0)  # Correct instantiation
    answer = llm.invoke(question)
    return answer

# App UI starts here
st.set_page_config(page_title="LangChain First Question Answer Project", page_icon=":robot:")
st.header("LangChain Demo")

# Gets the user input
def get_text():
    input_text = st.text_input("You: ", key="input")
    return input_text

user_input = get_text()
response = None

# If generate button is clicked
submit = st.button('Generate')  
if submit and user_input:   
    response = load_answer(user_input)
    st.subheader("Answer:")
    st.write(response)
