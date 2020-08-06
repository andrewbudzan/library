import os
import pdf_reader
from pprint import pprint

path = './books'
books = os.listdir(path)

for book in books:
    path_to_book = path + '/' + book
    try:
        pprint(pdf_reader.get_info(path_to_book))
    except:
        print(f'cannot reach "{book.split(sep=".")[0]}" metadata')


# with open('content.md', 'a') as f:
#     for book in books:
#         title, format = book.split(sep='.')
#         table_line = f'{title}|[link](/books/{".".join([title, format])})|{format}'
#         f.write(table_line + '\n')
