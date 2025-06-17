import streamlit as st
import plotly.graph_objects as go
from PIL import Image

def quantities(numberGlueLines, width, glueWidthReq):
    
        st.write("")
        st.write("")
        st.write("")

        col1, col2 = st.columns([1,22])
        with col1:
            st.image("images/icon11.png")
        with col2:
            st.header("Quantities")

        st.write('Chose how many panels you have in each roof area.')

        with st.expander("Expand"):
            glueLength = numberGlueLines*width

            st.subheader("Input")
            st.markdown('The gluing thickness is considered as <b>t = 5 mm</b>', unsafe_allow_html=True)
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
            st.subheader("Number of Panels")
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                noAreaH = st.number_input('Area H', min_value=0, step=1, format="%i", value=1)
                st.write("")
                n = 0
                st.write("Width per gluing line: <b> w = " + str(int(glueWidthReq[n]))+ ' mm</b>', unsafe_allow_html=True)
                sausagesAreaH = glueWidthReq[n] * glueLength/1000**2
                st.write("Glue area per panel: <b> A = " + str(sausagesAreaH)+ ' m<sup>2</sup></b>', unsafe_allow_html=True)
                sausagesVolumeH = round(sausagesAreaH * 0.005, 4)
                st.write("Glue volume per panel: <b> V = " + str(sausagesVolumeH)+ ' m<sup>3</sup></b>', unsafe_allow_html=True)
                sausagesVolumeHtot = round(sausagesVolumeH * noAreaH, 4)
                st.write("Glue volume per roof area: <b> V = " + str(sausagesVolumeHtot)+ ' m<sup>3</sup></b>', unsafe_allow_html=True)

            with col2:
                noAreaF = st.number_input('Area F', min_value=0, step=1, format="%i", value=1)
                st.write("")
                n = 1
                st.write("Width per gluing line: <b> w = " + str(int(glueWidthReq[n]))+ ' mm</b>', unsafe_allow_html=True)
                sausagesAreaF = glueWidthReq[n] * glueLength/1000**2
                st.write("Glue area per panel: <b> A = " + str(sausagesAreaF)+ ' m<sup>2</sup></b>', unsafe_allow_html=True)
                sausagesVolumeF = round(sausagesAreaF * 0.005, 4)
                st.write("Glue volume per panel: <b> V = " + str(sausagesVolumeF)+ ' m<sup>3</sup></b>', unsafe_allow_html=True)
                sausagesVolumeFtot = round(sausagesVolumeF * noAreaF, 4)
                st.write("Glue volume per roof area: <b> V = " + str(sausagesVolumeFtot)+ ' m<sup>3</sup></b>', unsafe_allow_html=True)

            with col3:
                noAreaG = st.number_input('Area G', min_value=0, step=1, format="%i", value=1)
                st.write("")
                n = 2
                st.write("Width per gluing line: <b> w = " + str(int(glueWidthReq[n]))+ ' mm</b>', unsafe_allow_html=True)
                sausagesAreaG = glueWidthReq[n] * glueLength/1000**2
                st.write("Glue area per panel: <b> A = " + str(sausagesAreaG)+ ' m<sup>2</sup></b>', unsafe_allow_html=True)
                sausagesVolumeG = round(sausagesAreaG * 0.005, 4)
                st.write("Glue volume per panel: <b> V = " + str(sausagesVolumeG)+ ' m<sup>3</sup></b>', unsafe_allow_html=True)
                sausagesVolumeGtot = round(sausagesVolumeG * noAreaG, 4)
                st.write("Glue volume per roof area: <b> V = " + str(sausagesVolumeGtot)+ ' m<sup>3</sup></b>', unsafe_allow_html=True)

            st.write("")
            st.write("")
            st.subheader("Estimate Total")

            totalVolume = sausagesVolumeHtot + sausagesVolumeFtot + sausagesVolumeGtot
            numberTubes = int(round(totalVolume * 1000000 / 600 + 0.5,0))
            numberTubesFact = int(round(numberTubes*1.1 + 0.5, 1))

            st.write("Total number of tubes: " + str(numberTubes), unsafe_allow_html=True)
            st.write("<b>Total number of tubes: " + str(numberTubesFact)+ ' (incl. 10%)</b>', unsafe_allow_html=True)
            st.markdown("<b>Note:</b> It is advised to consider a waste factor of 10%.", unsafe_allow_html=True)

            st.write("")
            st.write("")
            st.write("")

        return {
            "width": width,
            "numberTubes": numberTubes,
            "numberTubesFact": numberTubesFact
        }
