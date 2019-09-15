from search import search_number
from parser import process
import requests 
import PyPDF2 

def main():
    file_path = search_number('755205')
    if 'Error' not in file_path:
        record, status = process(file_path)
        return record, status
    else:
        return 'Error', 'Not Found'

def get_pdf():
    url = 'http://www.ipindia.nic.in/writereaddata/Portal/IPOJournal/1_4786_1/CLASS_14_-_24.pdf'
    html = requests.get(url).content
    hd = open('1.pdf','wb')
    hd.write(html)
    hd.close()

def pdf_reader():
    pdfFileObj = open('1.pdf', 'rb') 
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
    nos = pdfReader.numPages
    print(dir(pdfReader))
    count = 1
    for page_no in range(0, nos):
        pageObj = pdfReader.getPage(page_no) 
        print(pageObj.extractText()) 
        print('==' * 20)
        if count == 100:
            break
        count += 1

pdf_reader()
