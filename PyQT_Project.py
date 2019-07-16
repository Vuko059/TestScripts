import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Rooms import room
#///////libraries///////libraries///////libraries///////libraries////////

nick = " YOU "

class Main(QWidget):
    window = None

    def __init__(self, parent=None):
        super().__init__(parent)

        self.Start()

    def Start(self):
        Btngo = QPushButton("&Start", self)
        Btngo.clicked.connect(self.tt)
        self.resize(400, 300)
        self.move(300, 300)
        self.setWindowTitle('Start')
        self.show()



    def tt(self):
        global window
        window = Program()
        window.show()
        self.close()

#////////////////////////////////////////////////////////////////////////

#////////////////////////////////////////////////////////////////////////


class Program(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.Window()
#////////////////////////////////////////////////////////////////////////

#////////////////////////////////////////////////////////////////////////
    def Window(self):

        msg = " Window "

        ukladT = QGridLayout()

        self.napis1Edt = QLineEdit()
        self.napis1Edt.setFixedSize(300, 100)
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
        ukladT.addWidget(BtnUp, 3, 2)
        ukladT.addWidget(BtnRight, 3, 3)
        ukladT.addWidget(BtnLeft, 3, 1)
        ukladT.addWidget(self.napis2Edt, 4, 1, 2, 2)
        ukladT.addWidget(BtnDo, 4, 3, 2, 1)
        ukladT.addWidget(msg1, 0, 1, 1, 3)
        self.setLayout(ukladT)
        ukladH = QHBoxLayout()
        ukladT.addLayout(ukladH, 2, 0, 1, 4)
        self.setFixedSize(400, 300)
        self.move(300, 300)
        self.setWindowTitle('Adventure')
        self.show()
#////////////////////////////////////////////////////////////////////////
    
#////////////////////////////////////////////////////////////////////////


    def up(self):

        self.napis1Edt.setText(room.zone1())

        self.napis1Edt.setText(room.zone2())
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
    okno = Main()
    sys.exit(app.exec_())
