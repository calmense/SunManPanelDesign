import streamlit as st
import plotly.graph_objects as go
from PIL import Image
from utils.utils import interpolate_value, draw_arrow, add_text

# Listen
countries = ["Germany", "Belgium", "Netherlands", "Poland", "Czech Republic", "Spain", "Italy"]
windZones = [["I", "II", "III", "IV"], ["23", "24", "25", "26"], ["I", "II", "III"], ["1", "2", "3"], ["I", "II", "III", "IV", "V"], ["A", "B", "C"], ["1-2", "3", "4-7", "8", "9"]]
imagesCountry = ["images/wind_zones_germany.png", "images/wind_zones_belgium.png", "images/wind_zones_netherlands.png", "images/wind_zones_poland.png", "images/wind_zones_czech.png", "images/wind_zones_spain.png", "images/wind_zones_italy.png"]
terrainCategories = ["0", "I", "II", "III", "IV"]
fundBasicWindVelocities = [[23, 25, 28, 30], [23, 24, 25, 26], [30, 27, 25], [22, 27, 25], [22.5, 25, 27.5, 30, 36], [26, 27, 29], [25, 27, 28, 30, 31]]
heightCategories = [[0.5, 0.65, 0.85, 0.8, 1.05, 0.95, 1.25, 1.4], [0.65, 0.8, 1.0, 0.95, 1.2, 1.15, 1.4, 'N/A'], [0.75, 0.9, 1.1, 1.1, 1.3, 1.3, 1.55, 'N/A']]

