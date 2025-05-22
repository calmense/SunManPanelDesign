import streamlit as st

# Set page configuration
st.set_page_config(page_title="Checks on Roof Substructure", layout="wide")

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
col1, col2 = st.columns([1, 17])
with col1:
    st.image("images/icon6.png")
with col2:
    st.subheader("Checks on Roof Substructure")

# Content title
st.write("**Adhesive Application and Structural Assessment Requirements**")

# Bullet list
st.write("""
- An adhesion test is typically required up to this point.  
- Detailed calculations should be performed based on this design guide if applicable or separate load calculation if outside the parameters.  
- Verification of the roof substrate or substructure is necessary to assess tying down forces.  
- Determine the exact layout and width of the glue lines for the chosen product.  
- Identify the surface preparation required, including cleaning, priming, etc.
""")
