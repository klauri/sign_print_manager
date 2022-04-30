from dataclasses import dataclass, field
from barcode import UPCA
from barcode.writer import ImageWriter

@dataclass
class Barcode:
    upc: str
    barcode: object = field(init = False)

    def __post_init__(self):
        self.barcode = UPCA(self.upc, writer=ImageWriter())

    def save_to_file(self, filename: str):
        self.barcode.save(filename)
