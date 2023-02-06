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
        st.title(":wave: Hey There, I'm Emmanuel")
        st.write("##")
        st.header("Eng. Electromechanical")
        st.write("""Argentinian | 40 years | Married""")
        st.write("Professional, oriented to obtaining results through organization, process improvement, efficiency and safety. "+
                 "With skills in managing and leading work teams")
        st.write("Learning backend development with finance oriented Python")
        st.markdown("**email:** emmanueldeloinaz@gmail.com")
        st.write("[LinkedIn >](https://www.linkedin.com/in/emmanuel-de-loinaz-57747265/)")

    st.write("##")
    st.write("English")   
    with open("resume_eng.pdf", "rb") as file:
            btn = st.download_button(
                label="Download Resume",
                data=file,
                file_name="Resume_Emmanuel.pdf"
              )
    st.write("##")
    st.write("Español")
    with open("resume.pdf", "rb") as file:
            btn = st.download_button(
                label="Descarga CV",
                data=file,
                file_name="CV_Emmanuel.pdf"
              )

    
    with col_ini_der:
        st_lottie(hola, height=300, key="hola")
    
# -----------------------------------------------------------------------
# ULTIMA PARTE - FORMULARIO DE CONTACTO
# --------------------------------------------------------------------------

with st.container():
    st.write("---")
    st.header (":mortar_board: Studies")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<h4>UNICEN Olavarría</h4>", unsafe_allow_html=True)
        st.write("Electromechanical Engineer")
        st.markdown("<h4>AUSTRAL Pilar Bs.As.</h4>", unsafe_allow_html=True)
        st.write("Diploma in Asset Management and Maintenance")
        st.write("##")
        st.markdown("<h4>ARN Nuclear Regulatory Authority</h4>", unsafe_allow_html=True)
        st.write("Authorization for the use of radioisotopes")

    with col2:
        st.markdown("<h4>Stock Exchange Bs.As.</h4>", unsafe_allow_html=True)
        st.write("Investment Instrument")
        st.markdown("<h4>Ruben J. Ullua</h4>", unsafe_allow_html=True)
        st.write("Python for Traders (Basic/Intermediate/Advanced)")



with st.container():
    st.write("---")
    st.header(":mailbox: Contact Me!") # Get in touch with me!
    st.write("##")

contact_form = """
    <form id="contactform" action="https://formsubmit.io/send/algomercados@gmail.com" method="POST">
    <input name="_captcha" type="hidden" value="false">
    <input name="name" type="text" id="name" placeholder="Name .." required>
    <input name="email" type="email" id="email" placeholder="Email .." required>
    <textarea name="comment" id="comment" rows="3" placeholder="Here your message .."></textarea>
    <input name="_formsubmit_id" type="text" style="display:none">
    <input value="Enviar" type="submit">
    </form>
"""

col_izq, col_der = st.columns(2)
with col_izq:
    st.markdown(contact_form, unsafe_allow_html=True)
with col_der:
    st.empty()