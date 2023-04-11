import urllib.request
import urllib.parse   #

#upit oblika  https://www.google.com/search?client=firefox-b-d&q=proggramiranje+u+paytonu uput toga oblika
#ubacujemo u metodu urlopen() koristenjem modula parse modificiramo cemo nas upiut tako da odgovara http upitu

upit = 'programiranje+u+pythonu' # upit koji nam je potreban

parse_upit = urllib.parse.quote(upit) #pretvaranje ušpita pomocu "parse"
print(parse_upit)
upit_kodiran = parse_upit.encode('utf-8') # prekodiranje upita
print(upit_kodiran)

'''ovo je originalno kao u pocetku'''
URL_google = f'https://www.google.com/search?={upit}'
print(URL_google)

request = urllib.request.Request(URL_google)
respons = urllib.request.urlopen(request)

print(respons.read().decode())