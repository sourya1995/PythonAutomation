import os
import argparse
import csv
import docx
from bs4 import UnicodeDammit
from PyPDF2 import PdfFileReader

def search_txt(filename, word):
    with open(filename, 'rb') as file:
        content = file.read(1024)

    suggestion = UnicodeDammit(content)
    encoding = suggestion.original_encoding


    with open(filename, encoding=encoding) as file:
        for line in file:
            if word in line.lower():
                return True
            
    return False 

def search_csv(filename, word):
    with open(filename) as file:
        for row in csv.reader(file):
            for column in row:
                if word in column.lower():
                    return True
                
    return False


def search_pdf(filename, word):
    with open(filename, 'rb') as file:
        reader = PdfFileReader(file)
        if reader.isEncrypted:
            return False
        for page in reader.pages:
            text = page.extractText()
            if word in text.lower():
                return True
    
    return False


def search_docx(filename, word):
    doc = docx.Document(filename)
    for para in doc.paragraphs:
        if word in para.text.lower():
            return True
    
    return False


EXTENSIONS = {
    'txt': search_txt,
    'csv': search_csv,
    'pdf': search_pdf,
    'docx': search_docx
}

def main(word):
    for root, dirs, files in os.walk('.'):
        for file in files:
            extension = file.split('.')[-1]
            if extension in EXTENSIONS:
                search_file = EXTENSIONS.get(extension)
                filename = os.path.join(root, file)
                if search_file(filename, word):
                    print(f'Word found in {filename}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-w', type=str, help='Word to search', default='the')
    args = parser.parse_args()
    main(args.w.lower())


