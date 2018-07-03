# Diablock
from PyQt5.QtCore import (pyqtSignal, QLineF, QPointF, QRect, QRectF, QSize,
        QSizeF, Qt)
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsPolygonItem
from PyQt5.QtGui import (QPainterPath,QPixmap, QPolygonF, QPainter, QPen)

# draw the block and signal process event

class DiablockItem(QGraphicsPolygonItem):
    Step, Conditional, StartEnd, Io = range(4)
    def __init__(self, diagramType, parent=None):
        super(DiablockItem, self).__init__(parent)
        
        self.diagramType = diagramType
        #self.contextMenu = contextMenu
        
        path = QPainterPath()
        if self.diagramType == self.StartEnd:
            path.moveTo(200, 50)
            path.arcTo(150, 0, 50, 50, 0, 90)
            path.arcTo(50, 0, 50, 50, 90, 90)
            path.arcTo(50, 50, 50, 50, 180, 90)
            path.arcTo(150, 50, 50, 50, 270, 90)
            path.lineTo(200, 25)
            self.myPolygon = path.toFillPolygon()
        elif self.diagramType == self.Conditional:
            self.myPolygon = QPolygonF([
                    QPointF(-45, 45), QPointF(45, 45),
                    QPointF(45, 45), QPointF(45, -45),
                    QPointF(-45, 45)])
        elif self.diagramType == self.Step:
            self.myPolygon = QPolygonF([
                    QPointF(-45, -45), QPointF(45, -45),
                    QPointF(45, 45), QPointF(-45, 45),
                    QPointF(-45, -45)])
        else:
            self.myPolygon = QPolygonF([
                    QPointF(-120, -80), QPointF(-70, 80),
                    QPointF(120, 80), QPointF(70, -80),
                    QPointF(-120, -80)])
                    
        self.setPolygon(self.myPolygon)
        self.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)
        
    def image(self):
        pixmap = QPixmap(250, 250)
        pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap)
        painter.setPen(QPen(Qt.black, 8))
        painter.translate(125, 125)
        painter.drawPolyline(self.myPolygon)
        return pixmap
