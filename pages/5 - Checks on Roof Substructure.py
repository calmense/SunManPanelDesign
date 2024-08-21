import streamlit as st



# Set page configuration
st.set_page_config(page_title="Checks on Roof Substructure", layout="wide")



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
    st.header("Checks on Roof Substructure")
st.markdown('<h3 class="subsubheader">Adhesive Application and Structural Assessment Requirements</h3>', unsafe_allow_html=True)
st.write("")
st.write("")


st.markdown('<h3 class="text"> - An adhesion test is typically required up to this point.</h3>', unsafe_allow_html=True)
st.markdown('<h3 class="text"> - Detailed calculations should be performed based on this design guide if applicable or separate load calculation if outside the parameters.</h3>', unsafe_allow_html=True)
st.markdown('<h3 class="text"> - Verification of the roof substrate or substructure is necessary to assess tying down forces.</h3>', unsafe_allow_html=True)
st.markdown('<h3 class="text"> - Determine the exact layout and width of the glue lines for the chosen product.</h3>', unsafe_allow_html=True)
st.markdown('<h3 class="text"> - Identify the surface preparation required, including cleaning, priming, etc.</h3>', unsafe_allow_html=True)
