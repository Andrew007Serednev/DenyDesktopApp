# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\NewDriver.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 535)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(540, 460, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.new_driver_fio_edit = QtWidgets.QLineEdit(Dialog)
        self.new_driver_fio_edit.setGeometry(QtCore.QRect(200, 20, 311, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.new_driver_fio_edit.setFont(font)
        self.new_driver_fio_edit.setObjectName("new_driver_fio_edit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 171, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 61, 22))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.new_driver_snils_edit = QtWidgets.QLineEdit(Dialog)
        self.new_driver_snils_edit.setGeometry(QtCore.QRect(200, 70, 171, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.new_driver_snils_edit.setFont(font)
        self.new_driver_snils_edit.setObjectName("new_driver_snils_edit")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 141, 22))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.new_driver_license_edit = QtWidgets.QLineEdit(Dialog)
        self.new_driver_license_edit.setGeometry(QtCore.QRect(200, 120, 171, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.new_driver_license_edit.setFont(font)
        self.new_driver_license_edit.setObjectName("new_driver_license_edit")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 170, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.new_driver_start_date = QtWidgets.QDateEdit(Dialog)
        self.new_driver_start_date.setGeometry(QtCore.QRect(200, 180, 110, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.new_driver_start_date.setFont(font)
        self.new_driver_start_date.setObjectName("new_driver_start_date")
        self.new_driver_end_date = QtWidgets.QDateEdit(Dialog)
        self.new_driver_end_date.setGeometry(QtCore.QRect(330, 180, 110, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.new_driver_end_date.setFont(font)
        self.new_driver_end_date.setObjectName("new_driver_end_date")
        self.drivers_list = QtWidgets.QListWidget(Dialog)
        self.drivers_list.setGeometry(QtCore.QRect(10, 230, 431, 221))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.drivers_list.setFont(font)
        self.drivers_list.setObjectName("drivers_list")
        self.driver_delete_button = QtWidgets.QPushButton(Dialog)
        self.driver_delete_button.setGeometry(QtCore.QRect(470, 300, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.driver_delete_button.setFont(font)
        self.driver_delete_button.setObjectName("driver_delete_button")
        self.driver_save_button = QtWidgets.QPushButton(Dialog)
        self.driver_save_button.setGeometry(QtCore.QRect(470, 230, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.driver_save_button.setFont(font)
        self.driver_save_button.setObjectName("driver_save_button")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Новый водитель, ФИО"))
        self.label_2.setText(_translate("Dialog", "СНИЛС"))
        self.label_3.setText(_translate("Dialog", "Водительское, №"))
        self.label_4.setText(_translate("Dialog", "Водительское, \n"
"дата От-До"))
        self.driver_delete_button.setText(_translate("Dialog", "Удалить водителя\n"
" из списка"))
        self.driver_save_button.setText(_translate("Dialog", "Добавить водителя\n"
" в список"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Ui_Dialog()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())