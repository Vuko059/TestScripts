from PyQT_Project import Program
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Main(QWidget):
    window = None

    def __init__(self, parent=None):
        super().__init__(parent)

        self.Start()

    def Start(self):
        Btngo = QPushButton("&Start", self)
        Btngo.clicked.connect(self.Go)
        self.resize(400, 300)
        self.move(300, 300)
        self.setWindowTitle('Start')
        self.show()

    def Go(self):
        global window
        window = Program()
        window.show()


if __name__ == '__main__':

    app1 = QApplication(sys.argv)
    okno = Main()
    sys.exit(app1.exec_())
