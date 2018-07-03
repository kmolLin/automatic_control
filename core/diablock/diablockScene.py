# DiablockScene

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from .diablockItem import DiablockItem


class DiablockScene(QGraphicsScene):
    
    InsertItem, InsertLine, InsertText, MoveItem  = range(4)

    itemInserted = pyqtSignal(DiablockItem)

    textInserted = pyqtSignal(QGraphicsTextItem)

    itemSelected = pyqtSignal(QGraphicsItem)

    def __init__(self, itemMenu, parent=None):
        super(DiablockScene, self).__init__(parent)

        self.myItemMenu = itemMenu
        self.myMode = self.MoveItem
        self.myItemType = DiablockItem.Step
        self.line = None
        self.textItem = None
        self.myItemColor = Qt.white
        self.myTextColor = Qt.black
        self.myLineColor = Qt.black
        self.myFont = QFont()

    def setLineColor(self, color):
        self.myLineColor = color
        if self.isItemChange(Arrow):
            item = self.selectedItems()[0]
            item.setColor(self.myLineColor)
            self.update()

    def setTextColor(self, color):
        self.myTextColor = color
        if self.isItemChange(DiagramTextItem):
            item = self.selectedItems()[0]
            item.setDefaultTextColor(self.myTextColor)

    def setItemColor(self, color):
        self.myItemColor = color
        if self.isItemChange(DiagramItem):
            item = self.selectedItems()[0]
            item.setBrush(self.myItemColor)

    def setFont(self, font):
        self.myFont = font
        if self.isItemChange(DiagramTextItem):
            item = self.selectedItems()[0]
            item.setFont(self.myFont)

    def setMode(self, mode):
        self.myMode = mode
        
    def createblock(self):
        item = DiablockItem(self.myItemType)
        item.setPos(QPointF(0, 0))
        self.addItem(item)
        self.itemInserted.emit(item)

    def setItemType(self, type):
        self.myItemType = type
        print(type)

    def editorLostFocus(self, item):
        cursor = item.textCursor()
        cursor.clearSelection()
        item.setTextCursor(cursor)

        if item.toPlainText():
            self.removeItem(item)
            item.deleteLater()
