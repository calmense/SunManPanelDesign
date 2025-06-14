from datetime import date
from fpdf import FPDF
import plotly.io as pio
import tempfile

class SunmanPDF(FPDF):
    def __init__(self, logo_path=None):
        super().__init__()
        self.logo_path = logo_path

    def header(self):
        # --- Title: "SunMan Solar Panels" ---
        self.set_xy(10, 12)  # top left margin
        self.set_font("Arial", "B", 16)
        self.set_text_color(0)  # black
        self.cell(0, 8, "SunMan Solar Panels", ln=1, align="L")

        # --- Subtitle: "Structural Report" in grey ---
        self.set_font("Arial", "", 12)
        self.set_text_color(100)  # grey
        self.cell(0, 6, "Structural Report", ln=1, align="L")

        # Reset text color for the rest of the document
        self.set_text_color(0)

        # --- Logo (right side, slightly lower and smaller) ---
        if self.logo_path:
            self.image(self.logo_path, x=160, y=14, w=30)  # w=30 for smaller logo, y=14 to lower it slightly

        self.ln(10)  # space after header

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", size=8)

        # Date bottom left
        today = date.today().strftime("%Y-%m-%d")
        self.cell(0, 10, today, align="L")

        # Page number bottom right
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="R")

    def insert_plot_image(pdf, image_path, caption, width, xOffset, yOffset):
        pdf.set_font("Arial", "I", 9)
        pdf.ln(4)
        pdf.cell(0, 6, caption, ln=True)
        pdf.ln(1)
        pdf.image(image_path, w=width, x=xOffset, y=yOffset)
        pdf.set_font("Arial", "", 11)



