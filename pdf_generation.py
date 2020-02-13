
from fpdf import FPDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.cell(200, 10, txt="KeyWords[i]"+': ' +  "Result[i]", ln=1, align="C")
#pdf.cell(200, 10, txt=Name, ln=1, align="C")

#pdf.cell(200, 10, txt=Gender, ln=1, align="C")



pdf.output("Result[0].pdf")