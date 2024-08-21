import streamlit as st



# Set page configuration
st.set_page_config(page_title="Approval / Permission", layout="wide")



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
    st.image("icon6.png", width=60)
with col2:
    st.header("Approval / Permission")
st.markdown('<h3 class="subsubheader">Local building regulations</h3>', unsafe_allow_html=True)
st.write("")
st.write("")


st.markdown('<h3 class="text">It is the responsibility of the building owner or project developer to ensure compliance with the necessary planning requirements and to determine if planning permission is required.</h3>', unsafe_allow_html=True)
st.markdown('<h3 class="text">Additional certified testing of adhesives or the system may be necessary as part of project-based construction approval or by local building authorities. The following information is typically required.</h3>', unsafe_allow_html=True)
st.markdown("   - Structural Calculations – PV, Subframe and Adhesives ")
st.markdown("   - Structural Verification – existing roof structure")
st.markdown("   - Certified testing data")
