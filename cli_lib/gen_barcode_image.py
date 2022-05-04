import click
from pathlib import Path
from classes.Barcode import Barcode
from lib.create_pdf import generate_pdf

@click.group()
@click.option('-f', '--filename', type=str, help='Path of generated barcode image.')
@click.option('-u', '--upc', type=str, help='UPC Number')
def cli_create_barcode(filename: str, upc: str):
    """
        Generates PNG image of barcode from UPC number
        Saves file to ./saved_barcodes
    """
    working_dir = Path().absolute()
    file_type = '.png'
    filepath = f'{working_dir}/saved_barcodes/{filename}'
    file = Path(f'{filepath}.png')
    if file.is_file():
        raise FileExistsError('Barcode already generated')
    else:
        generated_barcode = Barcode(upc)
        generated_barcode.save_to_file(filepath)
        click.echo(f'Barcode generated. Path to File: {filepath}')