def load_calculation_section(countries, windZones, imagesCountry,
                              terrainCategories, fundBasicWindVelocities,
                              categories, heights):
    st.write("")
    st.write("")
    st.write("")
    col1, col2 = st.columns([1,22])
    with col1:
        st.image("images/icon2.png", width=50)
    with col2:
        st.subheader("Load Calculation")

    st.write('The design wind loads depend on the project location, building dimensions, roof edge details, and panel positions.')
    st.write("")
    st.write("")

    with st.expander("Expand"):
        st.markdown("#### **Base Velocity Pressure**")
        st.write('Chose the country and the wind zone of your project site.')
        st.markdown("""
        The **Fundamental Basic Wind Velocity** represents the speed of wind at a standard height above ground level, unaffected by local topography or obstacles. The **Base Velocity Pressure** represents the base wind force, determined by the project's location and local exposure category.
        """)
        st.latex("")
        st.latex("")

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            country = st.selectbox('Country', countries)
            indexCountries = countries.index(country)

        with col2:
            windZone = st.selectbox('Wind Zone', windZones[indexCountries])
            indexWindZone = windZones[indexCountries].index(windZone)

        # calculation
        fundBasicWindVelocity = fundBasicWindVelocities[indexCountries][indexWindZone]
        baseVelocityPressure = round(fundBasicWindVelocity**2*1.25*0.5*0.001, 2)

        col1, col2 = st.columns(2)
        with col1:
            st.latex("")
            st.latex("")
            st.latex("")
            st.latex("")
            st.latex("")
            st.caption('EN 1991-1-4 Equation 4.1')
            st.latex(r"\text{Fund. Basic Wind Velocity }" + ' v_{b0} = ' + str(fundBasicWindVelocity) + ' m/s')
            st.latex("")
            st.caption('EN 1991-1-4 Equation 4.10')
            st.latex(r"\text{Base Velocity Pressure }" + ' q_{b0} = ' + str(baseVelocityPressure) + ' kN/m^2')


        with col2:
            imageCountry = imagesCountry[indexCountries]
            st.image(imageCountry)

        st.write("")
        st.write("")
        st.write("")

        st.markdown("#### Gust Speed Pressure")
        st.write('The gust speed pressure is determined based on the terrain category and the building height.')
        st.write("The **Terrain Category** describes the surface roughness of the surrounding area 500m from the housing site.")
        st.write("**Gust Speed Pressure** refers to the dynamic pressure exerted on structures by the maximum instantaneous wind speed.")
        st.latex("")
        st.latex("")


        st.caption('EN 1991-1-4 Table 4.1')
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            terrainCategory = st.selectbox('Terrain Category', ["0", "I", "II", "III", "IV"])
            indexTerrainCategory = terrainCategories.index(terrainCategory)

        with col2:
            buildingHeight = int(st.text_input('Building Height [m]', 10))

        if buildingHeight >= 100:
            buildingHeight = 100
            st.write("The building height has to be smaller than 100m.")


        # calculation
        terrainFactor = round(interpolate_value(buildingHeight, indexTerrainCategory), 2)
        gustSpeedPressure = round(terrainFactor * baseVelocityPressure, 2)

        col1, col2 = st.columns(2)
        with col1:
            st.latex("")
            st.latex("")
            st.latex("")
            st.latex("")
            st.caption('EN 1991-1-4 Image 4.2')
            st.latex(r"\text{Terrain Factor }" + ' z_e(z) = ' + str(terrainFactor))
            st.latex("")
            st.caption('EN 1991-4 Equation 4.8')
            st.latex(r"\text{Gust Speed Pressure }" + ' q_{p}(z) = ' + str(gustSpeedPressure) + 'N/mm^2')

        with col2:
            st.image("images/terrain_cat.png", width=450)

        st.write("")
        st.write("")
        st.write("")


        st.markdown("#### Additional Factor")
        st.write("For designing the adhesives, a partial safety factor **γ = 1.5** for wind is applied according to Eurocode EN 1990-1-1.")

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.latex(r"\text{Partial safety factor } \gamma = 1.5")
            partialSafetyFactor = 1.5

        st.write("An additional factor is added for surface roughness due to wind flow around panels, undercurrents on rooftops and continuous behavior.")

        col1, col2 = st.columns(2)
        with col1:
            st.latex(r"\text{Additional factor } \chi = 1.2")
            additionalFactor = 1.2



        st.write("")
        st.write("")
        st.write("")


        st.markdown("#### Geometry")
        st.write('Due to the varying wind suction forces acting on the sealing surfaces, a flat roof is divided into the following areas.')
        st.caption("Wind Load – EN 1991-4 Ch. 7.2.3 – External Pressure Coefficients")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            buildingLength = int(st.text_input('Building Length [m]', 50))

        with col2:
            buildingWidth = int(st.text_input('Building Width [m]', 20))


        gapx = 20
        gapy = 20

        figBuilding = go.Figure(go.Scatter(x=[gapx + 0,gapx + buildingLength, gapx + buildingLength,gapx + 0, gapx + 0], 
                                y=[0 + gapy,0 + gapy, buildingWidth + gapy, buildingWidth + gapy, 0 + gapy], 
                                line=dict(color='darkgrey'),
                                mode="lines",
                                fillcolor='lightgrey',  
                                fill="toself",
                                opacity=0.7))

        e1 = min(2*buildingHeight, buildingLength)
        e2 = min(2*buildingHeight, buildingWidth)
        e_10_1 = e1/10
        e_10_2 = e2/10
        e_4_1 = e1/4    
        e_4_2 = e2/4

        figBuilding.update_layout(
                shapes=[
                    dict( type="rect", x0=gapx, y0=gapy, x1=gapx+e_4_1, y1=gapy+e_10_1, line=dict( color="red", width=0), fillcolor="red", opacity=1),
                    dict( type="rect", x0=gapx+buildingLength-e_4_1, y0=gapy, x1=gapx+buildingLength, y1=gapy+e_10_1, line=dict( color="red", width=0), fillcolor="red", opacity=1),
                    dict( type="rect", x0=gapx, y0=gapy+buildingWidth-e_10_1, x1=gapx+e_4_1, y1=gapy+buildingWidth, line=dict( color="red", width=0), fillcolor="red", opacity=1),
                    dict( type="rect", x0=gapx+buildingLength-e_4_1, y0=gapy+buildingWidth-e_10_1, x1=gapx+buildingLength, y1=gapy+buildingWidth, line=dict( color="red", width=0), fillcolor="red", opacity=1),

                    dict( type="rect", x0=gapx, y0=gapy, x1=gapx+e_10_2, y1=gapy+e_4_2, line=dict( color="red", width=0), fillcolor="red", opacity=1),
                    dict( type="rect", x0=gapx+buildingLength-e_10_2, y0=gapy, x1=gapx+buildingLength, y1=gapy+e_4_2, line=dict( color="red", width=0), fillcolor="red", opacity=1),
                    dict( type="rect", x0=gapx, y0=gapy+buildingWidth-e_4_2, x1=gapx+e_10_2, y1=gapy+buildingWidth, line=dict( color="red", width=0), fillcolor="red", opacity=1),
                    dict( type="rect", x0=gapx+buildingLength-e_10_2, y0=gapy+buildingWidth-e_4_2, x1=gapx+buildingLength, y1=gapy+buildingWidth, line=dict( color="red", width=0), fillcolor="red", opacity=1),

                    dict( type="rect", x0=gapx+e_4_1, y0=gapy, x1=gapx+buildingLength-e_4_1, y1=gapy+e_10_1, line=dict( color="black", width=0), fillcolor="black", opacity=0.3),
                    dict( type="rect", x0=gapx+e_4_1, y0=gapy+buildingWidth-e_10_1, x1=gapx+buildingLength-e_4_1, y1=gapy+buildingWidth, line=dict( color="black", width=0), fillcolor="black", opacity=0.3),
                    dict( type="rect", x0=gapx, y0=gapy+e_4_2, x1=gapx+e_10_2, y1=gapy+buildingWidth-e_4_2, line=dict( color="black", width=0), fillcolor="black", opacity=0.3),
                    dict( type="rect", x0=gapx+buildingLength-e_10_2, y0=gapy+e_4_2, x1=gapx+buildingLength, y1=gapy+buildingWidth-e_4_2, line=dict( color="black", width=0), fillcolor="black", opacity=0.3),
                ]
            )

        # scale
        scaleX = buildingLength / 50
        scaleY = buildingWidth / 20
        factor = 7

        # dimension width
        xList = [gapx-10*scaleX, gapx-10*scaleX]
        yList = [gapy, gapy+buildingWidth]
        draw_arrow(figBuilding, xList, yList, "Y", scaleX/factor, scaleY/factor)

        xList = [gapx, gapx+buildingLength]
        yList = [gapy+buildingWidth+10*scaleY, gapy+buildingWidth+10*scaleY]
        draw_arrow(figBuilding, xList, yList, "X", scaleX/factor, scaleY/factor)

        xList = [gapx-5*scaleX, gapx-5*scaleX]
        yList = [gapy+buildingWidth-e_4_2, gapy+buildingWidth]
        draw_arrow(figBuilding, xList, yList, "Y", scaleX/factor, scaleY/factor)

        xList = [gapx, gapx+e_4_1]
        yList = [gapy+buildingWidth+5*scaleY, gapy+buildingWidth+5*scaleY]
        draw_arrow(figBuilding, xList, yList, "X", scaleX/factor, scaleY/factor)

        xList = [gapx, gapx+e_10_2]
        yList = [gapy-5*scaleY, gapy-5*scaleY]
        draw_arrow(figBuilding, xList, yList, "X", scaleX/factor, scaleY/factor)

        xList = [gapx-5*scaleX, gapx-5*scaleX]
        yList = [gapy, gapy+e_10_1]
        draw_arrow(figBuilding, xList, yList, "Y", scaleX/factor, scaleY/factor)

        # text
        x = gapx-10*scaleX
        y = gapy+buildingWidth/2
        add_text(figBuilding, buildingWidth, x , y, 15)

        x = gapx+buildingLength/2
        y = gapy+buildingWidth+9*scaleY
        add_text(figBuilding, buildingLength, x , y, 15)

        x = gapx-4*scaleX
        y = gapy+e_10_1/2
        add_text(figBuilding, e_10_1, x , y, 15)

        x = gapx-4*scaleX
        y = gapy+buildingWidth-e_4_2/2
        add_text(figBuilding, e_4_2, x , y, 15)

        x = gapx+e_10_2+1*scaleX
        y = gapy-5*scaleY
        add_text(figBuilding, e_10_2, x , y, 15)

        x = gapx+e_4_1+1*scaleX
        y = gapy+buildingWidth+5*scaleY
        add_text(figBuilding, e_4_1, x , y, 15)


        x = gapx+buildingLength/2-2*scaleX
        y = gapy+e_10_1/2
        add_text(figBuilding, "Area G", x , y, 15)

        x = gapx+buildingLength/2-2*scaleX
        y = gapy+buildingWidth/2
        add_text(figBuilding, "Area H", x , y, 15)

        x = gapx+buildingLength+1*scaleX
        y = gapy+e_10_1/2
        add_text(figBuilding, "Area F", x , y, 15)

        figBuilding.update_layout(
            autosize=False,
            width=600,
            height=400,
            uirevision='static',
            xaxis=dict(scaleanchor="y", scaleratio=1, fixedrange=False, visible=False),
            yaxis=dict(scaleanchor="x", scaleratio=1, fixedrange=False, visible=False),
            showlegend=False,
            margin=dict(l=0, r=0, t=0, b=0),  # Minimize the margins
            paper_bgcolor='rgba(0,0,0,0)',  # Transparent background if needed
            plot_bgcolor='rgba(0,0,0,0)'    # Transparent plot background
        )

        # Hide the axis
        figBuilding.update_xaxes(showline=False, showgrid=False, zeroline=True)
        figBuilding.update_yaxes(showline=False, showgrid=False, zeroline=True)

        # st.write(figBuilding)
        st.plotly_chart(figBuilding, key="fig_building_main1")

        st.markdown("#### Design Wind Load")
        st.write('The design wind load is determined for each roof area.')
        st.caption("DIN EN 1991-1-4 Chapter 7.2.3 ")

        # Define the headers and the cells of the table
        headers = ['F', 'G', 'H']
        coefficients = [-2.50, -2.00, -1.20]

        # Calculate wk and wd based on coefficients
        wk = [round(gustSpeedPressure * x * additionalFactor, 2) for x in coefficients]
        wd = [round(x * partialSafetyFactor, 2) for x in wk]
        colHeader = ["coefficients", "w<sub>k</sub> [kN/m<sup>2</sup>]", "w<sub>d</sub> [kN/m<sup>2</sup>]"]
        colExpl = ["-", "char. wind load", "design wind load"]
        colF = [coefficients[0], wk[0], wd[0]]
        colG = [coefficients[1], wk[1], wd[1]]
        colH = [coefficients[2], wk[2], wd[2]]

        columns = ['Roof area', 'Explanation'] + headers
        cell_text = [colExpl, colF, colG, colH]

        # Create the table
        figTable = go.Figure(data=[go.Table(
            header=dict(values = columns,  # Empty string for the first header cell
                        fill_color='white',
                        height=35,
                        font=dict(color='red', size=16, family="Times New Roman"),
                        line=dict(color='darkslategray', width=2),
                        align='center'),
            cells=dict(values=[colHeader, colExpl, colF, colG, colH],              
                    fill_color=['white', 'white', 'white'],  # Alternating row colors
                    height=35,
                    font=dict(color=['red', 'grey', 'black', 'black'], size=16, family="Times New Roman"),
                    line=dict(color='darkslategray', width=2),
                    align='center'))
        ])

        # Set table layout
        figTable.update_layout(
            width=900,
            height=200,
            margin=dict(l=0, r=0, t=0, b=0),  # Minimize the margins as much as possible
            paper_bgcolor='rgba(0,0,0,0)',  # Transparent paper background (optional)
            plot_bgcolor='rgba(0,0,0,0)'    # Transparent plot background (optional)
        )

        st.plotly_chart(figTable)

        # Return all needed values
        return {
            "country": country,
            "windZone": windZone,
            "fundBasicWindVelocity": fundBasicWindVelocity,
            "baseVelocityPressure": baseVelocityPressure,
            "terrainCategory": terrainCategory,
            "buildingHeight": buildingHeight,
            "gustSpeedPressure": gustSpeedPressure,
            "buildingLength": buildingLength,
            "buildingWidth": buildingWidth,
            "figBuilding": figBuilding,
            "figTable": figTable,
            "wd": wd,
            "coefficients": coefficients,
            "imageCountry": imageCountry
        }
