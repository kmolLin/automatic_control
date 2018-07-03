# diablockText
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGraphicsTextItem, QGraphicsItem

class DiablockText(QGraphicsTextItem):
    
    def __init__(self, showtext, position, parent=None, scene=None):
        super(DiablockText, self).__init__(parent, scene)
        
        self.setPlainText(showtext)
        x, y = position
        self.setX(x)
        self.setY(y)

        #self.setFlag(QGraphicsItem.ItemIsMovable)
        #self.setFlag(QGraphicsItem.ItemIsSelectable)

    def itemChange(self, change, value):
        if change == QGraphicsItem.ItemSelectedChange:
            self.selectedChange.emit(self)
        return value

    def focusOutEvent(self, event):
        self.setTextInteractionFlags(Qt.NoTextInteraction)
        self.lostFocus.emit(self)
        super(DiablockText, self).focusOutEvent(event)

    def mouseDoubleClickEvent(self, event):
        if self.textInteractionFlags() == Qt.NoTextInteraction:
            self.setTextInteractionFlags(Qt.TextEditorInteraction)
        super(DiablockText, self).mouseDoubleClickEvent(event)
