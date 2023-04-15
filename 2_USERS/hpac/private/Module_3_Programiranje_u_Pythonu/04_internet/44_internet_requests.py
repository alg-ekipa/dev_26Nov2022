import requests
import urllib.request
import urllib.parse


url = 'https://www.algebra.hr'

resp = requests.get(url)

print(resp)          # objekt klase Response koja se nalazi u modulu requests
print()
print(resp.status_code)      # kod odgovora na request(200, 403, 404, ...)
print()
print(resp.content)      # sadrćaj stranice - bytes
print()
print(resp.headers)       # podaci o stranici i konekciji -  rječnik
print()
print(resp.text)      # string




'''
podaci_video = {'v':'x4maoo4A3x4', 't':'3m50s'} 
podaci_video_niz = urllib.parse.urlencode(podaci_video)
print(podaci_video_niz)

url_video = 'https://www.youtube.com/watch?'+podaci_video_niz
print(url_video)
'''