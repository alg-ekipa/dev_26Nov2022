import urllib.request
import urllib.parse

#upit oblika https://www.google.hr/search?q=programiranje+u+pythonu ubacujemo u metodu urlopen
#korištenjem modula parse modificirat ćemo naš upit tako da odgovara http upitu

upit = 'programiranje+u+pythonu'

parse_upit = urllib.parse.quote(upit)
print(parse_upit)
upit_kodiran = parse_upit.encode('utf-8')
print(upit_kodiran)

URL_google = f'https://www.google.hr/search?q={upit}'
print (URL_google)

request = urllib.request.Request(URL_google)
response = urllib.request.urlopen(request)

print(response.read().decode())