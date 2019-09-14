from search import search_number
from parser import process

def main():
    file_path = search_number('755205')
    record = process(file_path)
    
main()

