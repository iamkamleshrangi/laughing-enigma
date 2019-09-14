from bs4 import BeautifulSoup

def parser(file_path):
    content = open(file_path, 'rb').read()
    soup = BeautifulSoup(content, 'lxml')
    table = soup.find('table',{'style':"font-size=larger; background-color:mintcream;"})
    record = dict()
    for tr in table.find_all('tr'):
        tds = [ i.text.replace('.',' ').replace('\xa0','').strip() for i in tr.find_all('td') ]
        if len(tds) == 2:
            record[tds[0]] = tds[1]

    for table in soup.find_all('table',{'style':"font-size=larger; "}):
        for tr in table.find_all('tr'):
            for td in tr.find_all('td'):
                tds = [ i.text.replace('.',' ').strip() for i in td.find_all('font') ]
                tds = [ i.replace(':','').replace('\xa0','').strip() for i in tds ]
                if len(tds) == 2:
                    record[tds[0]] = tds[1]
    return record, record.get('Status','N/A')
