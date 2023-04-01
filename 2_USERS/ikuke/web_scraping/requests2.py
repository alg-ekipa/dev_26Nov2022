import requests
import json

url= ' https://bug.hr'

resp=requests.get(url)

print(resp.status_code)

sadrzaj=resp.content
sadrzaj_dekodiran=sadrzaj.decode('utf-8')

print(sadrzaj_dekodiran)


try:
    with open('bugweb.json', 'w')as file_writer:
        json.dump(sadrzaj_dekodiran, file_writer)

except Exception as e:
    print('doslo je do pogreske', e)