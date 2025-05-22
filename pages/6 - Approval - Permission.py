import streamlit as st

# Set page configuration
st.set_page_config(page_title="Approval / Permission", layout="wide")

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
    st.image("images/icon7.png")  # Adjust size as needed
with col2:
    st.subheader("Approval / Permission")

# Content title
st.write("**Local Building Regulations**")

# Main content
st.write(
    "It is the responsibility of the building owner or project developer to ensure compliance with the necessary planning requirements "
    "and to determine if planning permission is required.\n\n"
    "Additional certified testing of adhesives or the system may be necessary as part of project-based construction approval or by local building authorities. "
    "The following information is typically required:"
)

# Bullet list
st.write("""
- Structural Calculations – PV, Subframe and Adhesives  
- Structural Verification – existing roof structure  
- Certified testing data
""")
