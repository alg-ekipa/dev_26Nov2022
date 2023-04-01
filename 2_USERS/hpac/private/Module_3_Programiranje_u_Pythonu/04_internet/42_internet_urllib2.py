import urllib.request
import urllib.parse

# upit oblika https://www.google.com/search?q=programiranje+u+pythonu ubacujemo u metodu urlopen()
# korištenjem modula parse, modificirat ćemo naš upit tako da odgovra http upit

upit = 'programiranje+u+pythonu'

parse_upit = urllib.parse.quote(upit)

print(parse_upit)
upit_kodiran = parse_upit.encode('utf-8')
print(upit_kodiran)

URL_google = f'https://www.google.com/search?q={upit_kodiran}'
print(URL_google)

request = urllib.request.Request(URL_google)
respons = urllib.request.urlopen(request)

print(respons.read().decode())