__author__ = 'uv2sun'
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import td

import site

print(site.getsitepackages())


class TestDialog(QDialog, td.Ui_Dialog):
    def __init__(self, parent=None):
        super(TestDialog, self).__init__(parent)
        self.setupUi(self)


app = QApplication(sys.argv)
dialog = TestDialog()
dialog.show()
app.exec_()
