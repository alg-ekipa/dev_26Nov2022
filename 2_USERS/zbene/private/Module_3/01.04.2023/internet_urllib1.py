import urllib.request

URL = 'https://www.algebra.hr' #adresa koju želimo otvoriti

#stvaramo objekt koji predstavlja konekciju prema toj adresi
konekcija = urllib.request.urlopen(URL)

#nad konekcijom ćemo zvati metodu read() - čitanje sadržaja stranice i odmah dekodiramo decode()
#pročitano spremamo u varijablu sadržaj
sadržaj = konekcija.read().decode()

print(sadržaj)