import requests

url='https://www.algebra.hr'

resp=requests.get(url)

print(resp) #objekt klase Response koja se nalazi u modulu requests

print(resp.status_code) #kod odgovora na request(200,43,4040,...)
print(type(resp.content)) #sadržaj stranice -bytes
print() 

print(type(resp.headers)) #podaci o sadržaju i konekciji-dict
print()
print(type(resp.text)) #string


