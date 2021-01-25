import sys
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QApplication, QHBoxLayout


class Active(QVBoxLayout):
    app = QApplication(sys.argv)
    labels = [QLabel(""),QLabel(""),QLabel(""),QLabel(""),QLabel("")]
    numberlabels = [QLabel("1"),QLabel("2"),QLabel("3"),QLabel("4"),QLabel("5")]
    time = [QLabel(""),QLabel(""),QLabel(""),QLabel(""),QLabel("")]

    def __init__(self,list,time,*args,**kwargs):
        super(Active, self).__init__(*args,**kwargs)
        i=0
        Hl1 = QHBoxLayout()
        self.addWidget(QLabel("Time Active"))
        for lab in self.labels:
            lab.setText(list[i])
            self.time[i].setText(time[i])
            Hl1.addWidget(self.numberlabels[i])
            Hl1.addWidget(lab)
            Hl1.addWidget(self.time[i])
            self.addLayout(Hl1)
            Hl1 = QHBoxLayout()
            i += 1



    def updateContent(self,name,time):

        i=0
        for lab in self.labels:
            lab.setText(name[i])
            i += 1

        i=0
        for t in self.time:
            t.setText(time[i])
            i += 1
