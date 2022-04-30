from classes.PDF_Template import PDF_Template

title = 'PDF Test'

def generate_pdf():
    pdf = PDF_Template()
    pdf.set_title(title)
    pdf.set_author('Jules Verne')
    pdf.print_chapter(1, 'A RUNAWAY REEF', '20k_c1.txt')
    pdf.print_chapter(2, 'THE PROS AND CONS', '20k_c2.txt')
    pdf.output('tuto3.pdf', 'F')
    
if __name__=='__main__':
    generate_pdf()