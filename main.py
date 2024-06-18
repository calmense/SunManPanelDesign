# Schraubenbemessungsprogramm: Webapp mit Streamlit - Axial- und Schertragfähigkeit von Würth Vollgewindeschrauben
# Bibliotheken
from math import pi, sqrt, cos, sin
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from PIL import Image

# HTML Einstellungen
st.set_page_config(page_title="SunMan x ARUP", layout="wide")
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

# Eingangsparameter
# Listen
windZones = ['1', '2a', '2b', '3a', '3b', '4a', '4b', '4c']
windZonesCategory = ['Inland', 'Inland', 'Coast', 'Inland', 'Coast', 'Inland', 'Coast', 'Coast']
heightCategories = [[0.5, 0.65, 0.85, 0.8, 1.05, 0.95, 1.25, 1.4], [0.65, 0.8, 1.0, 0.95, 1.2, 1.15, 1.4, 'N/A'], [0.75, 0.9, 1.1, 1.1, 1.3, 1.3, 1.55, 'N/A']]

original_title = '<p style="font-family:Times; font-size: 60px;"> <span style="color:black;"></span>SunMan x <span style="color:rgb(230, 30, 40);">ARUP</span></p>'
st.markdown(original_title, unsafe_allow_html=True)

header = '<p style="font-family:Arial; color:rgb(0,0,0); font-size: 25px; font-weight: bold; ">SunMan Solar Panels - Ultra-light, Glass-free Technology</p>'
st.markdown(header, unsafe_allow_html=True)
st.write('This web tool provides a structural framework for adhering solar panels directly onto roofs without the need for screws. \
         The panels are made from a durable, glass-free organic polymer composite that excels in various climatic conditions and extreme temperatures. \
         Please note that the tool does not assume responsibility for any errors, and users are advised to verify the results independently.')






#__________________________________________________
#__________Main___________________________________
#__________________________________________________
    
with st.sidebar:
    header = '<p style="font-family:Arial; color:rgb(0,0,0); font-size: 25px; font-weight: bold; ">Wind Loading</p>'
    st.markdown(header, unsafe_allow_html=True)
    st.latex(r"\textbf{Velocity Pressure}")
    st.caption("DIN EN 1991-1-1: xx")

    col1, col2 = st.columns(2)
    with col1:
        windZone = st.selectbox('Wind Zone', ["1", "2a", "2b", "3a", "3b", "4a", "4b", "4c"])

    with col2:
        buildingHeight = int(st.text_input('Building Height [m]', 10))
        index = windZones.index(windZone)

        if buildingHeight <= 10:
            heightCategory = 1
        elif buildingHeight > 10 and buildingHeight <= 18:
            heightCategory = 2
        elif buildingHeight > 18 and buildingHeight <= 25:
            heightCategory = 3

        velocityPressure = heightCategories[heightCategory][index]

    col1, col2 = st.columns(2)
    with col1:
        st.write("")

    st.latex(r"\textbf{Flat Roof}")
    st.caption("DIN EN 1991-1-1: xx")
    col1, col2 = st.columns(2)
    with col1:
        buildingLength = int(st.text_input('Building Length [m]', 100))

    with col2:
        buildingWidth = int(st.text_input('Building Width [m]', 10))

    col1, col2 = st.columns(2)
    with col1:
        e1 = min(2*buildingHeight, buildingLength)
        e2 = min(2*buildingHeight, buildingWidth)
        e_10_1 = e1/10
        e_10_2 = e2/10
        e_4_1 = e1/4
        e_4_2 = e2/4

    st.latex(r"\textbf{Additional Loading Factors}")
    st.caption("DIN EN 1991-1-1: xx")
    col1, col2 = st.columns(2)
    with col1:
        partialSafetyFactor = float(st.text_input('Partial safety factor 𝜓', 1.2))

    with col2:
        additionalFactor = float(st.text_input('Additional factor 𝜒', 1.5))

    # Define the headers and the cells of the table
    headers = ['F', 'G', 'H', 'I']
    coefficients = [-2.50, -2.00, -1.20, -0.60]

    # Calculate wk and wd based on coefficients
    wk = [velocityPressure * x for x in coefficients]
    wd = [round(x * partialSafetyFactor * additionalFactor, 2) for x in wk]
    colHeader = ["coefficients", "wk", "wd"]
    colF = [coefficients[0], wk[0], wd[0]]
    colG = [coefficients[1], wk[1], wd[1]]
    colH = [coefficients[2], wk[2], wd[2]]
    colI = [coefficients[3], wk[3], wd[3]]


    # Create the table

    fig = go.Figure(data=[go.Table(
        header=dict(values=[''] + headers,  # Empty string for the first header cell
                    fill_color='white',
                    height=30,
                    font=dict(color='red', size=16, family="Times New Roman"),
                    line=dict(color='darkslategray', width=2),
                    align='center'),
        cells=dict(values=[colHeader, colF, colG, colH, colI],              
                fill_color=['white', 'white', 'white'],  # Alternating row colors
                height=30,
                font=dict(color='black', size=16, family="Times New Roman"),
                line=dict(color='darkslategray', width=2),
                align='center'))
    ])

    # Set table layout
    fig.update_layout(
        width=600,
        height=200,
        margin=dict(l=5, r=5, t=10, b=10)
    )




