import requests 

url = 'https://www.algebra.hr'

resp = requests.get(url)   # getanje ili povlačenje sadržaja - int

print(resp.status_code)    # kod odgovara na request (200, 403, 404 ...) 
print(type(resp.content))  # sadržaj stranice - bytes
print()
print(resp.headers)        # metapodaci o sadržaju i konekciji - dict
print()
print(type(resp.text))     # string 


''' još uvjek nismo došli do točnih podataka koji nam trebaju. 
Sad eventualno možemo to splitati itd ali moramo pronaći način kako doći do njih. 
Možda po tagu p, možda po nečemu iz CSSa'''