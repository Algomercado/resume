import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import requests
import numpy as np

st.set_page_config(page_title="Emmanuel_Resume", page_icon=":book:", layout="wide")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

computacion = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_w51pcehl.json")

with st.container():
    col_izq, col_der = st.columns(2)
    with col_izq:
        st. header("Proyectos Personales")
        st.subheader("Finanzas con Python")
        
    with col_der:
        st_lottie(computacion, height=200, key="ing")

st.write("---")
st.write("""
        - Conexión a mercado mediante API.
        - Registro en DDBB en red local (Postgresql / MariaDB / SQLite).
        - Análisis de estrategias varias y envío de señal a Telegram.
        - Bot arbitrador de bonos.
        - Registro en Googlesheet para seguimiento y/o envío por email.
        - Optimización de Portafolios.
        - Control de versión con GitHub.
         """)
st.write("##")
st.write("""
         *Aprendiendo ...*
        - Machine Learning.
        - Estrategias de opciones.
         """)