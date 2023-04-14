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
        st. header("Personal Projects")
        st.subheader("Finance with Python")
        
    with col_der:
        st_lottie(computacion, height=200, key="ing")

st.write("---")
st.markdown("- ETL application of an instrument for measuring electrical parameters  [_check this link_](https://me435-registro.streamlit.app/) ")
st.markdown("- Telegram Bot hosting on Oracle Cloud  [_check this link_](https://t.me/AlgoMercado_bot) ")
st.write("""
        - Market connection via API.
        - DDBB registration in local network (Postgresql / MariaDB / SQLite).
        - Strategy analysis and signal sending to Telegram running on Oracle Cloud Service.
        - Bonus arbitrator bot running on Oracle Cloud Service.
        - Registration in Googlesheet for follow up or sending by email.
        - Portfolio Optimization.
        - Version control with GitHub.
        - web Frameworks (Flask / FastAPI)
         """)
st.write("##")
st.write("""
         *Learning ...*
        - Machine Learning.
        - Options Strategy.
        - Cloud service.
         """)