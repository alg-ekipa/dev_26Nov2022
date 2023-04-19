import urllib.request
import urllib.parse 

link_yt = 'https://www.youtube.com/watch?v=EuC-yVzHhMI&t=5m56s' #linkovi u word fajlu na cloudu

podaci_video = {'v' : 'EuC-yVzHhMI', 't' : '5m56s'} #podaci iz videa koji nam je generirao sustav i iz njih želimo generirati url i pristupiti linku

# iz podataka koji je riječnik ćemo napraviti niz

podaci_video_niz = urllib.parse.urlencode(podaci_video)

print(podaci_video_niz)

url_video = 'https://www.youtube.com/watch?' + podaci_video_niz
print(url_video)

# kad smo ga dobili probamo doći do njega

rspns = urllib.request.urlopen(url_video)

print(rspns.code) #

html_rspns = rspns.read().decode()


