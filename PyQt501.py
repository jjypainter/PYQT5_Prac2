# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 20:38:13 2020

@author: krn41
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('One of My Serveral Application')
        self.move(300, 300)
        self.resize(400, 200)
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())