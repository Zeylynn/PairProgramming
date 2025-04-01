import api_handler as api
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLineEdit,
    QPushButton,
    QVBoxLayout
)

class FreeGamesGUI(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__api_handler = api.API_Handler()

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
window = FreeGamesGUI()
window.show()

# start the event loop
app.exec()