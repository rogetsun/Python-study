# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testdialog.ui'
#
# Created: Thu Aug 13 14:25:00 2015
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        dialog.resize(719, 409)
        self.buttonBox = QtWidgets.QDialogButtonBox(dialog)
        self.buttonBox.setGeometry(QtCore.QRect(360, 360, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 671, 331))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.verticalLayoutWidget)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.verticalLayout.addWidget(self.commandLinkButton)
        self.listView = QtWidgets.QListView(self.verticalLayoutWidget)
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)
        self.label = QtWidgets.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(30, 0, 59, 16))
        self.label.setObjectName("label")
        self.actionDdd = QtWidgets.QAction(dialog)
        self.actionDdd.setObjectName("actionDdd")

        self.retranslateUi(dialog)
        self.buttonBox.accepted.connect(dialog.accept)
        self.buttonBox.rejected.connect(dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "测试窗体"))
        dialog.setToolTip(_translate("dialog", "111"))
        dialog.setWhatsThis(_translate("dialog", "111"))
        dialog.setWindowFilePath(_translate("dialog", "111"))
        self.radioButton.setText(_translate("dialog", "男"))
        self.radioButton_2.setText(_translate("dialog", "女"))
        self.commandLinkButton.setText(_translate("dialog", "CommandLinkButton"))
        self.label.setText(_translate("dialog", "测试"))
        self.actionDdd.setText(_translate("dialog", "ddd"))
        self.actionDdd.setToolTip(_translate("dialog", "<html><head/><body><p>testddd</p></body></html>"))

