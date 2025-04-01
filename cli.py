#import sys
import api_handler as api
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLineEdit,
    QPushButton,
    QVBoxLayout
)

class FreeGamesCLI():
    def __init__(self):
        self.api_handler = api.API_Handler()

    def getUserPlatform(self):
        while(True):
            try:
                print("Welche Platform möchtest du auswählen:")
                for platform_entry in self.api_handler.get_platforms():
                    print(f"{platform_entry}")
                
                platform = input("")
                self.api_handler.set_platform(platform)
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

        for entry in data:
            print("Titel:",(entry["title"]),"URL:",entry["open_giveaway_url"],"\n")

    def run(self):
        self.getUserPlatform()
        self.api_handler.build()
        response = self.api_handler.call()
        self.printResults(response)

app = FreeGamesCLI()
app.run()