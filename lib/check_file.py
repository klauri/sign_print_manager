from pathlib import Path

def check_file_exists(filename: str, dir: str, filetype: str):
    working_dir = Path().absolute()
    filepath = f'{working_dir}/{dir}/{filename}'
    file = Path(f'{filepath}{filetype}')
    if file.is_file():
        return True
    else:
        return False