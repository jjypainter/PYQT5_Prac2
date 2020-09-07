# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 08:47:34 2020

@author: krn41
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.lb1 = QLabel('Option1', self)
        self.lb1.move(50, 150)
        
        
        cb = QComboBox(self)
        cb.addItem('Option1')
        cb.addItem('Option2')
        cb.addItem('Option3')
        cb.addItem('Option4')
        cb.move(50, 50)
        
        cb.activated[str].connect(self.onActivated)
        
        self.setWindowTitle('QComboBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()
        
    def onActivated(self, text):
        self.lb1.setText(text)
        self.lb1.adjustSize()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())