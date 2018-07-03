# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from widgets.Ui_mainwindow import Ui_MainWindow
from core.diablock.diablockItem import DiablockItem
from core.diablock.diablockText import DiablockText
from core.diablock.diablockGroup import DiablockGroup
from core.diablock.diablockScene import DiablockScene

class MainWindow(QMainWindow, Ui_MainWindow):
    InsertTextButton = 10
    def __init__(self, parent=None):

        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.createscence()
        self.createToolBox()
        
        #self.creatbutton(10)
        self.tool_bar.addAction(QIcon(QPixmap(':/core/icons/open-icon.png')), "Openfile")
        self.tool_bar.addAction(QIcon(QPixmap(':/core/icons/save-icon.png')), "Savefile")
        self.tool_bar.addAction(QIcon(QPixmap(':/core/icons/Settings-icon.png')), "Setting")
        self.tool_bar.addAction(QIcon(QPixmap(':/core/icons/Button-Next-icon.png')), "Go")
        self.tool_bar.addAction(QIcon(QPixmap(':/core/icons/Actions-process-stop-icon.png')), "Stop")
        
    
    def creatbutton(self, index):
        pass
        
    def createscence(self):
        self.itemgroup = DiablockGroup()
        
        self.scene = DiablockScene(self)
        ccreate = DiablockItem(0)
        textitem = DiablockText("Transfer Function", (-45, 50))
        
        self.graphicsView.setScene(self.scene)
        self.itemgroup.addToGroup(textitem)
        self.itemgroup.addToGroup(ccreate)
        self.scene.addItem(self.itemgroup)
        
    def buttonGroupClicked(self, id):
        buttons = self.buttonGroup.buttons()
        for button in buttons:
            if self.buttonGroup.button(id) != button:
                button.setChecked(False)

        if id == self.InsertTextButton:
            self.scene.setMode(DiablockScene.InsertText)
        else:
            self.scene.setItemType(id)
            self.scene.setMode(DiablockScene.InsertItem)
            self.scene.createblock()
            
    def createCellWidget(self, text, diagramType):
        item = DiablockItem(diagramType)
        icon = QIcon(item.image())

        button = QToolButton()
        button.setIcon(icon)
        button.setIconSize(QSize(50, 50))
        button.setCheckable(True)
        self.buttonGroup.addButton(button, diagramType)

        layout = QGridLayout()
        layout.addWidget(button, 0, 0, Qt.AlignHCenter)
        layout.addWidget(QLabel(text), 1, 0, Qt.AlignCenter)

        widget = QWidget()
        widget.setLayout(layout)

        return widget
    
    def createToolBox(self):
        self.buttonGroup = QButtonGroup()
        self.buttonGroup.setExclusive(False)
        self.buttonGroup.buttonClicked[int].connect(self.buttonGroupClicked)
        
        layout = QGridLayout()
        layout.addWidget(self.createCellWidget("step", DiablockItem.Conditional),
                0, 0)
        layout.addWidget(self.createCellWidget("Transfer Function", DiablockItem.Step), 0,
                1)
        layout.addWidget(self.createCellWidget("Output", DiablockItem.Io),
                1, 0)
        
        textButton = QToolButton()
        textButton.setCheckable(True)
        self.buttonGroup.addButton(textButton, self.InsertTextButton)
        textButton.setIcon(QIcon(QPixmap(':/images/textpointer.png').scaled(30, 30)))
        textButton.setIconSize(QSize(50, 50))
        
        textLayout = QGridLayout()
        textLayout.addWidget(textButton, 0, 0, Qt.AlignHCenter)
        textLayout.addWidget(QLabel("Text"), 1, 0, Qt.AlignCenter)
        textWidget = QWidget()
        textWidget.setLayout(textLayout)
        layout.addWidget(textWidget, 1, 1)
        
        layout.setRowStretch(3, 10)
        layout.setColumnStretch(2, 10)
        
        itemWidget = QWidget()
        itemWidget.setLayout(layout)
        self.toolBox.removeItem(0)
        self.toolBox.setMaximumWidth(itemWidget.sizeHint().width())
        #self.toolBox.setSizePolicy(QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Ignored))
        self.toolBox.insertItem(0, itemWidget, "Basic Flowchart Shapes")
    
    @pyqtSlot(int)
    def on_toolBox_currentChanged(self, index):
        """
        Slot documentation goes here.
        
        @param index DESCRIPTION
        @type int
        """
        # TODO: not implemented yet
        pass
