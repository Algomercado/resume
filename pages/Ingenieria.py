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

ingenieria = load_lottiefile("lottiefiles/ingeniero.json")

with st.container():
    col_izq, col_der = st.columns(2)
    with col_izq:
        st. header("Experiencia Laboral")
        
    with col_der:
        st_lottie(ingenieria, height=200, key="ing")

tab1, tab2, tab3, tab4 = st.tabs(["Pan American Silver",
                                  "Geprel", 
                                  "Cementos Avellaneda S.A.", 
                                  "Lopez&Pin"
                                  ])

with tab1:
    st.subheader("2016 - ")
    st.write("##")
    st.header("Experiencia")
    with st.expander("Jefe Eléctrico Mina Subterranea"):
        st.write("""
        - Gestionar las actividades de mantenimiento de los sistemas de distribución eléctrica en media y baja tensión en mina.
        - Velar por la seguridad y desarrollo del personal.
        - Gestionar la disponibilidad de energía a futuros desarrollos.
        - Administrar el proceso de mantenimientos mediante gestión de KPI.
        - Asegurar que todos los grupos de trabajo bajo su control trabajen dentro de las pautas requeridas por la empresa, asegurando un lugar de trabajo seguro y eficiente.
        - Detectar las competencias y la motivación del equipo para lograr el desarrollo individual mejorando el desempeño del área.
        - Asegurar el cumplimiento de los objetivos del área administradas bajo mi responsabilidad.
    """)
    with st.expander("Ingeniero Mantenimiento Mina Subterranea"):
        st.write("""
        - Planificar, coordinar y controlar el mantenimiento eléctrico y mecánico de dos nuevos proyectos mineros en fase de desarrollo.
        - Optimizar los recursos para cumplir con los objetivos de área y de la empresa.
        - Elaboración y seguimiento de cronograma.
        - Generar reportes diarios de indicadores de gestión.
        - Administrar las actividades y el desempeño diario del grupo de trabajo.
        - Realizar análisis por flota de disponibilidad, MTBS, MTTR.
        - Administrar el volumen de trabajo de la planificación semanal con un mínimo de tiempo de inactividad o de pérdidas de producción.
        - Minimizar las demoras en la operación.
    """)
    with st.expander("Supervisor Instrumentación"):
        st.write("""
        - Personal a cargo: 3 personas
        - Gestión de activos
        - Control de planificación semanal del área
        - Confección e incorporación de planillas típicas a planificación.
        - Gestión y control de tareas en parada de planta.
    """)
    with st.expander("Instrumentista"):
        st.write("""
        - Mantenimiento general de instrumentos.
        - Programación de PLC Rockwell, Incorporación de nodos Devicenet.
        - Parametrización de E3 y variadores PowerFlex.
        - Incorporación de línea de finos al sistema de control, Programación y SCADA.
    """)


with tab2:
    st.subheader("2013 - 2017")
    st.write("##")
    st.subheader("Socio - Ingeniería Eléctrica")
    st.write("""
             - Provisión de ingeniería eléctrica básica y de detalle, programación PLC y SCADA para proyectos varios en Cementos Avelaneda S.A.
             - Cálculo de inversión y anteproyecto eléctrico para la puesta en marcha de las instalaciones de una fábrica de cemento de vía húmeda. 
             - Automatización del sistema de emboquillado para embolsadoras de harina Molinos Cañuelas S.A. y Molinos Victoria S.A
             """)

with tab3:
    st.subheader("2010 - 2013")
    st.write("##")
    st.subheader("Ingeniero de Proyectos Eléctricos")
    st.write("""
             *Proyectos Varios*
             - Conversión, actualización y migración SCADA iFIX de la planta.
             - Ing. Básica, de detalle y programación para instalaciones varias.
             - Supervición de obra.
             """)

with tab4:
    st.subheader("2008 - 2010")
    st.write("##")
    st.subheader("Cadista - Proyectos Mecánicos")
    st.write("""
             *Proyectos Varios*
             - Planos de implantación general, desarrollo y cálculo básico mecánico, detalles y despieces aptos para construir.
             - Planos de detalle y despiece de sinfin, bandas transportadoras, tolvas, descargas, compensadores, estructuras metálicas, resbaladeras, etc.
             """)