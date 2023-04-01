import urllib.request

URL = 'https://www.algebra.hr' # Adresa koju želimo otvoriti

# Stvarmo objekt koji predstavlja konekciju prema toj adresi
konekcija = urllib.request.urlopen(URL)

# nad konekcijom ćemo zvati metodu read() - čitanje sadržaja stranice i odmah dekodiramo metodom decode()
# pročitano sspremamo u varijablu sadržaj
sadržaj = konekcija.read().decode()

print(sadržaj)