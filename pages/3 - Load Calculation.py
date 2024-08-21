import streamlit as st



# Set page configuration
st.set_page_config(page_title="Load Calculation", layout="wide")



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
    st.image("icon2.png", width=60)
with col2:
    st.header("Load Calculation")
st.markdown('<h3 class="subsubheader">To determine if panels can be installed on existing buildings, consider these key loads and parameters.</h3>', unsafe_allow_html=True)
st.write("")
st.write("")


st.markdown('<h3 class="text"> - The lightweight panels, with a self-weight of less than 3.0 kg/m2, typically do not pose structural issues since their load is minimal compared to the roofs weight and other loads such as snow.</h3>', unsafe_allow_html=True)
st.markdown('<h3 class="text"> - Wind suction is usually the key factor in deciding suitable buildings for panel installation and the amount of adhesive needed to secure the panels.</h3>', unsafe_allow_html=True)
st.markdown('<h3 class="text"> - To ensure structural safety in accordance with Eurocode the design action Ed must not exceed the design resistance 𝐸𝑑≤𝑅𝑑</h3>', unsafe_allow_html=True)
