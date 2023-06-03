import requests
import urllib.request
import urllib.parse

url = 'https://www.algebra.hr'

resp = requests.get(url)

print (resp) #objekt klase Response koja se nalazi u modulu requests

print (type(resp.status_code)) #kod odgovara na request (200, 403, 404 ...) - int
print (type (resp.content)) # sadraj stranice - bytes
print()
print (resp.headers) #podaci o sadržaju i konekciji - dict 
print()
print (resp.text) #string

podaci_video = {'x4maoo4A3x4', 't', '5m03s'}
podaci_video_niz = urllib.parse.urlencode (podaci_video)
print (podaci_video_niz)

url_video = 'https//www.youtube.com.watch?' + podaci_video_niz
print (url_video)