
import urllib.request,  urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE



url = input('Enter URL:')
co = input('Enter Count:')
posi = input('Enter Position:')

for i in range(int(co)):
    html = urllib.request.urlopen(url , context = ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    number = 0
    for tag in tags:
        number += 1
        if number == int(posi):
            url = tag.get('href')
            if i == int(co)-1:
                print (tag.contents[0])
                break
