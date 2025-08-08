import streamlit as st

# Set page configuration
st.set_page_config(page_title="Construction", layout="wide")

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
col1, col2 = st.columns([1, 15])
with col1:
    st.image("images/icon8.png", width=60)
with col2:
    st.subheader("Construction")

# Content title
st.write("**Installation and Compliance Protocols**")

# Bullet list
st.write("""
- Installation must be performed exclusively by qualified companies.  
- Assembly instructions should be followed as provided by the manufacturer.  
- Documentation of the building process, including photos of the preparation, cleaning and quality control measures is highly recommended.
""")
