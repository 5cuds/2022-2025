import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainClass(QMainWindow):

    def __init__(self):
        super.__init__()

        self.setWindowTitle("Nar's Cool window")
        self.setGeometry(50, 202, 500, 500)


def main():

    app = QApplication(sys.argv)
    main_window = QMainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()