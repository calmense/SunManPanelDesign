import streamlit as st

# Set page configuration
st.set_page_config(page_title="Initial Evaluation", layout="wide")

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
col1, col2 = st.columns([1, 22])
with col1:
    st.image("images/icon1.png")
with col2:
    st.subheader("Initial Evaluation / Due Diligence")

# Content title
st.write("**To determine if panels can be installed on existing buildings, check whether these initial criteria are met.**")

# Evaluation checklist
st.write("""
- Does your roof fit within the parameters: less than 25 meters in height and a slope of less than 5 degrees?  
  Roofs beyond these limits are still feasible but require a bespoke wind calculation.  
- Check the roof structure: Is the minimal additional weight likely to cause any issues?  
  Refer to a structural engineer if uncertain.  
- Check the roof surface membrane:  
  - Is the material or substructure suitable?  
  - What is the age and condition – any corrosion or peeling?  
  - Is cleaning or repair of the surface necessary?
""")
