from utils.wind_load_calc import *
from utils.glue_resistance_calc import glue_resistance_section
from utils.summary_report import summary_report_section
from utils.quantities import quantities

import streamlit as st
import plotly.graph_objects as go
from utils.utils import *

# Set page configuration
st.set_page_config(page_title="Designer", layout="wide")

st.markdown('''
<style>
.katex-html {
    text-align: left;
}
</style>''',
unsafe_allow_html=True
)

st.sidebar.header("Solar Panel Designer")
st.sidebar.markdown("NOTE: This web tool is intended solely for preliminary assessment as planning aids. The results must be verified by authorized personnel in the event of a project.")

# Render HTML to include Font Awesome icons
st.image("images/Sunman_logo.png", width = 300)
st.subheader("SunMan Solar Panels - Ultra-light, Glass-free Technology")
st.write('This web tool provides a structural framework for adhering solar panels directly onto roofs without the need for screws. \
         The panels are made from a durable, glass-free organic polymer composite that excels in various climatic conditions and extreme temperatures. \
         Please note that the tool does not assume responsibility for any errors, and users are advised to verify the results independently.')
st.write("")

# ==========================================================================

col1, col2 = st.columns([1,22])
with col1:
    st.image("images/icon1.png")
with col2:
    st.subheader("Pre-Assessment")


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
    load_results = load_calculation_section(countries, windZones, imagesCountry,
                              terrainCategories, fundBasicWindVelocities,
                              categories, heights)
    glue_results = glue_resistance_section(load_results["wd"], load_results["figTable"])
    
    quantities_results = quantities(glue_results["glueLength"], glue_results["glueLength"],  glue_results["glueWidthFinal"], glue_results["minThickness"])

    # Figures are part of your workflow
    summary_report_section(
        load_results, 
        glue_results,
        quantities_results
    )
