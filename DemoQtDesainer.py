import sys

from qtdesigner4 import*
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*

class MainFrom(QDialog):
	def __init__(self, parent = None):
		QDialog.__init__(self, parent)
		self.ui = Ui_Form()
		self.ui.setupUi(self)
		self.ui.Hallo.clicked.connect(self.halloClicked)
	
	def halloClicked(self):
		QMessageBox.information(self, 'Demo Qt Designer',
			'Hallo %s, apa kabar?' %self.ui.NameEdit.text())
		
if __name__== "__main__":
	a =QApplication(sys.argv)
	form = MainFrom()
	form.show()
	a.exec_()