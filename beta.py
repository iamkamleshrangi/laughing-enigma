import requests 
from bs4 import BeautifulSoup
import deathbycaptcha

def search_number():
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
    h = open('captcha.jpeg','wb')
    h.write(img.content)
    h.close()
    captcha = client.decode('captcha.jpeg', 100)
    print('captcha {}'.format(captcha))

    payload['ToolkitScriptManager1_HiddenField'] = tt
    payload['__EVENTTARGET'] = ''
    payload['__EVENTARGUMENT'] = ''
    payload['btnView'] = 'View+'
    payload['applNumber'] = '563412'
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

    dddd = agent.post('http://ipindiaonline.gov.in/eregister/Application_View.aspx', data=load).content

    yy = open('xx.html','wb')
    yy.write(dddd)
    yy.close()

search_number()
