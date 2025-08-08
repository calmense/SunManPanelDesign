import streamlit as st
import plotly.graph_objects as go
from PIL import Image

from utils.utils import add_text, draw_arrow

def glue_resistance_section(wd, figBuilding):


    glueManufacturer = ["Dow", "Scott Bader", "Soudal", "Innotec"]
    glueAdhesive = ["Dowsil 895", "Crestabond M7-15", "Soudalbond 677", ["Versabond", "Membrane Adhesive", "Adheseal"]]
    glueAdhesiveValue = [0.14, 21.54, 3.8, [0.4, 1.4, 2.6]]
    minWidthValues = [6, 10, 30, 10]
    minThicknessValues = [3, 1, 3, 3, 3, 3]
    
    st.write("")
    st.write("")
    st.write("")
    col1, col2 = st.columns([1,22])
    with col1:
        st.image("images/icon4.png", width=50)
    with col2:
        st.subheader("Glue Joint Resistance")

    st.write('The glue joint resistance needs to be obtained and verified from a glue manufacturer according to European standards.')
    st.write("")
    st.write("")

    with st.expander("Expand"):

        st.markdown("#### Input Parameters")
        st.write('Chose between two panel sizes and chose a design glue joint resistance.')

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            panelSize = st.selectbox('Panel Size', ["SMF430", "SMF520"])

        with col2:
            glueManufacturerSelected = st.selectbox('Glue Manufacturer', glueManufacturer)
            indexManufacturer = glueManufacturer.index(glueManufacturerSelected)
            minWidth = minWidthValues[indexManufacturer]
            minThickness = minThicknessValues[indexManufacturer]

        with col3:
            glueSelected = st.selectbox('Adhesives', glueAdhesive[indexManufacturer])


        # Dynamisch je nach Struktur (Liste oder Einzelwert)
        if glueManufacturerSelected == "Innotec":
            indexManufacturer = ["Versabond", "Membrane Adhesive", "Adheseal"].index(glueSelected)
            glueValue = [0.4, 1.4, 2.6][indexManufacturer]
            
        else:
            indexManufacturer = glueManufacturer.index(glueManufacturerSelected)
            glueValue = glueAdhesiveValue[indexManufacturer]

        st.write("")
        designGlueJointResistanceValue = round(glueValue / (1.3 * 1.6 * 1.0),2)

        if glueManufacturerSelected in ["Dow"]:
            if glueSelected == "Dowsil 895":
                designGlueJointResistanceValue = 0.14


            st.markdown(
                '<b>Note:</b> The adhesive is <b>ETAG-approved</b>, so the design strength '
                'R<sub>d</sub> is provided in the datasheet, and no additional reduction factors are required.',
                unsafe_allow_html=True
            )
            st.markdown(f'Design Strength <b> R<sub>d</sub> = {designGlueJointResistanceValue} N/mm²', unsafe_allow_html=True)

        else:
            st.markdown(
                '<b>Note:</b> The adhesive is <b>not ETAG-approved</b>, so the characteristic strength '
                'R<sub>k</sub> must be multiplied by appropriate reduction factors to determine R<sub>d</sub>.',
                unsafe_allow_html=True
            )
            st.markdown(f'Characteristic Strength: <b>R<sub>k</sub> = {glueValue} N/mm²</b>', unsafe_allow_html=True)

            st.markdown(
                f'Design Strength: <b>R<sub>d</sub> = R<sub>k</sub> / (γ<sub>M</sub> · K<sub>A</sub> · K<sub>𝜃</sub>) '
                f'= R<sub>k</sub> / 2.08 = {designGlueJointResistanceValue} N/mm²</b>',
                unsafe_allow_html=True
            )
                                                        
        gapx = 0
        gapy = 0

        # solar panel
        if panelSize == "SMF430":
            numberGlueLines = 5
            width = 1080
            height = 2054
            area = width * height
            
        else:
            numberGlueLines = 6
            width = 1197
            height = 2246
            area = width * height

        glueLength = numberGlueLines*width

        if panelSize == "SMF430":
            gluingDistance = (height - 100) / 4
            linesXCoords = [[gapx, width + gapx], [gapx, width + gapx], [gapx, width + gapx], [gapx, width + gapx], [gapx, width + gapx]]
            linesYCoords = [[gapy + 50, gapy + 50], [gapy + 50 + gluingDistance, gapy + 50 + gluingDistance], [gapy + 50 + gluingDistance*2, gapy + 50 + gluingDistance*2], [gapy + 50 + gluingDistance*3, gapy + 50 + gluingDistance*3], [gapy + 50 + gluingDistance*4, gapy + 50 + gluingDistance*4]]
        else:
            gluingDistance = (height - 100) / 5
            linesXCoords = [[gapx, width + gapx], [gapx, width + gapx], [gapx, width + gapx], [gapx, width + gapx], [gapx, width + gapx], [gapx, width + gapx]]
            linesYCoords = [[gapy + 50, gapy + 50], [gapy + 50 + gluingDistance, gapy + 50 + gluingDistance], [gapy + 50 + gluingDistance*2, gapy + 50 + gluingDistance*2], [gapy + 50 + gluingDistance*3, gapy + 50 + gluingDistance*3], [gapy + 50 + gluingDistance*4, gapy + 50 + gluingDistance*4], [gapy + 50 + gluingDistance*5, gapy + 50 + gluingDistance*5]]


        figPanel = go.Figure(go.Scatter(x=[gapx + 0,gapx + width,gapx + width,gapx + 0, gapx + 0], 
                                y=[0 + gapy,0 + gapy, height + gapy,height + gapy, 0 + gapy], 
                                line=dict(color='darkgrey'),
                                mode="lines",
                                fillcolor='lightgrey',  
                                fill="toself",
                                opacity=0))

        # hatching
        pyLogo = Image.open("images/hatch.png")
        figPanel.add_layout_image(
                dict(source=pyLogo, xref="x", yref="y",
                    x = gapx, y = gapy + height,
                    sizex = width, sizey = height,
                    sizing = "stretch",
                    layer="below"))

        def draw_line(figPanel, xList, yList, size, color, opacity):
            figPanel.add_trace(go.Scatter(x = list(reversed(xList)), y = list(reversed(yList)), 
                                    mode="lines", line=dict(color=color, width=size / 5), opacity=opacity))

        for i in range(len(linesYCoords)):
            draw_line(figPanel, linesXCoords[i], linesYCoords[i], 12, "red", 1)

        #____________________TEXT____________________
        # text sizes
        titleSize = + 20

        # update layout
        figPanel.update_layout(
            autosize=False,
            width = 500,
            height = 700,
            uirevision='static',
            xaxis=dict(scaleanchor="y", scaleratio=1, fixedrange=True, visible=False),
            yaxis=dict(scaleanchor="x", scaleratio=1, fixedrange=True, visible=False),
            paper_bgcolor='white', 
            plot_bgcolor='white', 
            showlegend=False)
        
        factor = 8
        
        # dimension width
        xList = [-100, -100]
        yList = [0, 0+height]
        draw_arrow(figPanel, xList, yList, "Y", factor, factor)
        add_text(figPanel, height, -300 , height/2, 15)

        # dimension height
        xList = [0, 0+width]
        yList = [-100, -100]
        draw_arrow(figPanel, xList, yList, "X", factor, factor)
        add_text(figPanel, width, width/2 -100 , -200, 15)

        # gluing distance
        xList = [width + 100, width + 100]
        yList = [50, 50 + gluingDistance]
        draw_arrow(figPanel, xList, yList, "Y", factor, factor)
        add_text(figPanel, int(gluingDistance), width + 150 , 50+gluingDistance/2, 15)

        # Hide the axis
        figPanel.update_xaxes(showline=False, showgrid=False, zeroline=False)
        figPanel.update_yaxes(showline=False, showgrid=False, zeroline=False)

        col1, col2 = st.columns(2)
        with col1:
            st.write("")
            st.markdown("#### SunMan Solar Panel")
            st.write(figPanel)

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

            st.markdown("#### Solar Panel")
            st.markdown(f'Width: <b>B = {width} mm</b>', unsafe_allow_html=True)
            st.markdown(f'Length: <b>L = {height} mm</b>', unsafe_allow_html=True)
            st.markdown(f'Area: <b>A = {round(area * 0.001**2, 1)} m²</b>', unsafe_allow_html=True)
            st.markdown(f'Gluing Distance: <b>a = {int(gluingDistance)} mm</b>', unsafe_allow_html=True)
            st.markdown(f'Design Glue Joint Resistance: <b>R<sub>d</sub> = {round(designGlueJointResistanceValue, 2)} N/mm²</b>', unsafe_allow_html=True)
            st.write("")
            st.write("")
            
        st.markdown("#### Gluing Design Table")
        st.write('This table shows the required glue width.')

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            
            st.markdown(f'Min. Gluing Width: <b>b = {minWidth} mm</b>', unsafe_allow_html=True)
            st.markdown(f'Min. Gluing Thickness: <b>t = {minThickness} mm</b>', unsafe_allow_html=True)

        # Define the headers and the cells of the table
        headers = ['F', 'G', 'H']

        # Calculate wk and wd based on coefficients
        glueWidthReq = [round( abs(wdi) * (gluingDistance / 1000)/ (designGlueJointResistanceValue), 0) for wdi in wd]
        glueWidthFinal = [int(max(glueWidthReq[x], minWidth)) for x in range(len(glueWidthReq))]   

        colHeader = ["Wind Load [N/mm2]", "Glue Width [mm]", "Glue Width [mm]"]
        colExpl = ["design", "required", "final"]

        colF = [str(abs(wd[0])) , str(round(glueWidthReq[0])), str(glueWidthFinal[0])]
        colG = [str(abs(wd[1])) , str(round(glueWidthReq[1])), str(glueWidthFinal[1])]
        colH = [str(abs(wd[2])) , str(round(glueWidthReq[2])), str(glueWidthFinal[2])]

        # Create the table
        figCheck = go.Figure(data=[go.Table(
            header=dict(values=['Roof area', 'Explanation'] + headers,  # Adding 'Roof Area' and other headers
                        fill_color='white',
                        height=35,
                        font=dict(color='red', size=16, family="Times New Roman"),
                        line=dict(color='darkslategray', width=2),
                        align='center'),
            cells=dict(values=[colHeader, colExpl, colF, colG, colH],
                    fill_color=['white', 'white', 'white', 'white'],
                    height=35,
                    font=dict(color=['red', 'grey', 'black', 'black', 'black'], size=16, family="Times New Roman"),
                    line=dict(color='darkslategray', width=2),
                    align='center'))
        ])

        # Set table layout
        figCheck.update_layout(
            width=900,
            height=230,
            margin=dict(l=5, r=5, t=10, b=10)
        )

        st.write(figCheck)

        return {
            "panelSize": panelSize,
            "width": width,
            "height": height,
            "area": area,
            "gluingDistance": gluingDistance,
            "figPanel": figPanel,
            "figCheck": figCheck,
            "glueManufacturerSelected": glueManufacturerSelected,
            "glueSelected": glueSelected,
            "glueValue": glueValue,
            "designGlueJointResistanceValue": designGlueJointResistanceValue,
            "glueWidthReq": glueWidthReq,
            "glueWidthFinal": glueWidthFinal,
            "numberGlueLines": numberGlueLines,
            "glueLength": glueLength,
            "minThickness": minThickness,
        }
