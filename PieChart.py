from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel
from time import sleep


class PieChart(QLabel):
    chartImage = "temp.jpg"

    def __init__(self,*args,**kwargs):
        super(PieChart, self).__init__(*args,**kwargs)
        pixmap = QPixmap(self.chartImage)
        pixmap = pixmap.scaled(500,500,Qt.KeepAspectRatio)
        self.setPixmap(pixmap)
        self.setAlignment(Qt.AlignCenter)


    def chartUpdate(self,path):
        sleep(1.5)
        self.chartImage = path
        pixmap = QPixmap(self.chartImage)
        pixmap = pixmap.scaled(500,500,Qt.KeepAspectRatio)
        self.setPixmap(pixmap)





