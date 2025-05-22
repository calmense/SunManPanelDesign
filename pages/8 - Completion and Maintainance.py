import streamlit as st

# Set page configuration
st.set_page_config(page_title="Completion and Maintenance", layout="wide")

# Logo + Einführung
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
    st.image("images/icon9.png")  # Optional, fills column
with col2:
    st.subheader("Completion and Maintenance")

# Content
st.write("**Establishing Maintenance and Inspection Guidelines**")
st.write("""
- The operator must create detailed operating instructions.  
- Regular tasks should include cleaning and inspecting contact surfaces for any unwanted deformations, as well as checking the adhesive surfaces.  
- The inspection intervals should be determined. Typically, annual visual inspections are recommended.  
- An independent inspection by a specialized company should occur at extended intervals, potentially every five years and possibly including an adhesion test.
""")
