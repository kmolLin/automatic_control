# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from core.digrams.diagramItem import DiagramItem

from widgets.Ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.createscence()
    
    def createscence(self):
        scene = QGraphicsScene(self)
        ccreate = DiagramItem(2)
        self.graphicsView.setScene(scene)
        scene.addItem(ccreate)
        greenBrush = QBrush(Qt.green)
        blueBrush = QBrush(Qt.green)
        outlinePen = QPen(Qt.green)
        outlinePen.setWidth(2)
        rectangle = scene.addRect(100, 0, 80, 100, outlinePen, blueBrush)
        a, b = 10, 20
        text = scene.addText("a^2+{b}", QFont("Aria", 20))
        text.setFlag(QGraphicsItem.ItemIsMovable)
        
    
    @pyqtSlot(int)
    def on_toolBox_currentChanged(self, index):
        """
        Slot documentation goes here.
        
        @param index DESCRIPTION
        @type int
        """
        # TODO: not implemented yet
        raise NotImplementedError
