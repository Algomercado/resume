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
        st. header("Work Experience")
        
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
    st.header("Experience")
    with st.expander("Underground Mine Electrical Chief"):
        st.write("""
        - Manage the maintenance activities of the electrical distribution systems in medium and low voltage in the mine.
        - Ensure the safety and development of staff.
        - Manage the availability of energy for future developments.
        - Manage the maintenance process through KPI management.
        - Ensure that all work groups work within the guidelines required by the company, ensuring a safe and efficient workplace.
        - Detect the skills and motivation of the team to achieve individual development, improving the performance of the area.
        - Ensure compliance with the objectives of the area managed under my responsibility.
    """)
    with st.expander("Underground Mine Maintenance Engineer"):
        st.write("""
        - Plan, coordinate and control the electrical and mechanical maintenance of two new mining projects under development.
        - Optimize resources to accomplish area and company objectives.
        - Preparation and follow up of schedule.
        - Generate daily reports of management indicators.
        - Manage the daily activities and performance of the workgroup.
        - Perform analysis by fleet availability, MTBS, MTTR.
        - Minimize delays in the operation.
    """)
    with st.expander("Instrumentation Supervisor"):
        st.write("""
        - Asset Management.
        - Area weekly planning control.
        - Preparation and incorporation of typical spreadsheets to planning.
        - Management and control of plant shutdown tasks.
    """)
    with st.expander("Instrumentalist"):
        st.write("""
        - General instrument maintenance.
        - Rockwell PLC Programming, Devicenet Node Onboarding.
        - Parameterization of E3 and PowerFlex drives.
        - Incorporation of the fine line to the control system, programming and SCADA.
    """)


with tab2:
    st.subheader("2013 - 2017")
    st.write("##")
    st.subheader("Partner - Electrical Engineering")
    st.write("""
             - Provision of basic and detailed electrical engineering, PLC and SCADA programming for various projects at Cementos Avelaneda S.A.
             - Investment calculation and electrical preliminary project for the start-up of the facilities of a wet cement factory. 
             - Automation of the capping system for flour bagging machines at Molinos Cañuelas S.A. y Molinos Victoria S.A
             """)

with tab3:
    st.subheader("2010 - 2013")
    st.write("##")
    st.subheader("Electrical Project Engineer")
    st.write("""
             *Miscellaneous Projects*
             - Plant SCADA iFIX conversion, upgrade and migration.
             - Basic, detailed and programming engineering for various installations.
             - Construction supervision.
             """)

with tab4:
    st.subheader("2008 - 2010")
    st.write("##")
    st.subheader("Mechanical Projects")
    st.write("""
             *Miscellaneous Projects*
             - General implementation plans, development and basic mechanical calculation, details and exploded views suitable for construction.
             - Detail and exploded views of screw, conveyor belts, hoppers, discharges, compensators, metal structures, slides, etc.
             """)