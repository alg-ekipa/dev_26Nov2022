from bs4 import BeautifulSoup

html_kod= '<p>Some<b>bad<i>HTML'

html_soup=BeautifulSoup(html_kod)

print(html_soup.prettify())


print(html_soup.find(text='bad'))
print(html_soup.i)
print(html_soup.p)
print(html_soup.p.b.i.text)     #ukloni sve ><p, b,.... i ostane samo text između njih

