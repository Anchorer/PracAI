import urllib

url = "https://raw.githubusercontent.com/GokuMohandas/practicalAI/master/data/titanic.csv"
response = urllib.request.urlopen(url)
http = response.read()
with open('titanic.csv', 'wb') as f:
    f.write(http)



