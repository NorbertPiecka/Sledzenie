import sys
import threading
import warnings
warnings.simplefilter("ignore", UserWarning)
sys.coinit_flags = 2
from pywinauto import Desktop
from PyQt5.QtWidgets import QMainWindow,QHBoxLayout,QApplication,QWidget,QVBoxLayout,QPushButton
from Focuse import Focus
from Active import Active
from Clock import Clock
from PieChart import PieChart
from Spy import Spy
from time import sleep
import sys
import threading


class MainWindow(QMainWindow):
    focusName = ['-', '-', '-', '-', '-']
    focusTime = ['00:00:00','00:00:00','00:00:00','00:00:00','00:00:00']
    activeName = ['-','-','-','-','-']
    activeTime = ['00:00:00', '00:00:00', '00:00:00', '00:00:00', '00:00:00']
    layout = QVBoxLayout()

    def __init__(self,*args,**kwargs):
        super(MainWindow, self).__init__(*args,**kwargs)
        self.setWindowTitle("Self Spy")
        self.spy = 0
        self.resize(900,700)

        self.highGroundLayout = QHBoxLayout()

        self.clock = Clock()
        self.focusChart = PieChart()

        self.highGroundLayout.addWidget(self.clock)
        self.highGroundLayout.addWidget(self.focusChart)

        self.focusLayout = Focus(self.focusName,self.focusTime)
        self.activeLayout = Active(self.activeName,self.activeTime)

        self.middleLayout = QHBoxLayout()
        self.middleLayout.addLayout(self.focusLayout)
        self.middleLayout.addLayout(self.activeLayout)

        self.layout.addLayout(self.highGroundLayout)
        self.layout.addLayout(self.middleLayout)

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

    def closeEvent(self, event):
        self.clock.running = False

    def initSpy(self):
        print("I started")
        self.spy = Spy(self)

    def updateWindow(self,focusName,focusTime,activeName,activeTime,focusPath):
        self.focusLayout.updateName(focusName)
        sleep(0.5)
        self.focusLayout.updateTime(focusTime)
        sleep(0.5)
        self.activeLayout.updateName(activeName)
        sleep(0.5)
        self.activeLayout.updateTime(activeTime)
        sleep(1.25)
        self.focusChart.chartUpdate(focusPath)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    clockThread = threading.Thread(target=window.clock.startClock, args=())
    spyThread = threading.Thread(target=window.initSpy, args=())
    clockThread.start()
    spyThread.start()
    sys.exit(app.exec_())
