import urllib.request
import urllib.parse
# upit oblika https://www.google.com/search?client=firefox-b-d&q=programiranje+u+pythonu ubacujemo u metodu urlopen()
# korištenjem modula parse modificirat ćemo naš upit tako da odgovara http upitu

upit='programiranje+u+pythonu'
parse_upit = urllib.parse.quote(upit)
print(parse_upit)

upit_kodiran = parse_upit.encode('utf-8')
print(upit_kodiran)

URL_google = f'https://www.google.com/search?client=firefox-b-d&q={upit}'
print(URL_google)

requests=urllib.request.Request(URL_google)
response=urllib.request.urlopen(requests)

print(response.read().decode())
