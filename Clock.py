from PyQt5.QtWidgets import QWidget, QLabel
from time import sleep
from PyQt5.Qt import Qt

class Clock(QLabel):

    def __init__(self,*args,**kwargs):
        super(Clock, self).__init__(*args,**kwargs)
        self.setText("00:00:00")
        self.setAlignment(Qt.AlignCenter)
        font = self.font()
        font.setPointSize(50)
        self.setFont(font)
        self.setStyleSheet("background-color: #CADAC4  ;border: 1px solid black;border-radius: 10px;")

    def setClock(self,time):
        self.setText(time)
