# diablockgroup

from PyQt5.QtWidgets import QGraphicsItemGroup, QGraphicsItem

class DiablockGroup(QGraphicsItemGroup):
    
    def __init__(self, parent=None):
        super(DiablockGroup, self).__init__(parent)
        self.setFlags(QGraphicsItem.ItemIsSelectable and QGraphicsItem.ItemIsMovable)
    
    
