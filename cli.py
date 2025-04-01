import api_handler as api

class FreeGamesCLI():
    def __init__(self):
        self.__api_handler = api.API_Handler()

    def getUserPlatform(self):
        while(True):
            try:
                print("Welche Platform möchtest du auswählen:")
                for platform_entry in self.__api_handler.get_platforms():
                    print(f"{platform_entry}")
                
                platform = input("")
                self.__api_handler.set_platform(platform)
                break
            except KeyboardInterrupt:
                break
            except:
                print("Fehler bei der Eingabe. Try again!")

    def printResults(self, data):
        if type(data) == dict:
            if "No active giveaways" in data["status_message"]:
                print("Zurzeit kein Giveaway verfügbar!")
                return

        print(f"{len(data)} Einträge gefunden")
        for entry in data:
            print(f"Titel:{entry["title"]}\nURL:{entry["open_giveaway_url"]}\n")

    def run(self):
        self.getUserPlatform()
        self.__api_handler.build()
        self.printResults(self.__api_handler.call())

app = FreeGamesCLI()
app.run()