import requests

url = 'https://algebra.hr'

resp=requests.get(url)

print(resp)             #
print(resp.status_code) #kod odgovara na request (200,400,404,...)
print(resp.content)     #
print(resp.headers)
print(resp.text)
