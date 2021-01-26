import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QApplication, QHBoxLayout
from time import sleep
from PyQt5.Qt import Qt


class Focus(QVBoxLayout):
    app = QApplication(sys.argv)
    labels = [QLabel(""),QLabel(""),QLabel(""),QLabel(""),QLabel("")]
    numberlabels = [QLabel("1"),QLabel("2"),QLabel("3"),QLabel("4"),QLabel("5")]
    time = [QLabel(""),QLabel(""),QLabel(""),QLabel(""),QLabel("")]

    def __init__(self,list,time,*args,**kwargs):
        super(Focus, self).__init__(*args,**kwargs)
        i=0
        self.font = QFont("Time New Roman", 14)
        self.lfont = QFont("Time New Roman", 22)
        Hl1 = QHBoxLayout()
        focus = QLabel("Time Focused")
        focus.setAlignment(Qt.AlignCenter)
        focus.setStyleSheet("background-color: #DC7633 ;border: 1px solid black;border-radius: 10px;")
        focus.setFont(self.lfont)
        style = "color: black; background-color: #F5CBA7 ;border: 1px solid #C0392B;border-radius: 10px;"
        self.addWidget(focus)
        for lab in self.labels:
            lab.setFont(self.font)
            # lab.setStyleSheet("background-color: #BFB8B6;border: 1px solid black;border-radius: 10px;")
            lab.setStyleSheet(style)
            lab.setAlignment(Qt.AlignCenter)
            self.time[i].setFont(self.font)
            self.time[i].setStyleSheet(style)
            self.time[i].setAlignment(Qt.AlignCenter)
            lab.setText(list[i])
            self.time[i].setText(time[i])
            Hl1.addWidget(self.numberlabels[i])
            Hl1.addWidget(lab)
            Hl1.addWidget(self.time[i])
            self.addLayout(Hl1)
            Hl1 = QHBoxLayout()
            i += 1
        for lab in self.numberlabels:
            lab.setFont(self.font)
            lab.setAlignment(Qt.AlignCenter)
            lab.setStyleSheet(style)


    def updateName(self,name):
        i = 0
        for lab in self.labels:
            lab.setText(name[i])
            i += 1
            sleep(0.4)

    def updateTime(self,time):
        i = 0
        for t in self.time:
            t.setText(time[i])
            i += 1
            sleep(0.4)