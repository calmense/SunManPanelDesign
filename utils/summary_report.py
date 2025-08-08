import streamlit as st
import plotly.graph_objects as go
from utils.pdf_utils import generate_pdf_summary

def summary_report_section(load_results, glue_results, quantities_results):

    figBuilding = load_results["figBuilding"]
    figTable = load_results["figTable"]
    figCheck = glue_results["figCheck"]
    figPanel = glue_results["figPanel"]

    numberTubes = quantities_results["numberTubes"]
    numberTubesFact = quantities_results["numberTubesFact"]
    
    st.write("")
    st.write("")
    st.write("")
    col1, col2 = st.columns([1,22])
    with col1:
        st.image("images/icon1.png", width=50)
    with col2:
        st.subheader("Summary Report")
    st.write('Summary of the calculation.')

    with st.expander("Expand"):
        if st.button("Create PDF"):

            # 📦 Variablen extrahieren
            country = load_results["country"]
            windZone = load_results["windZone"]
            fundBasicWindVelocity = load_results["fundBasicWindVelocity"]
            baseVelocityPressure = load_results["baseVelocityPressure"]
            terrainCategory = load_results["terrainCategory"]
            buildingHeight = load_results["buildingHeight"]
            gustSpeedPressure = load_results["gustSpeedPressure"]
            buildingLength = load_results["buildingLength"]
            buildingWidth = load_results["buildingWidth"]
            imageCountry = load_results["imageCountry"]

            panelSize = glue_results["panelSize"]
            width = glue_results["width"]
            height = glue_results["height"]
            area = glue_results["area"]
            glueManufacturerSelected = glue_results["glueManufacturerSelected"]
            glueSelected = glue_results["glueSelected"]
            glueValue = glue_results["glueValue"]
            designGlueJointResistanceValue = glue_results["designGlueJointResistanceValue"]
            glueWidthReq = glue_results["glueWidthReq"]
            glueWidthFinal = glue_results["glueWidthFinal"]
            gluingDistance = glue_results["gluingDistance"]
            minThickness = glue_results["minThickness"]

            figBuilding = load_results["figBuilding"]

            # 📄 PDF erzeugen
            pdf_bytes = generate_pdf_summary(
                country, windZone, fundBasicWindVelocity, baseVelocityPressure,
                terrainCategory, buildingHeight, gustSpeedPressure,
                buildingLength, buildingWidth,
                panelSize, width, height, area, gluingDistance,
                glueManufacturerSelected, glueSelected, glueValue, designGlueJointResistanceValue,
                glueWidthReq, glueWidthFinal, minThickness,
                figBuilding, figTable, figPanel, figCheck, numberTubes, numberTubesFact,
                logo_path="./images/Sunman_logo.png", country_path=imageCountry,
                
            )

            # ⬇️ Download-Button
            st.download_button(
                label="Download PDF",
                data=pdf_bytes,
                file_name="SunMan-Summary-Report.pdf",
                mime="application/pdf"
            )
