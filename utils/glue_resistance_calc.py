import streamlit as st
import plotly.graph_objects as go
from PIL import Image

def glue_resistance_section(wd, figBuilding):
    
    st.write("")
    st.write("")
    st.write("")
    col1, col2 = st.columns([1,22])
    with col1:
        st.image("images/icon4.png")
    with col2:
        st.subheader("Glue Joint Resistance")

    st.write('The glue joint resistance needs to be obtained and verified from a glue manufacturer according to European standards.')
    st.write("")
    st.write("")

    with st.expander("Expand"):

        st.subheader("Input Parameters")
        st.markdown('<h3 class="subsubheader">Chose between two panel sizes and chose a design glue joint resistance.</h3>', unsafe_allow_html=True)

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            panelSize = st.selectbox('Panel Size', ["SMF430", "SMF520"])
        with col2:
            designGlueJointResistance = st.selectbox('Glue Manufacturer', ["Dowsil 895", "Sika SG-20"])

        st.write("")
        st.markdown('Both glues are ETAG approved, so the design strength R<sub>d</sub> is specified in the datasheet, eliminating the need for further reduction factors.', unsafe_allow_html=True)
        
        designGlueJointResistanceValue = 0.14 if designGlueJointResistance == "Dowsil 895" else 0.17
                                                  
        gapx = 0
        gapy = 0

        # solar panel
        if panelSize == "SMF430":
            width = 1080
            height = 2054
            area = width * height
            
        else:
            width = 1197
            height = 2246
            area = width * height

        if panelSize == "SMF430":
            gluingDistance = (height - 100) / 4
            linesXCoords = [[gapx, width + gapx], [gapx, width + gapx], [gapx, width + gapx], [gapx, width + gapx], [gapx, width + gapx]]
            linesYCoords = [[gapy + 50, gapy + 50], [gapy + 50 + gluingDistance, gapy + 50 + gluingDistance], [gapy + 50 + gluingDistance*2, gapy + 50 + gluingDistance*2], [gapy + 50 + gluingDistance*3, gapy + 50 + gluingDistance*3], [gapy + 50 + gluingDistance*4, gapy + 50 + gluingDistance*4]]
        else:
            gluingDistance = (height - 100) / 5
            linesXCoords = [[gapx, width + gapx], [gapx, width + gapx], [gapx, width + gapx], [gapx, width + gapx], [gapx, width + gapx], [gapx, width + gapx]]
            linesYCoords = [[gapy + 50, gapy + 50], [gapy + 50 + gluingDistance, gapy + 50 + gluingDistance], [gapy + 50 + gluingDistance*2, gapy + 50 + gluingDistance*2], [gapy + 50 + gluingDistance*3, gapy + 50 + gluingDistance*3], [gapy + 50 + gluingDistance*4, gapy + 50 + gluingDistance*4], [gapy + 50 + gluingDistance*5, gapy + 50 + gluingDistance*5]]


        scaleY = height / 400
        scaleX = 400 / height

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

        # Hide the axis
        figPanel.update_xaxes(showline=False, showgrid=False, zeroline=False)
        figPanel.update_yaxes(showline=False, showgrid=False, zeroline=False)

        col1, col2 = st.columns(2)
        with col1:
            st.write("")
            st.subheader("SunMan Solar Panel")
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

            st.subheader("Solar Panel")
            st.latex(r"\text{Width }" + ' B = ' + str(width) + ' mm')
            st.latex(r"\text{Length }" + ' L = ' + str(height) + ' mm')
            st.latex(r"\text{Area }" + ' A = ' + str(round(area * 0.001**2,1)) + ' m^2')
            st.latex(r"\text{Gluing Distance }" + ' a = ' + str(int(gluingDistance)) + ' mm')
            st.latex(r"\text{Design Glue Joint Resistance }" + ' R_d = ' + str(designGlueJointResistanceValue) + ' N/mm^2')
            st.write("")
            st.write("")
            
        st.subheader("Gluing Design Table")
        st.markdown('<h3 class="subsubheader">This table shows the required glue width.</h3>', unsafe_allow_html=True)

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            utilTarget = 0.9
            st.latex(r"\text{Utilization Target} = " + str(int(utilTarget*100)) + r"\, \%")
            st.latex(r"\text{Gluing Width }" + 'b = ' + str(10) + ' mm')

        # Define the headers and the cells of the table
        headers = ['F', 'G', 'H']

        # Calculate wk and wd based on coefficients
        glueWidthReq = [round( abs(wdi) * (gluingDistance / 1000)/ (designGlueJointResistanceValue / utilTarget), 0) for wdi in wd]
        glueWidthChos = [round( x+5, -1) for x in glueWidthReq]
        glueWidthUtil = [int( 100 *glueWidthReq[i] * utilTarget / (glueWidthChos[i])) for i in range(len(glueWidthChos))]
        check = ["✅" if x < 100 else "❌" for x in glueWidthUtil]

        colHeader = ["Wind Load [N/mm2]", "Glue Width [mm]"]
        colExpl = ["w_d", "req. glue per panel"]

        colF = [str(abs(wd[0])) , str(round(glueWidthReq[0]))]
        colG = [str(abs(wd[1])) , str(round(glueWidthReq[1]))]
        colH = [str(abs(wd[2])) , str(round(glueWidthReq[2]))]

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
            "designGlueJointResistance": designGlueJointResistance,
            "designGlueJointResistanceValue": designGlueJointResistanceValue,
            "figPanel": figPanel,
            "figCheck": figCheck,
            "glueWidthReq": glueWidthReq,
            "glueWidthChos": glueWidthChos,
            "glueWidthUtil": glueWidthUtil,
        }
