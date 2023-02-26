import webbrowser
from matplotlib import image
import streamlit as st
import streamlit.components.v1 as components

st.title("Hello There 👋 \n ")
st.header(" I am S. Vamshi Krishna \n Data Science Intern @ Innomatics Research Labs ")

st.markdown("Learning and Implementing Data Science & Machine Learning Since 2021")
st.markdown("Let's Connect !")


ln = st.button(label="LinkedIn")
if ln == True:
    webbrowser.open("https://www.linkedin.com/in/vamshi-krishna-shanigarapu-228587219/")


ln = st.button(label="GitHub")
if ln == True:
    webbrowser.open("https://github.com/VamshiKrsna")
