from bs4 import BeautifulSoup


html_kod = '<p>Some<b>bad<i>HTML'

html_soup = BeautifulSoup(html_kod)

print(html_soup.prettify())  #sam zatvori tagove

print(html_soup.find(text='bad')) #trazi 'bad'

print(html_soup.p.b.i.text)   #skida tagove p,b,i i ostavlja samo text