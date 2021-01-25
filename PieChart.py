from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel


class PieChart(QLabel):
    chartImage = "abc.jpg"

    def __init__(self,*args,**kwargs):
        super(PieChart, self).__init__(*args,**kwargs)
        pixmap = QPixmap(self.chartImage)
        pixmap = pixmap.scaled(400,400,Qt.KeepAspectRatio)
        self.setPixmap(pixmap)


    def chartUpdate(self,path):
        self.chartImage = path
        pixmap = QPixmap(self.chartImage)
        pixmap = pixmap.scaled(400,400,Qt.KeepAspectRatio)
        self.setPixmap(pixmap)





