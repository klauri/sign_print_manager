import click
from pathlib import Path
from classes.Barcode import Barcode
from lib.create_pdf import generate_pdf
from lib.check_file import check_file_exists

@click.command()
@click.option('-f', '--filename', type=str, help='Name of barcode image file.')
@click.option('-u', '--upc', type=str, help='11 Digit UPC Number')
def cli_create_barcode(filename: str, upc: str):
    """
        Generates PNG image of barcode from UPC number
        Saves file to ./saved_barcodes
    """
    file_exists = check_file_exists(filename, '/saved_barcodes', '.png')
    if file_exists:
        raise FileExistsError('Barcode already generated')
    else:
        generated_barcode = Barcode(upc)
        generated_barcode.save_to_file(f'saved_barcodes/{filename}')
        click.echo(f'Barcode generated. Path to File: {filename}')
