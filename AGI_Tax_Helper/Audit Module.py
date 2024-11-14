import pandas as pd
from fpdf import FPDF

class AuditReport(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Audit Report", 0, 1, "C")

    def add_entry(self, entry):
        self.set_font("Arial", "", 10)
        for key, value in entry.items():
            self.cell(0, 10, f"{key}: {value}", 0, 1)

def generate_audit_report(data):
    pdf = AuditReport()
    pdf.add_page()
    for _, entry in data.iterrows():
        pdf.add_entry(entry.to_dict())
    pdf.output("audit_report.pdf")