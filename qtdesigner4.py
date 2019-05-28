# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtdesigner4.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(537, 300)
        self.Label = QtWidgets.QLabel(Form)
        self.Label.setGeometry(QtCore.QRect(80, 90, 241, 16))
        self.Label.setObjectName("Label")
        self.NameEdit = QtWidgets.QLineEdit(Form)
        self.NameEdit.setGeometry(QtCore.QRect(80, 120, 371, 20))
        self.NameEdit.setText("")
        self.NameEdit.setObjectName("NameEdit")
        self.Hallo = QtWidgets.QPushButton(Form)
        self.Hallo.setGeometry(QtCore.QRect(180, 160, 75, 23))
        self.Hallo.setObjectName("Hallo")
        self.Clear = QtWidgets.QPushButton(Form)
        self.Clear.setGeometry(QtCore.QRect(270, 160, 75, 23))
        self.Clear.setObjectName("Clear")
        self.EXit = QtWidgets.QPushButton(Form)
        self.EXit.setGeometry(QtCore.QRect(240, 260, 75, 23))
        self.EXit.setObjectName("EXit")

        self.retranslateUi(Form)
        self.EXit.clicked.connect(Form.close)
        self.Clear.clicked.connect(self.NameEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; color:#aaaaff;\">Masukkan Nama Anda :</span></p><p><br/></p></body></html>"))
        self.Hallo.setText(_translate("Form", "Hallo"))
        self.Clear.setText(_translate("Form", "Clear"))
        self.EXit.setText(_translate("Form", "Exit"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
