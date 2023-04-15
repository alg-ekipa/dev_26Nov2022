import urllib.request
import urllib.parse   #


link_yt = 'https://www.youtube.com/watch?v=EuC-yVzHhMI&t=5m56s'

#podatci o videu koji je generirao sustav i iz njih zeliomo stvoriti url i pristupiti
#podatci_video = {'v' : 'EuC-yVzHhMI', 't':'5m56s'}
podatci_video = {'v' : 'EuC-hMI', 't':'5m56s'}
podatci_video_niz = urllib.parse.urlencode(podatci_video)

print(podatci_video_niz)

url_video = 'https://www.youtube.com/watch?' + podatci_video_niz
print(url_video)

respons = urllib.request.urlopen(url_video)
print(respons.code)  #ispis coda

hrml_resp = respons.read().decode()