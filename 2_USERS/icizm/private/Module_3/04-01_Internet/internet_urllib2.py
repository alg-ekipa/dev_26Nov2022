import urllib.request
import urllib.parse 

# upit oblika https://www.google.com/search?q=programiranje+u+pythonu ubacujemo u metodu urlopen()
# korištenjem modula parse modificirat ćemo naš upit tako da odgovara http upitu

upit = "programiranje+u+pythonu"

parse_upit = urllib.parse.quote(upit)

print(parse_upit)

upit_kodiran = parse_upit.encode('utf-8')

print(upit_kodiran)

URL_google = f'https://www.google.com/search?q={upit_kodiran}' # tu bi složili string i dodali upit

print(URL_google)

# i to bi sad on trebao ubaciti u request

request = urllib.request.Request(URL_google)
rspns_odgovor = urllib.request.urlopen(request)

print(rspns_odgovor.read().decode())

''' Uzeli smo primjer kroz search i nije nam dao Google na kraju da pristupimo jer bi svi onda mogli pristupiti. 
Pogledati u tobots.txt na cloudu - neda kroz search scrapanje podataka'''