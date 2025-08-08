import streamlit as st

# Set page configuration
st.set_page_config(page_title="Glue Joint Resistance", layout="wide")

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
col1, col2 = st.columns([1, 23])
with col1:
    st.image("images/icon4.png", width=50)
with col2:
    st.subheader("Glue Joint Resistance")

# Content title
st.write("**Design Guidelines for Adhesive Use**")

# Explanation
st.write(
    "The glue joint resistance needs to be obtained and verified from a glue manufacturer according to European standards.\n\n"
    "The design glue joint resistance is either:"
)

# Bullet list
st.write("""
- Not approved by ETAG and needs reduction according to Eurocode-based partial safety factors  
  (non-approved products typically rely on testing and data from the manufacturer), or  
- Approved by ETAG, with independent testing and safety factors included in the "design strength", eliminating the need for reduction factors.
""")
