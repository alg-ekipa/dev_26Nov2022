import urllib.request
import urllib.parse



#upit oblika https://www.google.com/search?q=programiranje+u+pythonu ubacujemo u metodu urlopen()
#korištenjem modula parse modificirat ćemo naš upit tako da odgovara http upitu


upit = 'programiranje+u+pythonu'

parse_upit=urllib.parse.quote(upit)
print(parse_upit)
upit_kodiran=parse_upit.encode('utf-8')

URL_google= f'https://www.google.com/search?q={upit}'
print(URL_google)


request = urllib.request.Request(URL_google)
respons = urllib.request.urlopen(request)


"""
URL= 'https://www.algebra.hr' #adresa koju želimo otvoriti


#stvaramo objekt koji predstavlja konekciju prema toj adresi

konekcija = urllib.request.urlopen(URL)

#nad konekcijom ćemo zvati metodu read()-čitanje sadržaja stranice i odmah dekodiramo metodom decode()
#pročitano spremamo u varijablu sadržaj
sadrzaj=konekcija.read().decode()
print(sadrzaj)
"""