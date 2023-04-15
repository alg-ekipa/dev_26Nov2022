import urllib.request

#adresa koju želimo otvoriti
URL = 'https://www.algebra.hr'  #definiramo varijablu kao URL, i u string dodajemo web adresu

#stvaramo obijekt koji stvara konekciju, zato smo ga tako nazvali
konekcija = urllib.request.urlopen(URL) # Mogli smo i direktno pisati string unutar argumenta


#nad "konekcijom" ce mo zvati motodu read() - citanje sadrzaja stranice 
#i odmah dekodiramo metodom decode()
#procitano spremamo u varijablu "sadrzaj"
sadrzaj = konekcija.read().decode()

print(sadrzaj) #dobijemo buckuriš HTML-a
