import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
#from run import *

#///////libraries///////libraries///////libraries///////libraries////////

class Program(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.Window()
#////////////////////////////////////////////////////////////////////////

#////////////////////////////////////////////////////////////////////////
    def Window(self):

        msg = "TEST.Window"

        ukladT = QGridLayout()

        self.napis1Edt = QLineEdit()
        self.napis2Edt = QLineEdit()

        msg1 = QLabel(msg)

        BtnUp = QPushButton("&^", self)
        BtnLeft = QPushButton("&<", self)
        BtnRight = QPushButton("&>", self)
        BtnDo = QPushButton("&Done", self)
        BtnUp.clicked.connect(self.up)
        BtnLeft.clicked.connect(self.left)
        BtnRight.clicked.connect(self.right)
        BtnDo.clicked.connect(self.do)

        self.napis1Edt.setReadOnly(True)
        ukladT.addWidget(self.napis1Edt, 1, 1, 2, 3)
        ukladT.addWidget(BtnUp, 2, 2)
        ukladT.addWidget(BtnRight, 2, 3)
        ukladT.addWidget(BtnLeft, 2, 1)
        ukladT.addWidget(self.napis2Edt, 3, 1, 2, 2)
        ukladT.addWidget(BtnDo, 3, 3, 2, 3)
        ukladT.addWidget(msg1, 0, 1)
        self.setLayout(ukladT)
        self.resize(400, 300)
        self.move(300, 300)
        self.setWindowTitle('Okno')
        self.show()
#////////////////////////////////////////////////////////////////////////

#////////////////////////////////////////////////////////////////////////
    def up(self):

        self.napis1Edt.setText("Up")

#////////////////////////////////////////////////////////////////////////

#////////////////////////////////////////////////////////////////////////
    def left(self):
        self.napis1Edt.setText("Left")

#////////////////////////////////////////////////////////////////////////

#////////////////////////////////////////////////////////////////////////
    def right(self):
        self.napis1Edt.setText("Right")

#////////////////////////////////////////////////////////////////////////

#////////////////////////////////////////////////////////////////////////
    def do(self):
        pass
#////////////////////////////////////////////////////////////////////////

#////////////////////////////////////////////////////////////////////////
if __name__ == '__main__':

    app = QApplication(sys.argv)
    okno = Program()
    sys.exit(app.exec_())
#exit()
