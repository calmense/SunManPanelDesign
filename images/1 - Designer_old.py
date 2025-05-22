from math import pi, sqrt, cos, sin
import streamlit as st
import plotly.graph_objects as go
from PIL import Image
from utils.utils import *
import streamlit as st

from fpdf import FPDF
import io
import base64
import tempfile
from ..utils.pdf_utils import generate_pdf_summary


# Set page configuration
st.set_page_config(page_title="Designer", layout="wide")

# color: rgb(230, 30, 40); /* Change the color as needed */

st.markdown(
    """
    <style>
    .subsubheader {
        font-size: 1em;
        font-weight: 300;
        margin-top: 1em;
        margin-bottom: 0.5em;
        font-family: 'Arial', sans-serif;
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

st.markdown('''
<style>
.katex-html {
    text-align: left;
}
</style>''',
unsafe_allow_html=True
)



# Eingangsparameter Netherlands
# Listen
countries = ["Germany", "Belgium", "Netherlands", "Poland", "Czech Republic", "Spain", "Italy"]
windZones = [["I", "II", "III", "IV"], ["23", "24", "25", "26"], ["I", "II", "III"], ["1", "2", "3"], ["I", "II", "III", "IV", "V"], ["A", "B", "C"], ["1-2", "3", "4-7", "8", "9"]]
imagesCountry = ["wind_zones_germany.png", "wind_zones_belgium.png", "wind_zones_netherlands.png", "wind_zones_poland.png", "wind_zones_czech.png", "wind_zones_spain.png", "wind_zones_italy.png"]
terrainCategories = ["0", "I", "II", "III", "IV"]
fundBasicWindVelocities = [[23, 25, 28, 30], [23, 24, 25, 26], [30, 27, 25], [22, 27, 25], [22.5, 25, 27.5, 30, 36], [26, 27, 29], [25, 27, 28, 30, 31]]
heightCategories = [[0.5, 0.65, 0.85, 0.8, 1.05, 0.95, 1.25, 1.4], [0.65, 0.8, 1.0, 0.95, 1.2, 1.15, 1.4, 'N/A'], [0.75, 0.9, 1.1, 1.1, 1.3, 1.3, 1.55, 'N/A']]

# Nested list containing all categories data
categories = [
    [1.80, 3.00, 3.35, 3.65, 3.80, 3.95, 4.10, 4.20, 4.30, 4.35, 4.40],  # Category 0
    [1.50, 2.80, 3.20, 3.45, 3.65, 3.80, 3.90, 4.05, 4.15, 4.20, 4.30],  # Category I
    [1.40, 2.30, 2.80, 3.10, 3.30, 3.50, 3.60, 3.70, 3.80, 3.90, 4.00],  # Category II
    [1.30, 2.00, 2.20, 2.50, 2.70, 2.90, 3.00, 3.15, 3.25, 3.35, 3.45],  # Category III
    [1.20, 1.20, 1.65, 1.95, 2.15, 2.35, 2.50, 2.60, 2.75, 2.85, 2.95]   # Category IV
]

# Heights corresponding to the values in categories
heights = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


def interpolate_value(z, category_index):
    """
    Simple linear interpolation to find the value at a specific height z, 
    within the given category, without using any external libraries.
    
    :param z: Target height (must be between 0 and 100)
    :param category_index: Index of the category (0 to 4)
    :return: Interpolated value at height z, rounded to the nearest ten
    """
    if not (0 <= z <= 100):
        raise ValueError("Height z must be between 0 and 100.")
    if not (0 <= category_index < len(categories)):
        raise ValueError("Invalid category index. Must be between 0 and 4.")

    # Get the category data
    category_values = categories[category_index]

    # Find the position in the heights array where z would fit
    for i in range(len(heights) - 1):
        if heights[i] <= z <= heights[i + 1]:
            # Heights and values at the interval endpoints
            x1, y1 = heights[i], category_values[i]
            x2, y2 = heights[i + 1], category_values[i + 1]
            
            # Linear interpolation formula: y = y1 + ((y2 - y1) / (x2 - x1)) * (z - x1)
            interpolated_value = y1 + ((y2 - y1) / (x2 - x1)) * (z - x1)
            return interpolated_value

    # If z exactly matches the last point
    if z == heights[-1]:
        return round(category_values[-1] / 10) * 10

    # If z is outside the interpolation bounds
    raise ValueError("Height z is out of the interpolation bounds.")

st.sidebar.header("Solar Panel Designer")
st.sidebar.markdown("NOTE: This web tool is intended solely for preliminary assessment as planning aids. The results must be verified by authorized personnel in the event of a project.")

# Render HTML to include Font Awesome icons
st.image("Sunman_logo.png", width = 300)
st.subheader("SunMan Solar Panels - Ultra-light, Glass-free Technology")
st.write('This web tool provides a structural framework for adhering solar panels directly onto roofs without the need for screws. \
         The panels are made from a durable, glass-free organic polymer composite that excels in various climatic conditions and extreme temperatures. \
         Please note that the tool does not assume responsibility for any errors, and users are advised to verify the results independently.')
st.write("")
st.write("")
st.write("")




# ==========================================================================


col1, col2 = st.columns([3,60])
with col1:
    st.image("icon1.png", width=40)
with col2:
    st.header("Pre-Assessment")


st.write("""
I confirm my understanding that the calculator is a preliminary design tool, and I have reviewed and completed the following design steps before proceeding to the next stage:

- Initial Evaluation
- Load Calculation
- Suitable Construction
- Glue Joint Resistance
- Checks on Roof Substrate
- Approval - Permission
- Construction
- Completion and Maintenance
""")



acknowledgement = st.checkbox(
    "In order to proceed to the design tool, please confirm."
)

if acknowledgement:


    # ==========================================================================



    st.write("")
    st.write("")
    st.write("")
    col1, col2 = st.columns([3,60])
    with col1:
        st.image("icon2.png", width=40)
    with col2:
        st.header("Load Calculation")

    st.write('The design wind loads depend on the project location, building dimensions, roof edge details, and panel positions.')
    st.write("")
    st.write("")

    with st.expander("Expand"):
        st.subheader("**Base Velocity Pressure**")
        st.markdown('<h3 class="subsubheader">Chose the country and the wind zone of your project site.</h3>', unsafe_allow_html=True)
        st.write("**Fundamental Basic Wind Velocity** represents the speed of wind at a standard height above ground level, unaffected by local topography or obstacles.")
        st.write("**Base Velocity Pressure** represents the base wind force, determined by the project's location and local exposure category.")
        st.latex("")
        st.latex("")

        col1, col2, col3, col4, col5, col6 = st.columns(6)
        with col1:
            country = st.selectbox('Country', countries)
            indexCountries = countries.index(country)

        with col2:
            windZone = st.selectbox('Wind Zone', windZones[indexCountries])
            indexWindZone = windZones[indexCountries].index(windZone)

        # calculation
        fundBasicWindVelocity = fundBasicWindVelocities[indexCountries][indexWindZone]
        baseVelocityPressure = round(fundBasicWindVelocity**2*1.25*0.5*0.001, 2)

        col1, col2, col3, col4, col5, col6 = st.columns(6)
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


        with col3:
            imageCountry = imagesCountry[indexCountries]
            st.image(imageCountry, width=500)

        st.write("")
        st.write("")
        st.write("")

        st.subheader("Gust Speed Pressure")
        st.markdown('<h3 class="subsubheader">The gust speed pressure is determined based on the terrain category and the building height.</h3>', unsafe_allow_html=True)
        st.write("The **Terrain Category** describes the surface roughness of the surrounding area 500m from the housing site.")
        st.write("**Gust Speed Pressure** refers to the dynamic pressure exerted on structures by the maximum instantaneous wind speed.")
        st.latex("")
        st.latex("")


        st.caption('EN 1991-1-4 Table 4.1')
        col1, col2, col3, col4, col5, col6 = st.columns(6)
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

        col1, col2, col3, col4, col5, col6 = st.columns(6)
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

        with col3:
            st.image("terrain_cat.png", width=450)

        st.write("")
        st.write("")
        st.write("")


        st.subheader("Additional Factor")
        st.write("For designing the adhesives, a partial safety factor **γ = 1.5** for wind is applied according to Eurocode EN 1990-1-1.")

        col1, col2, col3, col4, col5, col6 = st.columns(6)
        with col1:
            st.latex(r"\text{Partial safety factor }" + ' \gamma = 1.5')
            partialSafetyFactor = 1.5

        st.write("An additional factor is added for surface roughness due to wind flow around panels, undercurrents on rooftops and continuous behavior.")

        col1, col2, col3, col4, col5, col6 = st.columns(6)
        with col1:
            st.latex(r"\text{Additional factor }" + ' \chi = 1.2')
            additionalFactor = 1.2



        st.write("")
        st.write("")
        st.write("")


        st.subheader("Geometry")
        st.markdown('<h3 class="subsubheader">Due to the varying wind suction forces acting on the sealing surfaces, a flat roof is divided into the following areas.</h3>', unsafe_allow_html=True)
        st.caption("Wind Load – EN 1991-4 Ch. 7.2.3 – External Pressure Coefficients")

        col1, col2, col3, col4, col5, col6 = st.columns(6)

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


        st.subheader("Design Wind Load")
        st.markdown('<h3 class="subsubheader">The design wind load is determined for each roof area.</h3>', unsafe_allow_html=True)
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




    # ==========================================================================

    st.write("")
    st.write("")
    st.write("")
    col1, col2 = st.columns([3,60])
    with col1:
        st.image("images/icon4.png", width=40)
    with col2:
        st.header("Glue Joint Resistance")

    st.markdown('<h3 class="subsubheader">The glue joint resistance needs to be obtained and verified from a glue manufacturer according to European standards.</h3>', unsafe_allow_html=True)
    st.write("")
    st.write("")

    with st.expander("Expand"):

        st.subheader("Input Parameters")
        st.markdown('<h3 class="subsubheader">Chose between two panel sizes and chose a design glue joint resistance.</h3>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)
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


        colHeader = ["Wind Load [N/mm2]", "Glue Width [mm]", "Glue Width [mm]", "Utilization [%]", "Check"]
        colExpl = ["w_d", "req. glue per panel", "chosen glue width", "-", "-"]

        colF = [str(abs(wd[0])) , str(round(glueWidthReq[0])), str(int(glueWidthChos[0])), str(glueWidthUtil[0]) + "%", str(check[0])]
        colG = [str(abs(wd[1])) , str(round(glueWidthReq[1])), str(int(glueWidthChos[1])), str(glueWidthUtil[1]) + "%", str(check[0])]
        colH = [str(abs(wd[2])) , str(round(glueWidthReq[2])), str(int(glueWidthChos[2])), str(glueWidthUtil[2]) + "%", str(check[0])]


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

        # st.write(figBuilding)
        st.plotly_chart(figBuilding, key="fig_building_main2")



    # ==========================================================================

    st.write("")
    st.write("")
    st.write("")
    col1, col2 = st.columns([3,60])
    with col1:
        st.image("images/icon10.png", width=40)
    with col2:
        st.header("Summary Report")

    st.markdown('<h3 class="subsubheader">Summary of the calculation.</h3>', unsafe_allow_html=True)
    st.write("")
    st.write("")

    def create_download_link(val, filename):
        b64 = base64.b64encode(val).decode()  # Encode the PDF bytes as base64
        return f'<a href="data:application/octet-stream;base64,{b64}" download="{filename}.pdf">Download PDF</a>'

    with st.expander("Expand"):

        st.markdown('<h1 class="subsubheader">Preface</h1>', unsafe_allow_html=True)
        st.markdown('This web tool provides a structural framework for adhering solar panels directly onto roofs without the need for screws. \
                    The panels are made from a durable, glass-free organic polymer composite that excels in various climatic conditions and extreme temperatures. ')
        st.markdown('Please note that this tool does not assume responsibility for any errors, and users are advised to independently verify the results. \
                    It is intended solely for preliminary assessments as a planning aid, and the results must be confirmed by authorized personnel for project purposes', unsafe_allow_html=True)
        
        st.markdown('For more information, please visit: [https://de.sunman-energy.com/](https://de.sunman-energy.com/)')


        col1, col2, col3, col4 = st.columns(4)
        with col1:

            st.markdown('<h1 class="subsubheader">Wind Loading</h1>', unsafe_allow_html=True)
            st.caption("DIN EN 1991-1-4")

            st.write('Country: ' + str(country) + '; Wind Zone: ' + str(windZone))
            st.write('Terrain Category: ' + str(terrainCategory))
            st.write('Building Height: ' + str(buildingHeight) + ' m')
            st.write('Building Length: ' + str(buildingLength) + ' m')
            st.write('Building Width: ' + str(buildingWidth) + ' m')
            st.write("")
            st.markdown('Fund. Basic Wind Velocity v<sub>b0</sub> = ' + str(fundBasicWindVelocity) + ' m/s', unsafe_allow_html=True)
            st.markdown('Base Velocity Pressure q<sub>b0</sub> = ' + str(baseVelocityPressure) + ' kN/m<sup>2</sup>', unsafe_allow_html=True)
            st.markdown('Gust Speed Pressure q<sub>p</sub>(z) = ' + str(gustSpeedPressure) + 'N/mm<sup>2</sup>', unsafe_allow_html=True)

        with col2:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.image(imagesCountry[indexCountries], width=450)
        
        st.write("")    
        st.write("")
        st.markdown('<b>Design Wind Load</b>', unsafe_allow_html=True)


        figTable.update_layout(
            width=800,  # Half the original width, adjust as needed
            height=200,  # Half the original height, adjust as needed
            margin=dict(l=0, r=0, t=0, b=0)  # Minimized margins
        )
        st.plotly_chart(figTable)

        st.markdown('<b>Roof Areas</b>', unsafe_allow_html=True)     
        figBuilding.update_layout(
            width=600,  # Half the original width, adjust as needed
            height=400,  # Half the original height, adjust as needed
            margin=dict(l=0, r=0, t=0, b=0)  # Minimized margins
        )
        st.plotly_chart(figBuilding, key="fig_building_main")


        st.markdown('<h1 class="subsubheader">Glue Joint Resistance</h1>', unsafe_allow_html=True)
        st.markdown('<b>Note</b>: Testing is generally required by all manufacturers to verify there is sufficient bond between the adhesive and the roof surface.',unsafe_allow_html=True)
        st.write("") 


        
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:

            st.markdown('Panel Size: <b>' + str(panelSize) + '</b>',unsafe_allow_html=True)
            st.markdown('Panel Width B = ' + str(width) + ' mm', unsafe_allow_html=True)
            st.markdown('Panel Length L = ' + str(height) + ' m', unsafe_allow_html=True)
            st.markdown('Panel Area A = ' + str(round(area * 0.001**2,2)) + ' m<sup>2</sup>', unsafe_allow_html=True)

            st.markdown('Gluing Distance a = ' + str(int(gluingDistance)) + ' mm', unsafe_allow_html=True)
            st.write("")

            st.markdown('Glue Manufacturer: <b>' + str(designGlueJointResistance) + '</b>', unsafe_allow_html=True)
            st.markdown('Design Glue Joint Resistance Rd = ' + str(designGlueJointResistanceValue) + ' N/mm<sup>2</sup>', unsafe_allow_html=True)


        with col2:
            figPanel.update_layout(
                width=700,  # Half the original width, adjust as needed
                height=350,  # Half the original height, adjust as needed
                margin=dict(l=0, r=0, t=0, b=0)  # Minimized margins
            )
            st.write(figPanel)

        st.write("")    
        st.write("")
        st.markdown('Gluing Design Table', unsafe_allow_html=True)
        figCheck.update_layout(
            width=800,  # Half the original width, adjust as needed
            height=250,  # Half the original height, adjust as needed
            margin=dict(l=0, r=0, t=0, b=0)  # Minimized margins
        )
        st.write(figCheck)


    with st.expander("📄 Generate PDF Summary"):
        if st.button("Create PDF"):


            pdf_bytes = generate_pdf_summary(
                country, windZone, fundBasicWindVelocity, baseVelocityPressure,
                terrainCategory, buildingHeight, gustSpeedPressure,
                buildingLength, buildingWidth,
                panelSize, width, height, area, gluingDistance,
                designGlueJointResistance, designGlueJointResistanceValue,
                glueWidthReq, glueWidthChos, glueWidthUtil,
                logo_path="Sunman_logo.png",
                country_path=imageCountry
            )

            st.download_button(
                label="📥 Download Summary PDF",
                data=pdf_bytes,
                file_name="summary_report.pdf",
                mime="application/pdf"
            )
