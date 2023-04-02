import urllib.request

URL= 'https://www.algebra.hr' #adresa koju želimo otvoriti


#stvaramo objekt koji predstavlja konekciju prema toj adresi

konekcija = urllib.request.urlopen(URL)

#nad konekcijom ćemo zvati metodu read()-čitanje sadržaja stranice i odmah dekodiramo metodom decode()
#pročitano spremamo u varijablu sadržaj
sadrzaj=konekcija.read().decode()
print(sadrzaj)