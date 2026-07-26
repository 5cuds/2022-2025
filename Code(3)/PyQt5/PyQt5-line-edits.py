import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QLineEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.entry = QLineEdit(self)

        self.initGU()

        def initGU(self):
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())