## PANEL DESIGN
st.latex(r"\textbf{Design Wind Load}")
with st.expander("Expand"):
    st.latex(r"\text{Velocity Pressure }" + ' q_{p} = ' + str(velocityPressure) + 'N/mm^2')
    st.latex(r"\text{Additional Factor }" + ' \chi = ' + str(additionalFactor))
    st.latex(r"\text{Partial Safety Factor }" + ' \psi = ' + str(partialSafetyFactor))
    st.write("")
    st.latex(r"\text{Wind Loading }" + 'kN/m^2')
    st.plotly_chart(fig)


st.latex(r"\textbf{Solar Panel Design}")
with st.expander("Expand"):

    col1, col2 = st.columns(2)
    with col1:
        panelSize = st.selectbox('Panel Size', [1, 2])
    with col2:
        gluingConfig = st.selectbox('Gluing Configuration Size', [1, 2])

    gapx = 0
    gapy = 0

    # solar panel
    if panelSize == 1:
        width = 1080
        height = 2054
        area = width * height
        
    else:
        width = 1197
        height = 2246
        area = width * height

    if gluingConfig == 1:
        if panelSize == 1:
            distance = (height - 100) / 4
            linesXCoords = [[gapx, width + gapx], [gapx, width + gapx], [gapx, width + gapx], [gapx, width + gapx], [gapx, width + gapx]]
            linesYCoords = [[gapy + 50, gapy + 50], [gapy + 50 + distance, gapy + 50 + distance], [gapy + 50 + distance*2, gapy + 50 + distance*2], [gapy + 50 + distance*3, gapy + 50 + distance*3], [gapy + 50 + distance*4, gapy + 50 + distance*4]]
        else:
            distance = (height - 100) / 5
            linesXCoords = [[gapx, width + gapx], [gapx, width + gapx], [gapx, width + gapx], [gapx, width + gapx], [gapx, width + gapx], [gapx, width + gapx]]
            linesYCoords = [[gapy + 50, gapy + 50], [gapy + 50 + distance, gapy + 50 + distance], [gapy + 50 + distance*2, gapy + 50 + distance*2], [gapy + 50 + distance*3, gapy + 50 + distance*3], [gapy + 50 + distance*4, gapy + 50 + distance*4], [gapy + 50 + distance*5, gapy + 50 + distance*5]]
    
    elif gluingConfig == 2:
        if panelSize == 1:
            distance = (width - 100) / 2
            linesXCoords = [[gapx + 50, gapx + 50], [gapx + 50 + distance, gapx + 50 + distance], [gapx + 50 + distance*2, gapx + 50 + distance*2]]
            linesYCoords = [[gapx, gapx + height], [gapx, gapx + height], [gapx, gapx + height]]
        else:
            distance = (width - 100) / 3
            linesXCoords = [[gapx + 50, gapx + 50], [gapx + 50 + distance, gapx + 50 + distance], [gapx + 50 + distance*2, gapx + 50 + distance*2], [gapx + 50 + distance*3, gapx + 50 + distance*3]]
            linesYCoords = [[gapx, gapx + height], [gapx, gapx + height], [gapx, gapx + height], [gapx, gapx + height]]

    scaleY = height / 400
    scaleX = 400 / height

    fig = go.Figure(go.Scatter(x=[gapx + 0,gapx + width,gapx + width,gapx + 0, gapx + 0], 
                            y=[0 + gapy,0 + gapy, height + gapy,height + gapy, 0 + gapy], 
                            line=dict(color='darkgrey'),
                            mode="lines",
                            fillcolor='lightgrey',  
                            fill="toself",
                            opacity=0))

    # hatching
    pyLogo = Image.open("hatch.png")
    fig.add_layout_image(
            dict(source=pyLogo, xref="x", yref="y",
                x = gapx, y = gapy + height,
                sizex = width, sizey = height,
                sizing = "stretch",
                layer="below"))

    def draw_line(fig, xList, yList, size, color, opacity):
        fig.add_trace(go.Scatter(x = list(reversed(xList)), y = list(reversed(yList)), 
                                mode="lines", line=dict(color=color, width=size / 5), opacity=opacity))

    for i in range(len(linesYCoords)):
        draw_line(fig, linesXCoords[i], linesYCoords[i], 12, "red", 1)

    #____________________TEXT____________________
    # text sizes
    titleSize = + 20

    # update layout
    fig.update_layout(
        autosize=False,
        width = 500,
        height = 700,
        uirevision='static',
        xaxis=dict(scaleanchor="y", scaleratio=1, fixedrange=True, visible=False),
        yaxis=dict(scaleanchor="x", scaleratio=1, fixedrange=True, visible=False),
        paper_bgcolor='white', 
        plot_bgcolor='white', 
        showlegend=False)


    # Hide the axis
    fig.update_xaxes(showline=False, showgrid=False, zeroline=False)
    fig.update_yaxes(showline=False, showgrid=False, zeroline=False)

    col1, col2 = st.columns(2)
    with col1:
        st.write("")
        st.latex(r"\text{SunMan Solar Panel - Gluing Configuration }")
        st.write(fig)

    with col2:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")


        st.latex(r"\textbf{Solar Panel}")
        st.latex(r"\text{Width }" + ' B = ' + str(width) + ' mm')
        st.latex(r"\text{Length }" + ' L = ' + str(height) + ' mm')
        st.latex(r"\text{Area }" + ' A = ' + str(round(area*0.001**2,1)) + ' m^2')
