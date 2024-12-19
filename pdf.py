from fpdf import FPDF

class PDFGenerator:
    def __init__(self, output_filename="weather_forecast.pdf"):
        self.output_filename = output_filename

    def generate_pdf(self, content):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Add content to the PDF
        for line in content.splitlines():
            pdf.cell(200, 10, txt=line, ln=True)

        # Save the PDF to the specified file
        pdf.output(self.output_filename)

        return self.output_filename
