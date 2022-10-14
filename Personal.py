import streamlit as st
from streamlit_lottie import st_lottie
import json

st.set_page_config(page_title="Emmanuel_Resume", page_icon=":book:", layout="wide")

# ESTA FUNCIÓN LEE LOS ARCHIVOS LOTTIE DIRECTAMENTE DE LA WEB
#def load_lottieurl(url):
#    r = requests.get(url)
#    if r.status_code != 200:
#        return None
#    return r.json()

def load_lottiefile(filepath:str):
    with open(filepath, "r") as f:
        return json.load(f)

hola = load_lottiefile("lottiefiles/hola.json")
        
#computacion = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_w51pcehl.json")
#ingenieria = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_f8arnpdn.json")
#hola = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_wtpprtnc.json")
#data_science = load_lottieurl("https://assets3.lottiefiles.com/private_files/lf30_8z6ubjgk.json")
#graficas = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_q5qeoo3q.json")
#linkedin = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_ijoepf55.json")


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# -----------------------------------------------------------------------------
# PARTE SUPERIOR - DESCRIPCIÓN PERSONAL
# -----------------------------------------------------------------------------
with st.container():
    col_ini_iz, col_ini_der = st.columns([2,1])
    with col_ini_iz:
        st.title(":wave: Hola! soy Emmanuel")
        st.write("##")
        st.header("Ing. Electromecánico")
        st.write("""Argentino | 40 años | Casado | Dos Hijos""")
        st.write("Profesional, orientado a la obtención de resultados mediante la organización, mejora de procesos, eficiencia y seguridad. "+
                 "Con habilidades en gestión y conducción de equipos de trabajo")
        st.write("Aficionado al desarrollo backend con Python orientado en finanzas")
        st.markdown("**email:** emmanueldeloinaz@gmail.com")
        st.write("[LinkedIn >](https://www.linkedin.com/in/emmanuel-de-loinaz-57747265/)")
        
    with open("resume.pdf", "rb") as file:
            btn = st.download_button(
                label="Descarga CV",
                data=file,
                file_name="Resume_Emmanuel.pdf"
              )
    
    with col_ini_der:
        st_lottie(hola, height=300, key="hola")
    
# -----------------------------------------------------------------------
# ULTIMA PARTE - FORMULARIO DE CONTACTO
# --------------------------------------------------------------------------

with st.container():
    st.write("---")
    st.header (":mortar_board: Educación")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<h4>ENET N°2 Olavarría Bs.As.</h4>", unsafe_allow_html=True)
        st.write("Técnico Mecánico Electricista")
        st.markdown("<h4>UNICEN Olavarría</h4>", unsafe_allow_html=True)
        st.write("Ingeniero Electromecánico")
        st.markdown("<h4>AUSTRAL Pilar Bs.As.</h4>", unsafe_allow_html=True)
        st.write("Diplomatura en gestión de activos y mantenimiento")
        st.write("##")
        st.markdown("<h4>ARN Autoridad Regulatoria Nuclear</h4>", unsafe_allow_html=True)
        st.write("Habilitación para el uso de radioisótopos")
        st.write("##")
        st.write("Ingles Avanzado")
    with col2:
        st.markdown("<h4>Bolsa de Comercio Bs.As.</h4>", unsafe_allow_html=True)
        st.write("Instrumento de Inversión")
        st.markdown("<h4>Ruben J. Ullua</h4>", unsafe_allow_html=True)
        st.write("Python para Traders (Básico/Intermedio/Avanzado)")



with st.container():
    st.write("---")
    st.header(":mailbox: Contactame!") # Get in touch with me!
    st.write("##")

contact_form = """
    <form id="contactform" action="https://formsubmit.io/send/algomercados@gmail.com" method="POST">
    <input name="_captcha" type="hidden" value="false">
    <input name="name" type="text" id="name" placeholder="Nombre .." required>
    <input name="email" type="email" id="email" placeholder="Email .." required>
    <textarea name="comment" id="comment" rows="3" placeholder="Aqui tu mensaje .."></textarea>
    <input name="_formsubmit_id" type="text" style="display:none">
    <input value="Enviar" type="submit">
    </form>
"""

col_izq, col_der = st.columns(2)
with col_izq:
    st.markdown(contact_form, unsafe_allow_html=True)
with col_der:
    st.empty()