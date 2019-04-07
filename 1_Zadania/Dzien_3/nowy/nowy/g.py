import requests
import pprint

r = requests.get("http://onet.pl")

print(r)

pprint.pprint(r.content)

with open('index.html', 'wb') as f:
    f.write(r.content)

def pobierz_stronke(page_url):
    r = requests.get(page_url)
    return r.content

print(pobierz_stronke("http://docs.python-requests.org/en/master/")[:20])
print(pobierz_stronke("http://onet.pl"))