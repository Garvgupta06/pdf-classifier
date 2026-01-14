from pathlib import Path
from pyPDF2 import PdfReader
def extract_books():
    directory = Path("D:\\pdf-classifier\\data\\books")
    for pdf in directory.iterdir():
        if pdf.is_file():
            print(pdf)

extract_books()    
        

