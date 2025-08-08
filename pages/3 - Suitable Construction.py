import streamlit as st

# Set page configuration
st.set_page_config(page_title="Suitable Construction", layout="wide")

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
    st.image("images/icon3.png", width=50)
with col2:
    st.subheader("Suitable Construction")

# Content title
st.write("**Structural adhesives can be used to attach the panels directly or using sub-frames without mechanical connectors.**")

# Bullet-style explanation
st.write("""
- Direct fixing to roof membrane or with substructure.  
- All glued joints must be strong enough to withstand design loads without permanent deformation.  
- Safety Factor Key:  
  - ETAG-based total factor  
  - Eurocode-based partial safety factors (Load & Material)
""")
