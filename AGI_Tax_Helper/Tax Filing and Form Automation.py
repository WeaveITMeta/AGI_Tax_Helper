from fpdf import FPDF

class TaxForm1040(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Form 1040", 0, 1, "C")

    def fill_personal_info(self, name, ssn, address):
        self.set_font("Arial", "", 10)
        self.cell(0, 10, f"Name: {name}", 0, 1)
        self.cell(0, 10, f"SSN: {ssn}", 0, 1)
        self.cell(0, 10, f"Address: {address}", 0, 1)

    def fill_income_info(self, wage_income, business_income):
        self.cell(0, 10, f"Wage Income: {wage_income}", 0, 1)
        self.cell(0, 10, f"Business Income: {business_income}", 0, 1)

pdf = TaxForm1040()
pdf.add_page()
pdf.fill_personal_info("John Doe", "123-45-6789", "123 Elm St")
pdf.fill_income_info(50000, 10000)
pdf.output("form_1040.pdf")