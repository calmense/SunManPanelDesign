import streamlit as st



# Set page configuration
st.set_page_config(page_title="Initial Evaluation", layout="wide")



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



# Render HTML to include Font Awesome icons
st.image("Sunman_logo.png", width = 300)
st.subheader("SunMan Solar Panels - Ultra-light, Glass-free Technology")
st.write('This web tool provides a structural framework for adhering solar panels directly onto roofs without the need for screws. \
         The panels are made from a durable, glass-free organic polymer composite that excels in various climatic conditions and extreme temperatures. \
         Please note that the tool does not assume responsibility for any errors, and users are advised to verify the results independently.')
st.write("")
st.write("")
st.write("")

col1, col2 = st.columns([3,60])
with col1:
    st.image("icon1.png", width=60)
with col2:
    st.header("Initial Evaluation / Due Dilligance")

st.markdown('<h3 class="subsubheader">To determine if panels can be installed on existing buildings, check whether these initial criteria are met.</h3>', unsafe_allow_html=True)
st.write("")
st.write("")

st.markdown('<h3 class="text"> Does your roof fit within the parameters: less than 25 meters and a slope of less than 5 degrees? Roofs beyond these limits are still feasible, but they are not directly covered in this document and require a bespoke wind calculation.</h3>', unsafe_allow_html=True)
st.markdown('<h3 class="text"> Checking the roof structure: Is the minimal additional weight likely to cause any issues? Refer to a structural engineer if uncertain.</h3>', unsafe_allow_html=True)
st.markdown('<h3 class="text"> Checking the roof surface membrane:</h3>', unsafe_allow_html=True)
st.markdown("   - Is the material/substructure suitable?")
st.markdown("   - What is the age and condition – any corrosion or peeling?")
st.markdown("   - Is cleaning or repair of the surface necessary?")