import requests

BASE = "http://127.0.0.1:5000/"

data = [{"name":"name","singer":1,"album":1},{"name":"name","singer":1,"album":1},{"name":"name","singer":1,"album":1}]
data = [{"name":"ppgcasper"}]

response = requests.get(BASE + "singer/" + str(0))
print(response.json())


#for i in range(len(data)):
#    response = requests.put(BASE + "singer/" + str(i), data[i])
#    print(response.json())


