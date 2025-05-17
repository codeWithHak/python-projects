import streamlit as st

st.header("The Goat Unit Converter")

meter_conversions = {
    "meter":1,
    "kilometer":1000,
    "centimeter": 0.01,
    "millimetre":0.001,
    "micrometre":0.000001,
    "nanometer":0.000000001,
    "mile":1609.34,
    "yard": 0.9144,
    "foot":0.3048,
    "inch":0.0254,
}

col1,col2,col3 = st.columns([6,1,6])

selected_value_from = col1.number_input("Select Value",key='from',value=None)
selected_unit_from = col1.selectbox("From",meter_conversions,label_visibility="collapsed") 

col2.markdown("<div style='text-align:center; margin-top: 32px; font-size:22px'>=</div>", unsafe_allow_html=True)

a = 10
b = 10
val = a * b

selected_value_to = col3.number_input("Select Value", key='to', value=val)
selected_unit_to = col3.selectbox("To",meter_conversions, label_visibility="collapsed")

st.write(selected_unit_from)