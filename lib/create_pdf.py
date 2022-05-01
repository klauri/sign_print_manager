from classes.PDF_Template import PDF_Template

title = 'PDF Test'

def generate_pdf(filename: str):
    pdf = PDF_Template(orientation='L', format='Letter')
    pdf.set_title(title)
    pdf.output(f'saved_pdfs/{filename}', 'F')

