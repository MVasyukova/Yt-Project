#!/usr/bin/python3 
#-*- coding utf-8 -*-

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QListWidget, QListWidgetItem, QLabel
from PyQt5 import uic #pyuic генерирует код из QtCreator

FormUI, Form = uic.loadUiType('form.ui') #Form и FormUI чем отличаются?

class  MyWindow(Form): 

    def __init__(self, parent = None): #self - способ сообщения между экземплярами;                                         способ, чтобы класс ссылался на себя
        
        super(MyWindow, self).__init__()
        self.ui = ui = FormUI() #что это?
        ui.setupUi(self) 
        ui.execute_button.clicked.connect(self.__execute)
        ui.query_history.itemDoubleClicked.connect(self.__edit)

    def __del__(self):
        self.ui = None

    def __edit(self):
        item = self.ui.query_history.currentItem()
        if not item:
            return
        self.ui.query_text.setText(item.text())

    def __execute(self):
         text = self.ui.query_text.text().strip()
         self.ui.query_text.setText('')
         if text == '':
             return

         lbl = QLabel(text)
         lbl.resize(lbl.sizeHint())
         lwi = QListWidgetItem()
         lwi.setSizeHint(lbl.sizeHint())
                                
         h = self.ui.query_history
         h.addItem(lwi)
         h.setItemWidget(lwi, lbl)

    def keyPressEvent(self, event):
        print(event)
        if event.key() == Qt.Key_Return and self.ui.query_text.hasFocus():
            self.__execute()
          

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # create window
    w = MyWindow()
    w.setWindowTitle("DB Shell")
    w.show()
    # enter main loop
    sys.exit(app.exec_()) 
