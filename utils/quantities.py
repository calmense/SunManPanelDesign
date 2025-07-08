import streamlit as st
import plotly.graph_objects as go
from PIL import Image

def quantities(glueLength, width, glueWidthFinal, minThickness):
    
        st.write("")
        st.write("")
        st.write("")
        col1, col2 = st.columns([3, 60])
        with col1:
            st.image("images/icon11.png", width=50)
        with col2:
            st.subheader("Quantities")

        st.write('Chose how many panels you have in each roof area.')

        with st.expander("Expand"):

            st.markdown("#### Input")
            st.markdown('The gluing thickness is considered as <b>t = '+ str(minThickness) +' mm</b>', unsafe_allow_html=True)
            st.markdown('One panel has a gluing length of <b>L = ' + str(glueLength/1000) + ' m</b>.', unsafe_allow_html=True)
            st.markdown('The gluing tube contains <b>600 ml </b>glue.', unsafe_allow_html=True)


            if 'noAreaH' not in st.session_state:
                st.session_state.noAreaH = 2
            if 'noAreaF' not in st.session_state:
                st.session_state.noAreaH = 2
            if 'noAreaG' not in st.session_state:
                st.session_state.noAreaH = 2

            # Layout for columns
            st.write("")
            st.write("")
            st.markdown("#### Number of Panels")
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                noAreaH = st.number_input('Area H', min_value=0, step=1, format="%i", value=1)
                st.write("")
                n = 0
                st.write("Width per gluing line: <br> <b> w = " + str(float(glueWidthFinal[n]))+ ' mm</b>', unsafe_allow_html=True)
                sausagesAreaH = float(glueWidthFinal[n]) * glueLength/1000**2
                st.write("Glue area per panel: <br> <b> A = " + str(sausagesAreaH)+ ' m<sup>2</sup></b>', unsafe_allow_html=True)
                sausagesVolumeH = round(sausagesAreaH * minThickness/1000, 4)
                st.write("Glue volume per panel: <br> <b> V = " + str(sausagesVolumeH)+ ' m<sup>3</sup></b>', unsafe_allow_html=True)
                sausagesVolumeHtot = round(sausagesVolumeH * noAreaH, 4)
                st.write("Glue volume per roof area: <br> <b> V = " + str(sausagesVolumeHtot)+ ' m<sup>3</sup></b>', unsafe_allow_html=True)

            with col2:
                noAreaF = st.number_input('Area F', min_value=0, step=1, format="%i", value=1)
                st.write("")
                n = 1
                st.write("Width per gluing line: <br> <b> w = " + str(float(glueWidthFinal[n]))+ ' mm</b>', unsafe_allow_html=True)
                sausagesAreaF = float(glueWidthFinal[n]) * glueLength/1000**2
                st.write("Glue area per panel: <br> <b> A = " + str(sausagesAreaF)+ ' m<sup>2</sup></b>', unsafe_allow_html=True)
                sausagesVolumeF = round(sausagesAreaF * minThickness/1000, 4)
                st.write("Glue volume per panel: <br> <b> V = " + str(sausagesVolumeF)+ ' m<sup>3</sup></b>', unsafe_allow_html=True)
                sausagesVolumeFtot = round(sausagesVolumeF * noAreaF, 4)
                st.write("Glue volume per roof area: <br> <b> V = " + str(sausagesVolumeFtot)+ ' m<sup>3</sup></b>', unsafe_allow_html=True)

            with col3:
                noAreaG = st.number_input('Area G', min_value=0, step=1, format="%i", value=1)
                st.write("")
                n = 2
                st.write("Width per gluing line: <br> <b> w = " + str(float(glueWidthFinal[n]))+ ' mm</b>', unsafe_allow_html=True)
                sausagesAreaG = float(glueWidthFinal[n]) * glueLength/1000**2
                st.write("Glue area per panel: <br> <b> A = " + str(sausagesAreaG)+ ' m<sup>2</sup></b>', unsafe_allow_html=True)
                sausagesVolumeG = round(sausagesAreaG * minThickness/1000, 4)
                st.write("Glue volume per panel: <br> <b> V = " + str(sausagesVolumeG)+ ' m<sup>3</sup></b>', unsafe_allow_html=True)
                sausagesVolumeGtot = round(sausagesVolumeG * noAreaG, 4)
                st.write("Glue volume per roof area: <br> <b> V = " + str(sausagesVolumeGtot)+ ' m<sup>3</sup></b>', unsafe_allow_html=True)

            st.write("")
            st.write("")
            st.markdown("#### Estimate Total")

            st.write(
                "<b>Note: </b>The quantities provided are for direct bonding to the roof. "
                "<br>For bonding to a substructure, these quantities must be doubled."
                "<br>It is also advised to consider a waste factor of 10%.",
                unsafe_allow_html=True
            )

            totalVolume = sausagesVolumeHtot + sausagesVolumeFtot + sausagesVolumeGtot
            numberTubes = float(round(totalVolume * 1000000 / 600 + 0.5,0))
            numberTubesFact = float(round(numberTubes*1.1 + 0.5, 1))

            st.write("")
            st.write("Total number of tubes: " + str(numberTubes), unsafe_allow_html=True)
            st.write("<b>Total number of tubes: " + str(numberTubesFact)+ ' (incl. 10%)</b>', unsafe_allow_html=True)

            st.write("")
            st.write("")
            st.write("")
      

        return {
            "width": width,
            "numberTubes": numberTubes,
            "numberTubesFact": numberTubesFact
        }
