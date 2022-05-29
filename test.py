import requests

BASE = "http://127.0.0.1:5000/"

data = [{"name":"name","singer":1,"album":1},{"name":"name","singer":1,"album":1},{"name":"name","singer":1,"album":1}]
data = [{"name":"bladee"}]
data = [{"name":"AAAAAAAAAAAAAAAA","singer":2}]

response = requests.get(BASE + "singer/"+str(3) )
#response = requests.post(BASE + "postSinger/",data[0] )
#response = requests.post(BASE + "postAlbum/",data[0])
response = requests.get(BASE + "album/"+str(5) )
print(response.json())


#for i in range(len(data)):
#    response = requests.put(BASE + "singer/" + str(i), data[i])
#    print(response.json())


