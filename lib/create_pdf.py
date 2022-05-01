from classes.PDF_Template import PDF_Template

title = 'PDF Test'

def generate_pdf(filename: str):
    pdf = PDF_Template(orientation='L', format='Letter')
    pdf.set_title(title)
    pdf.output(filename, 'F')
    
if __name__=='__main__':
    generate_pdf()