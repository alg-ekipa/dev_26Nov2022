import urllib.request
import urllib.parse

link_yt = 'https://www.youtube.com/watch?v=EuC-yVzHhMI=5m56s' #cilj je dobiti ovaj url/link!

#podaci o videu koje nam je generirao sustav i iz njih želimo stvoriti url i pristupiti
podaci_video = {'v': 'EuC-yVzHhMI', 't': '5m56s'}
podaci_video_niz = urllib.parse.urlencode (podaci_video)
print (podaci_video_niz)

url_video = 'https://www.youtube.com/watch?' + podaci_video_niz
print (url_video)

response = urllib.request.urlopen(url_video)
print(response.code)

html_resp = response.read().decode()