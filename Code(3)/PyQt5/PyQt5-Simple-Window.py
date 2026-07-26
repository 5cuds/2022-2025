import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My First GUI PyQt5!") # Windows title

        self.setGeometry(0, 0, 500, 500) # (x, y, width, height)

        self.setWindowIcon(QIcon("images/haze.png")) # Icon for the window.

        label = QLabel("Hello world", self) # prints "Hello World" to the window.

        label.setFont(QFont("Comic sans", 30)) # Adds Font to the text and makes it bigger!

        label.setGeometry(0, 0, 600, 100)

        label.setStyleSheet(
            "color: white;"         
            "background-color: #0f97d1;"
            "font-weight: Bold;"
            # "font-style: italic;"
            "text-decoration: underline;"
        )

        # label.setAlignment(Qt.AlignTop)
        # label.setAlignment(Qt.AlignBottom)
        # label.setAlignment(Qt.AlignVCenter)
        # label.setAlignment(Qt.AlignHCenter)
        # label.setAlignment(Qt.AlignRight)
        label.setAlignment(Qt.AlignVCenter | Qt.AlignTop)


def main():

    app = QApplication(sys.argv) # Painful step to make a Simple window.
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()