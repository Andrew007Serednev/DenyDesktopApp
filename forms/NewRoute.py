# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\NewRoute.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(240, 480)
        font = QtGui.QFont()
        font.setPointSize(12)
        Dialog.setFont(font)
        Dialog.setModal(True)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(130, 420, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.route_save_button = QtWidgets.QPushButton(Dialog)
        self.route_save_button.setGeometry(QtCore.QRect(120, 70, 31, 31))
        self.route_save_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\ui\\../static/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.route_save_button.setIcon(icon)
        self.route_save_button.setIconSize(QtCore.QSize(32, 32))
        self.route_save_button.setObjectName("route_save_button")
        self.route_list = QtWidgets.QListWidget(Dialog)
        self.route_list.setGeometry(QtCore.QRect(30, 120, 71, 321))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.route_list.setFont(font)
        self.route_list.setObjectName("route_list")
        self.route_delete_button = QtWidgets.QPushButton(Dialog)
        self.route_delete_button.setGeometry(QtCore.QRect(120, 170, 31, 31))
        self.route_delete_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\ui\\../static/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.route_delete_button.setIcon(icon1)
        self.route_delete_button.setIconSize(QtCore.QSize(32, 32))
        self.route_delete_button.setObjectName("route_delete_button")
        self.new_route_edit = QtWidgets.QLineEdit(Dialog)
        self.new_route_edit.setGeometry(QtCore.QRect(30, 70, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.new_route_edit.setFont(font)
        self.new_route_edit.setObjectName("new_route_edit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 11, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.route_edit_button = QtWidgets.QPushButton(Dialog)
        self.route_edit_button.setGeometry(QtCore.QRect(120, 120, 31, 31))
        self.route_edit_button.setMaximumSize(QtCore.QSize(16777207, 16777215))
        self.route_edit_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(".\\ui\\../static/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.route_edit_button.setIcon(icon2)
        self.route_edit_button.setIconSize(QtCore.QSize(32, 32))
        self.route_edit_button.setObjectName("route_edit_button")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Маршруты"))
        self.label.setText(_translate("Dialog", "Маршрут"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())