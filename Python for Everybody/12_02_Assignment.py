
import urllib.request,  urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input("Enter URL: ")
page = urllib.request.urlopen(url , context = ctx).read()
soup = BeautifulSoup(page, "html.parser")

spans = soup('span')

numbers = []

for span in spans:
    numbers.append(int(span.string))

print (sum(numbers))
