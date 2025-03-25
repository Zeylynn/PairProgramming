# https://github.com/Zeylynn/PairProgramming.git

import requests as req

def getAPI(url):
    return req.get(url).json()

url = "https://www.gamerpower.com/api/giveaways"

data = getAPI(url)

# Platform Input
while(True):
    try:
        platform = input("Auf welcher Platform sollen die Spiele gespielt werden\n1) PC\n2) Android\n3) XBox\n4) Playstation\n5) Nintendo Switch\n")

        match platform:
            case "1": platform = "PC"; break
            case "2": platform = "Android"; break
            case "3": platform = "Xbox"; break
            case "4": platform = "Playstation"; break
            case "5": platform = "Switch"; break
    except KeyboardInterrupt:
        break
    except:
        pass

j = 0
for i in data:
    if platform in i["platforms"]:
        print("Titel:",(i["title"]),"URL:",i["open_giveaway_url"],"\n")
        j += 1

print(f"Anzahl der gefundenen Beiträge: {j}")