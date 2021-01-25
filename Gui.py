import win32gui as win32
import pandas as pd
from pywinauto import Desktop
from PyQt5.QtWidgets import QMainWindow,QHBoxLayout,QApplication,QWidget,QVBoxLayout,QPushButton
from Focuse import Focus
from Active import Active
from Clock import Clock
from PieChart import PieChart
from Spy import Spy
import sys
import threading


class MainWindow(QMainWindow):
    focusName = ['Youtube', 'Music', 'Teams', 'Stack', 'Python']
    focusTime = ['00:00:00','00:00:00','00:00:00','00:00:00','00:00:00']
    activeName = ['Spotify','Python','TeamSpeak','Word','Excel']
    activeTime = ['00:00:00', '00:00:00', '00:00:00', '00:00:00', '00:00:00']
    focusPieName = ['Youtube', 'Music', 'Teams', 'Stack', 'Python','Other']
    focusPieTime = [1,2,3,4,5,10]
    activePieName = ['Spotify', 'Python', 'TeamSpeak', 'Word', 'Excel','Other']
    activePieTime = [2,2,2,2,2,5]
    layout = QVBoxLayout()

    def __init__(self,*args,**kwargs):
        super(MainWindow, self).__init__(*args,**kwargs)
        self.setWindowTitle("Self Spy")
        self.spy = 0
        self.resize(900,700)

        self.clock = Clock()
        self.layout.addWidget(self.clock)

        self.focusLayout = Focus(self.focusName,self.focusTime)
        self.activeLayout = Active(self.activeName,self.activeTime)

        self.focusChart = PieChart()
        self.activeChart = PieChart()

        self.pieLayout = QVBoxLayout()
        self.pieLayout.addWidget(self.focusChart)
        self.pieLayout.addWidget(self.activeChart)

        self.middleLayout = QHBoxLayout()
        self.middleLayout.addLayout(self.focusLayout)
        self.middleLayout.addLayout(self.activeLayout)
        self.middleLayout.addLayout(self.pieLayout)

        self.layout.addLayout(self.middleLayout)

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

    def closeEvent(self, event):
        self.clock.running = False

    def updateCharts(self, focusPath, activePath):
        self.focusChart.chartUpdate(focusPath)
        self.activeChart.chartUpdate(activePath)

    def initSpy(self):
        print("I started")
        self.spy = Spy(self)

    def updateWindow(self):
        print("Odebrałem paczke danych")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    clockThread = threading.Thread(target=window.clock.startClock, args=())
    spyThread = threading.Thread(target=window.initSpy, args=())
    clockThread.start()
    spyThread.start()
    sys.exit(app.exec_())
