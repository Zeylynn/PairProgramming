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
                all_platforms = self.api_handler.get_platforms()
                for platform_entry in all_platforms:
                    print(f"{platform_entry}")
                
                platform = input("")
                self.api_handler.set_platform(platform)
                break
            except KeyboardInterrupt:
                break
            except:
                print("Fehler bei der Eingabe. Try again!")

    def run(self):
        self.getUserPlatform()
        self.api_handler.build()
        response = self.api_handler.call()
        if type(response) == dict and response.get("status") != None:
            print("Sorry no Giveaways available")
            return
        for entry in response:
            print("Titel:",(entry["title"]),"URL:",entry["open_giveaway_url"],"\n")

app = FreeGamesCLI()
app.run()

"""
class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # set the window title
        self.setWindowTitle('Qt Signals & Slots')

        # create a button widget and connect its clicked signal
        # to a method
        button = QPushButton('Click me')
        button.clicked.connect(self.button_clicked)

        # place the buton on window using a vertical box layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        layout.addWidget(button)

        # show the window
        self.show()

    def button_clicked(self):
        print('clicked')

# create the QApplication, ich brauch IMMER nur eine QApplication => das Objekt beinhaltet die Main Loop => Nur eine Loop
app = QApplication([])

# create the main window
window = MainWindow()
window.show()

# start the event loop
app.exec()
"""