import urllib.request
import urllib.parse

link_yt = 'https://www.youtube.com/watch?v=EuC-yVzHhMI&t=5m56s'     #cilj je dobiit ovaj url/link

podaci_video = {'v':'EuC-yVzHhMI', 't':'5m56s'}     # Podaci o videu koje nam je genrirao sustav i iz njih želimo stvoriti url i pristupiti
podaci_video_niz = urllib.parse.urlencode(podaci_video)
print(podaci_video_niz)

url_video = 'https://www.youtube.com/watch?'+podaci_video_niz
print(url_video)

respons = urllib.request.urlopen(url_video)
print(respons.code)

html_resp = respons.read().decode()
