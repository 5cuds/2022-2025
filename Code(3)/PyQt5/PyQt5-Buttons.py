import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
import random


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.InitGUI()
        self.setGeometry(150, 200, 200, 200)
        # or | self.button = QPushButton("Don't Click Me!", self)

        self.label = QLabel("Hello World", self)
    
    def InitGUI(self):
        self.button = QPushButton("Don't Click Me!", self)
        self.button.setGeometry(100, 100, 250, 100)
        self.button.setStyleSheet("font-size: 30px;")
        self.button.clicked.connect(self.baby)
    
    def baby(self):
        # stopit = ["Pls stop", "really", "dude you \nshould stop", "STOP!!", "AMAMMAMAMdf"]
        # print("bals")
        # self.button.setText(random.choice(stopit))
        # self.button.setDisabled(True)
        self.label.setText("Goodbye World")




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())