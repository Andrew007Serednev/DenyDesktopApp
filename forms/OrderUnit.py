# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\OrderUnit.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(990, 818)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(860, 10, 81, 461))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.dateEdit = QtWidgets.QDateEdit(Dialog)
        self.dateEdit.setGeometry(QtCore.QRect(70, 20, 110, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dateEdit.setFont(font)
        self.dateEdit.setObjectName("dateEdit")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(20, 100, 61, 561))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 60, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.listWidget_2 = QtWidgets.QListWidget(Dialog)
        self.listWidget_2.setGeometry(QtCore.QRect(20, 710, 81, 81))
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 680, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.listWidget_3 = QtWidgets.QListWidget(Dialog)
        self.listWidget_3.setGeometry(QtCore.QRect(140, 710, 101, 81))
        self.listWidget_3.setObjectName("listWidget_3")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        self.listWidget_4 = QtWidgets.QListWidget(Dialog)
        self.listWidget_4.setGeometry(QtCore.QRect(830, 190, 71, 561))
        self.listWidget_4.setObjectName("listWidget_4")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_4.addItem(item)
        self.timeEdit = QtWidgets.QTimeEdit(Dialog)
        self.timeEdit.setGeometry(QtCore.QRect(720, 110, 118, 22))
        self.timeEdit.setObjectName("timeEdit")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(140, 680, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(800, 160, 51, 16))
        self.label_4.setObjectName("label_4")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 670, 341, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Dialog", "508"))
        item = self.listWidget.item(1)
        item.setText(_translate("Dialog", "501"))
        item = self.listWidget.item(2)
        item.setText(_translate("Dialog", "503"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("Dialog", "Борт №"))
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        item = self.listWidget_2.item(0)
        item.setText(_translate("Dialog", "2"))
        item = self.listWidget_2.item(1)
        item.setText(_translate("Dialog", "3"))
        item = self.listWidget_2.item(2)
        item.setText(_translate("Dialog", "21"))
        item = self.listWidget_2.item(3)
        item.setText(_translate("Dialog", "4"))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("Dialog", "Маршрут"))
        __sortingEnabled = self.listWidget_3.isSortingEnabled()
        self.listWidget_3.setSortingEnabled(False)
        item = self.listWidget_3.item(0)
        item.setText(_translate("Dialog", "2"))
        item = self.listWidget_3.item(1)
        item.setText(_translate("Dialog", "4"))
        item = self.listWidget_3.item(2)
        item.setText(_translate("Dialog", "5"))
        item = self.listWidget_3.item(3)
        item.setText(_translate("Dialog", "6"))
        self.listWidget_3.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget_4.isSortingEnabled()
        self.listWidget_4.setSortingEnabled(False)
        item = self.listWidget_4.item(0)
        item.setText(_translate("Dialog", "1"))
        item = self.listWidget_4.item(1)
        item.setText(_translate("Dialog", "2"))
        item = self.listWidget_4.item(2)
        item.setText(_translate("Dialog", "3"))
        item = self.listWidget_4.item(3)
        item.setText(_translate("Dialog", "4"))
        item = self.listWidget_4.item(4)
        item.setText(_translate("Dialog", "5"))
        item = self.listWidget_4.item(5)
        item.setText(_translate("Dialog", "6"))
        self.listWidget_4.setSortingEnabled(__sortingEnabled)
        self.label_3.setText(_translate("Dialog", "Кол-во графиков"))
        self.label_4.setText(_translate("Dialog", "График"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
