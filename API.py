import requests as req
# GitHub Link: https://github.com/Zeylynn/PairProgramming.git

class FreeGames():
    """
    TO DO LATER: 
    Funktionen dokumentieren
    Funktionen einheitlich benennen:
        set für self. setzen
        get für return
        print für print lol
    Nachdenken wann self.set und wann Variablen verwendet werden
    GitLense zu GitHub connecten
    GitLense anschauen
    """
    def __init__(self, api_url=""):
        self.api_url = api_url
        self.platformList = {0: "",
                             1: "?platform=pc",
                             2: "?platform=android",
                             3: "?platform=xbox-one&xbox-series&xs,xbox-360",
                             4: "?platform=ps4&ps5",
                             5: "?platform=switch"}

    def getData(self, url):
        return req.get(url).json()

    def setPlatform(self, platform):
        self.platform = platform

    def setPlatformFromUser(self):
        while(True):
            try:
                platform = int(input("Nach welcher Platform soll gefiltert werden:\n0) Alle anzeigen\n1) PC\n2) Android\n3) XBox\n4) Playstation\n5) Nintendo Switch\n"))

                self.setPlatform(self.platformList[platform])
                break
            except KeyboardInterrupt:
                break
            except:
                print("Fehler bei der Eingabe. Try again!")

    def updateFilteredApiUrl(self):
        self.filteredURL = self.api_url + self.platform

    def printResults(self, data):
        print(f"Einträge gefunden: {self.getAmountOfEntries()}")
        for entry in data:
            print("Titel:",(entry["title"]),"URL:",entry["open_giveaway_url"],"\n")

    def getAmountOfEntries(self):
        return len(self.getData(self.filteredURL))

    def run(self):
        self.setPlatformFromUser()
        self.updateFilteredApiUrl()
        data = self.getData(self.filteredURL)
        self.printResults(data)

base_url = "https://www.gamerpower.com/api/giveaways"

myProgramm = FreeGames(base_url)
myProgramm.run()