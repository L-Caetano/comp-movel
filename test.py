import requests

BASE = "http://127.0.0.1:5000/"

data1 = [{"name":"Bladee"}]
data2 = [{"name":"Working on dying", "singer":1}]
data3 = [{"name":"Redlight Moments","album":2}]


#response = requests.post(BASE + "postSinger/",data1[0] )
#print(response.json())
#response = requests.post(BASE + "postAlbum/",data2[0])
#print(response.json())
#response = requests.post(BASE + "postSong/",data3[0])
#print(response.json())
#response = requests.get(BASE + "album/"+str(2) )
#print(response.json())
#response = requests.get(BASE + "singer/"+str(1) )
#print(response.json())
response = requests.get(BASE + "song/"+str(1) )

print(response.json())


#for i in range(len(data)):
#    response = requests.put(BASE + "singer/" + str(i), data[i])
#    print(response.json())


