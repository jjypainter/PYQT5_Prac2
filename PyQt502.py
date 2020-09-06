# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 20:51:30 2020

@author: krn41
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox
from PyQt5.QtCore import Qt

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        cb = QCheckBox('Showtitle', self)
        cb.move(20, 20)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)
        
        self.setWindowTitle('QCheckBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()
        
    def changeTitle(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle(' ')
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())