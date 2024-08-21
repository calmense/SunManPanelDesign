import streamlit as st



# Set page configuration
st.set_page_config(page_title="Completion and Maintainance", layout="wide")



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
    st.image("icon9.png", width=60)
with col2:
    st.header("Completion and Maintainance")
st.markdown('<h3 class="subsubheader">Establishing Maintenance and Inspection Guidelines</h3>', unsafe_allow_html=True)
st.write("")
st.write("")


st.markdown('<h3 class="text"> - The operator must create detailed operating instructions.</h3>', unsafe_allow_html=True)
st.markdown('<h3 class="text"> - Regular tasks should include cleaning and inspecting contact surfaces for any unwanted deformations, as well as checking the adhesive surfaces.</h3>', unsafe_allow_html=True)
st.markdown('<h3 class="text"> - The inspection intervals should be determined. Typically, annual visual inspections are recommended.</h3>', unsafe_allow_html=True)
st.markdown('<h3 class="text"> - An independent inspection by a specialized company should occur at extended intervals, potentially every five years and possibly including an adhesion test.</h3>', unsafe_allow_html=True)

