import streamlit as st
from streamlit_lottie import st_lottie
import json

st.set_page_config(page_title="Emmanuel_Resume", page_icon=":book:", layout="wide")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

def load_lottiefile(filepath:str):
    with open(filepath, "r") as f:
        return json.load(f)

computacion = load_lottiefile("lottiefiles/computer.json")

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