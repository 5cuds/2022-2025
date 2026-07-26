import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QCheckBox
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.box = QCheckBox("SUIIII", self)
        self.initGUI()

    def initGUI(self):
        self.box.setGeometry(10, 0, 500, 100)
        self.box.setStyleSheet("font-size: 30px;"
                            "font-family: arial;")
        self.box.stateChanged.connect(self.pront)

    def pront(self, slate):
        if slate == 2:
            print("SUIIII")
        else:
            print("aww damn")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

