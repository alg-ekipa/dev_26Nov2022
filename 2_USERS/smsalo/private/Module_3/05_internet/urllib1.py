import urllib.request

URL='https://www.algebra.hr'        #adresa koju zelimo otvoriti

konekcija = urllib.request.urlopen(URL)  #objekt koji predstavlja konekciju prema toj adresi

#nad konekcijom ćemo zvati naredbu read() - čitanje sadržaja stranice i odmah dekodiamo metodom decode

sadrzaj = konekcija.read().decode()

print(sadrzaj)
