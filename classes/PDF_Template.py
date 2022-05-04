from fpdf import FPDF
title = 'PDF Test'

class PDF_Template(FPDF):

    def header(self):
        self.set_font('Arial', 'B', 14)
        w = self.get_string_width(title)
        self.set_x((210 - w)/2)
        self.set_draw_color(0, 80, 180)
        self.set_fill_color(230, 230, 0)
        self.set_text_color(220, 50, 50)
        self.set_line_width(1)
        self.cell(w, 9, title, 1, 1, 'C', 1)
        self.ln(10)

    def footer(self):
        self.set_y(-50)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(128)
        self.image('saved_barcodes/apples.png', type='PNG', x=90, w=100, h=50)
    