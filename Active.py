import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QApplication, QHBoxLayout
from time import sleep

class Active(QVBoxLayout):
    app = QApplication(sys.argv)
    labels = [QLabel(""),QLabel(""),QLabel(""),QLabel(""),QLabel("")]
    numberlabels = [QLabel("1"),QLabel("2"),QLabel("3"),QLabel("4"),QLabel("5")]
    time = [QLabel(""),QLabel(""),QLabel(""),QLabel(""),QLabel("")]

    def __init__(self,list,time,*args,**kwargs):
        super(Active, self).__init__(*args,**kwargs)
        i=0
        Hl1 = QHBoxLayout()
        self.font = QFont("Time New Roman", 14)
        activity = QLabel("Time Active")
        activity.setFont(self.font)
        self.addWidget(activity)
        for lab in self.labels:
            lab.setFont(self.font)
            self.time[i].setFont(self.font)
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
