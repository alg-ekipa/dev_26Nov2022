import urllib.request
import urllib.parse

link_yt='https://youtube.com/watch?v=EuC-yVzHhMI&t=5m56s'  #cilj je dobiti ovaj url/link

#podaci o videu koe nam je generirao sustav i iz njih želimo stvoriti url i pristupiti
podaci_video={'v':'x4maoo4A3x4', 't':'5m56s'}
podaci_video_niz=urllib.parse.urlencode(podaci_video)

print(podaci_video_niz)

url_video='https://youtube.com/watch?'+podaci_video_niz
print(url_video)

respons=urllib.request.urlopen(url_video)
print(respons.code)

html_resp=respons.read().decode()
