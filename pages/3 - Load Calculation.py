import streamlit as st

# Set page configuration
st.set_page_config(page_title="Load Calculation", layout="wide")

# Logo and description
st.image("images/Sunman_logo.png", width=300)
st.subheader("SunMan Solar Panels - Ultra-light, Glass-free Technology")
st.write(
    "This web tool provides a structural framework for adhering solar panels directly onto roofs without the need for screws. "
    "The panels are made from a durable, glass-free organic polymer composite that excels in various climatic conditions and extreme temperatures. "
    "Please note that the tool does not assume responsibility for any errors, and users are advised to verify the results independently."
)
st.write("")

# Section header with icon
col1, col2 = st.columns([1, 25])
with col1:
    st.image("images/icon2.png")
with col2:
    st.subheader("Load Calculation")

# Content title
st.write("**To determine if panels can be installed on existing buildings, consider these key loads and parameters.**")

# Bullet points
st.write("""
- The lightweight panels, with a self-weight of less than 3.0 kg/m², typically do not pose structural issues since their load is minimal compared to the roof’s weight and other loads such as snow.  
- Wind suction is usually the key factor in deciding suitable buildings for panel installation and the amount of adhesive needed to secure the panels.  
- To ensure structural safety in accordance with Eurocode, the design action must not exceed the design resistance: 𝐸𝑑 ≤ 𝑅𝑑.
""")
