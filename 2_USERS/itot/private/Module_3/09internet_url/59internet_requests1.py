import requests

url = 'https://www.algebra.hr'

resp = requests.get(url)
print(resp) # INT #objekt klase Response koja se nalazi u modelu requests

#print(resp.status_code) # kod odgovora request (200, 403, 404...)
print() 
print(resp.content)    # sadrzaj starnice - bytes
print()  
print(resp.headers)   # pdoatci o stranici - rijecnik
print()
print(resp.text)  #string  # 

