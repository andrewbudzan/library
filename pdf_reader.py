from PyPDF2 import PdfFileReader
from pprint import pprint


def get_info(file):
    ''' read pdf file metadata and return dictionary '''
    book = PdfFileReader(file)
    info_dict = {
        'title': book.documentInfo.title,
        'author': book.documentInfo.author,
        'pages': book.getNumPages(),
        'subject': book.documentInfo.subject,
    }
    return info_dict
