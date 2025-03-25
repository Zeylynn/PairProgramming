import requests as req
# https://github.com/Zeylynn/PairProgramming.git

class FreeGames():
    """
    TO DO LATER: ANZAHL AN EINTRÄGEN(MIT FUNKTION)
    FUNKTIONEN DOKUMENTIEREN
    FILTER FÜR ALLE PLATFORMEN
    STANDARDWERT FÜR KONSTRUKTOR
    """
    def __init__(self, apiurl):
        self.api_url = apiurl
        # STANDARTWERTE??
        self.platform = "pc"

        # DICTIONARY
        self.platformList = {1: "pc", 2: "android"}

    def getData(self):
        return req.get(self.api_url).json()

    def setPlatform(self, platform):
        self.platform = platform

    def getPlatformFromUser(self):
        while(True):
            try:
                platform = int(input("Auf welcher Platform sollen die Spiele gespielt werden\n1) PC\n2) Android\n"))

                self.setPlatform(self.platformList[platform])
                break
            except KeyboardInterrupt:
                break
            except:
                print("Fehler bei der Eingabe. Try again!")

    def updateAPI(self):
        self.api_url = self.api_url + f"?platform={self.platform}"

    def printResults(self, data):
        for entry in data:
            print("Titel:",(entry["title"]),"URL:",entry["open_giveaway_url"],"\n")

    def run(self):
        self.getPlatformFromUser()
        self.updateAPI()
        data = self.getData()
        self.printResults(data)

base_url = "https://www.gamerpower.com/api/giveaways"

myProgramm = FreeGames(base_url)
myProgramm.run()