def generate_pdf_summary(
    country, windZone, fundBasicWindVelocity, baseVelocityPressure,
    terrainCategory, buildingHeight, gustSpeedPressure,
    buildingLength, buildingWidth,
    panelSize, width, height, area, gluingDistance,
    designGlueJointResistance, designGlueJointResistanceValue,
    glueWidthReq, glueWidthChos, glueWidthUtil, 
    figBuilding, figTable, figPanel, figCheck,
    panel_image_path=None,
    logo_path="images/Sunman_logo.png",
    country_path="images/Country_image.png"
):
    pdf = SunmanPDF(logo_path=logo_path)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.set_font("Arial", "I", 11)
    pdf.multi_cell(0, 6, (
    "This report provides a structural framework for solar panels by SunMan. "
    "Please note that the tool does not assume responsibility for any errors, "
    "and users are advised to verify the results independently."
    ))
    pdf.cell(0, 8, "", ln=True)

    # images
    # Export the Plotly figure to PNG
    img_table = pio.to_image(figTable, format="png", width=850, height=230)

    # Save the PNG to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmpfile:
        tmpfile.write(img_table)
        table_image_path = tmpfile.name

    # Export the Plotly figure to PNG
    img_building = pio.to_image(figBuilding, format="png", width=800, height=500)

    # Save the PNG to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmpfile:
        tmpfile.write(img_building)
        building_image_path = tmpfile.name

    # ----------------------------
    # Page 1: Wind Load Parameters
    # ----------------------------
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "1. Wind Load Parameters", ln=True)
    
    # Base Velocity Pressure
    pdf.set_font("Arial", "B", 11)
    pdf.cell(0, 8, "1.1 Project Details", ln=True)

    pdf.set_font("Arial", "I", 9)
    pdf.set_text_color(100)  # grey
    pdf.cell(0, 8, "Base Velocity Pressure - EN 1991-1-4 Equation 4.1", ln=True)
    pdf.set_text_color(0)  # black

    pdf.set_font("Arial", "", 11)
    pdf.cell(0, 8, f"Country: {country}", ln=True)
    pdf.cell(0, 8, f"Wind Zone: {windZone}", ln=True)
    pdf.cell(0, 8, f"Fundamental Basic Wind Velocity: {fundBasicWindVelocity} m/s", ln=True)
    pdf.cell(0, 8, f"Base Velocity Pressure: {baseVelocityPressure} kN/m²", ln=True)

    pdf.ln(1)

    # Gust Speed Pressure
    pdf.set_font("Arial", "I", 9)
    pdf.set_text_color(100)  # grey
    pdf.cell(0, 8, "Gust Speed Pressure - EN 1991-1-4 Table 4.1", ln=True)
    pdf.set_text_color(0)  # black
    
    pdf.set_font("Arial", "", 11)
    pdf.cell(0, 8, f"Terrain Category: {terrainCategory}", ln=True)
    pdf.cell(0, 8, f"Building Height: {buildingHeight} m", ln=True)
    pdf.cell(0, 8, f"Gust Speed Pressure: {gustSpeedPressure} N/mm²", ln=True)

    pdf.ln(1)

    # Roof Geometry
    pdf.set_font("Arial", "B", 11)
    pdf.cell(0, 8, "", ln=True)
    pdf.cell(0, 8, "1.3 Roof Geometry", ln=True)

    pdf.set_font("Arial", "I", 9)
    pdf.set_text_color(100)  # grey
    pdf.cell(0, 8, "Wind Load EN 1991-4 Ch. 7.2.3 - External Pressure Coefficients", ln=True)
    pdf.set_text_color(0)  # black

    # image
    pdf.insert_plot_image(building_image_path, "Roof geometry and zones", 120, 10, 210)

    # --- Page break before glue section ---
    pdf.add_page()

    # Design Wind Load
    pdf.set_font("Arial", "B", 11)
    pdf.cell(0, 8, "", ln=True)
    pdf.cell(0, 8, "1.4 Design Wind Load", ln=True)
    pdf.set_font("Arial", "", 11)
    pdf.cell(0, 8, "The design wind load is determined for each roof area.", ln=True)
    pdf.set_font("Arial", "I", 9)
    pdf.set_text_color(100)  # grey
    pdf.cell(0, 8, "DIN EN 1991-1-4 Chapter 7.2.3", ln=True)

    pdf.ln(3)

    # image
    pdf.insert_plot_image(table_image_path, "Design Wind Load", 140, 10, 85)

    # page break
    pdf.add_page()

    # ----------------------------
    # Page 3: Glue Joint Resistance
    # ----------------------------

    # images
    # Export the Plotly figure to PNG
    img_panel = pio.to_image(figPanel, format="png", width=800, height=600)

    # Save the PNG to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmpfile:
        tmpfile.write(img_panel)
        panel_image_path = tmpfile.name

    # Export the Plotly figure to PNG
    img_check = pio.to_image(figCheck, format="png", width=800, height=240)

    # Save the PNG to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmpfile:
        tmpfile.write(img_check)
        check_image_path = tmpfile.name

    pdf.set_font("Arial", "B", 12)
    pdf.set_text_color(0)
    pdf.cell(0, 10, "2. Glue Joint Resistance", ln=True)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "2.1 Glue Joint Parameters", ln=True)
    pdf.set_font("Arial", "", 11)
    pdf.cell(0, 8, f"Glue Manufacturer: {designGlueJointResistance}", ln=True)
    pdf.cell(0, 8, f"Design Glue Joint Resistance: {designGlueJointResistanceValue} N/mm²", ln=True)
    
    pdf.ln(2)

    # Solar Panel
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "2.2 Solar Panel", ln=True)
    pdf.set_font("Arial", "", 11)
    pdf.cell(0, 8, f"Panel Size: {panelSize}", ln=True)
    pdf.cell(0, 8, f"Panel Width: {width} mm", ln=True)
    pdf.cell(0, 8, f"Panel Height: {height} mm", ln=True)
    pdf.cell(0, 8, f"Panel Area: {round(area * 0.001**2, 2)} m²", ln=True)
    pdf.cell(0, 8, f"Gluing Distance: {int(gluingDistance)} mm", ln=True)


    # image
    pdf.insert_plot_image(panel_image_path, "Solar Panel Layout", 140, -40, 135)


    # page break
    pdf.add_page()

    # Gluing Design Table
    pdf.set_font("Arial", "B", 11)
    pdf.cell(0, 8, "", ln=True)
    pdf.cell(0, 8, "2.3 Gluing Design Table", ln=True)
    pdf.set_font("Arial", "", 11)
    pdf.cell(0, 8, "This table shows the required glue width.", ln=True)

    # image
    pdf.insert_plot_image(check_image_path, "Gluing Design Table", 150, 10, 70)

    return pdf.output(dest='S').encode('latin-1')
