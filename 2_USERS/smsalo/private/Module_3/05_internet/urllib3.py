import urllib.request
import urllib.parse

podaci_video = {'v':'x4maoo4A3x4'}
podaci_video_niz=urllib.parse.urlencode(podaci_video)

print(podaci_video_niz)
url_video = 'https://youtube.com/watch?' + podaci_video_niz
print(url_video)
respons = urllib.request.urlopen(url_video)
print(respons.code)
htmp_resp= respons.read().decode()

