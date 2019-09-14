from search import search_number
from parser import process

def main():
    file_path = search_number('755205')
    if 'Error' not in file_path:
        record, status = process(file_path)
        return record, status
    else:
        return 'Error', 'Not Found'
main()

