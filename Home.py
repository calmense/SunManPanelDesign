# Schraubenbemessungsprogramm: Webapp mit Streamlit - Axial- und Schertragfähigkeit von Würth Vollgewindeschrauben
# Bibliotheken
from math import pi, sqrt, cos, sin
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from PIL import Image

# from würth_screws_functions import get_length, ec5_87_tragfähigkeit_vg, get_min_distances_axial, get_min_distances_shear

# HTML Einstellungen
st.set_page_config(page_title="SunMan Solar Panel Designer", layout="wide")
st.markdown("""<style>
[data-testid="stSidebar"][aria-expanded="false"] > div:first-child {width: 500px;}
[data-testid="stSidebar"][aria-expanded="false"] > div:first-child {width: 500px;margin-left: -500px;}
footer:after{
    content:"Arup Deutschland GmbH | SunMan Energy | Cal Mense";
    display:block;
    position:relative;
    color:grey;
}
</style>""",unsafe_allow_html=True)

st.markdown('''
<style>
.katex-html {
    text-align: left;
}
</style>''',
unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    .subsubheader {
        font-size: 1.5em; /* Adjust the font size as needed */
        font-weight: bold;
        margin-top: 0em; /* Adjust the margin as needed */
        color: rgb(230, 30, 40); /* Change the color as needed */
    }
    .text {
        font-size: 1.0em; /* Adjust the font size as needed */
        margin-top: 0em; /* Adjust the margin as needed */
        color: "black"; /* Change the color as needed */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("""
    <style>
    .header-button {
        display: inline-block;
        padding: 5px 15px;
        font-size: 1.5rem;  /* Use a similar size as st.header */
        font-weight: 600;  /* Bold to match the header style */
        color: black;
        background-color: #F0F2F6;  /* Change this to match your theme */
        border: none;
        border-radius: 5px;
        cursor: pointer;
        text-decoration: none;
    }
    .header-button:hover {
        background-color: #F0F2F6;  /* Lighten color on hover */
    }
    </style>
""", unsafe_allow_html=True)

original_title = '<p style="font-family:Times; font-size: 60px;"> <span style="color:black;"></span>SunMan x <span style="color:rgb(230, 30, 40);">ARUP</span></p>'
st.image("images/Sunman_logo.png", width = 300)
# st.markdown(original_title, unsafe_allow_html=True)

# header = '<p style="font-family:Arial; color:rgb(0,0,0); font-size: 25px; font-weight: bold; ">SunMan Solar Panels - Ultra-light, Glass-free Technology</p>'
# st.markdown(header, unsafe_allow_html=True)
st.subheader("SunMan Solar Panels - Ultra-light, Glass-free Technology")
st.write('This web tool provides a structural framework for adhering solar panels directly onto roofs without the need for screws. \
         The panels are made from a durable, glass-free organic polymer composite that excels in various climatic conditions and extreme temperatures. \
         Please note that the tool does not assume responsibility for any errors, and users are advised to verify the results independently.')

st.write("")
st.write("")
st.write("")

col1, col2 = st.columns([40,70])
with col1:
    st.image("images/title_image.png", width=450)
with col2:


    st.write('This document provides structural guidance for adhering solar panels directly to roofs without the need for screw penetrations. \
        The solar panels utilize an organic polymer composite, devoid of glass, known for its exceptional durability in withstanding diverse climatic conditions and extreme temperatures. \
    ')

    st.write('For more information, please visit: [https://de.sunman-energy.com/](https://de.sunman-energy.com/)')
