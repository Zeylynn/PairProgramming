import requests as req

def NetGagget(url):
    data = req.get(url).json()
    return data

url = "https://www.gamerpower.com/api/giveaways"

Dictionary = NetGagget(url)

lauf = 0
for i in Dictionary:
    print("Titel:",(i["title"]),"URL:",i["open_giveaway_url"],"\n")
    lauf+=1
    
print("")
print(lauf)