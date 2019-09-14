import requests 
from bs4 import BeautifulSoup
import deathbycaptcha
import uuid, os 

def search_number(application_number):
    agent = requests.session()
    url = 'http://ipindiaonline.gov.in/eregister/Application_View.aspx'
    html = agent.get(url)
    soup = BeautifulSoup(html.content, 'lxml')

    pay = dict()
    for param in soup.find_all('input',{'type':"hidden"}):
        key = param.get('id')
        value = param.get('value')
        pay[key] = value

    pay['__EVENTTARGET'] = 'rdb$0'
    pay['__EVENTARGUMENT'] = ''
    pay['__LASTFOCUS'] = ''
    pay['rdb'] = 'N'

    tt = ''
    for dd in soup.find_all('script'):
        ch = dd.get('src')
        if ch and '/eregister/Application_View.aspx' in ch:
            tt = ch.split('TSM_CombinedScripts_=')[1]
    pay['ToolkitScriptManager1_HiddenField'] = tt
    html = agent.post('http://ipindiaonline.gov.in/eregister/Application_View.aspx',data=pay)

    soup = BeautifulSoup(html.content, 'lxml')

    payload = dict()
    for param in soup.find_all('input',{'type':"hidden"}):
        key = param.get('id')
        value = param.get('value')
        payload[key] = value

    tt = ''
    for dd in soup.find_all('script'):
        ch = dd.get('src')
        if ch and '/eregister/Application_View.aspx' in ch:
            tt = ch.split('TSM_CombinedScripts_=')[1]

    captcha_url = 'http://ipindiaonline.gov.in/eregister/captcha.ashx'
    client = deathbycaptcha.SocketClient('cubictree', 'P@ssw0rd')
    img = agent.get(captcha_url)
    captcha_path = uuid.uuid4().hex + '.jpeg'
    h = open(captcha_path, 'wb')
    h.write(img.content)
    h.close()
    captcha = client.decode(captcha_path, 100)
    print('captcha {}'.format(captcha))
    os.remove(captcha_path)
    payload['ToolkitScriptManager1_HiddenField'] = tt
    payload['__EVENTTARGET'] = ''
    payload['__EVENTARGUMENT'] = ''
    payload['btnView'] = 'View+'
    payload['applNumber'] = application_number
    payload['captcha1'] = captcha['text']

    url = 'http://ipindiaonline.gov.in/eregister/Application_View.aspx'
    html = agent.post(url, data=payload).content

    soup = BeautifulSoup(html, 'lxml')
    load = dict()
    for param in soup.find_all('input',{'type':"hidden"}):
        key = param.get('id')
        value = param.get('value')
        load[key] = value

    tt = ''
    for dd in soup.find_all('script'):
        ch = dd.get('src')
        if ch and '/eregister/Application_View.aspx' in ch:
            tt = ch.split('TSM_CombinedScripts_=')[1]

    load['ToolkitScriptManager1_HiddenField'] = tt
    load['__EVENTTARGET'] = 'SearchWMDatagrid$ctl03$lnkbtnappNumber1'
    load['__EVENTARGUMENT'] = ''

    html = agent.post('http://ipindiaonline.gov.in/eregister/Application_View.aspx', data=load)
    if html.status_code == 200:
        soup = BeautifulSoup(html.content, 'lxml')
        error = soup.find('span',{'id':"errorText"})
        if error:
            error = error.text.strip()
            return 'Not Found'
        else:
            file_name = uuid.uuid4().hex + '.html'
            hh = open(file_name, 'wb')
            hh.write(html.content)
            hh.close()
            return 'Success'
    else:
        return 'Error'

arr = ['755205', '563412', '563411', '563410', '563112', '553412', '564412']
for number in arr:
    rr = search_number(number)
    print(rr)
    
