import urllib.request

URL='https://www.algebra.hr' #adresa koju želimo otvoriti


#stavarmo objekt koji predstavlja konekciju prema toj adresi
konekcija=urllib.request.urlopen(URL)

#nad konekcijom ćemo zvati medtodu read()-čitanje sadržaja stranice i odmah dekodiramo metodom decode()
#pročitamo spremamo u varijablu sadržaj
sadrzaj=konekcija.read().decode()

print(sadrzaj)