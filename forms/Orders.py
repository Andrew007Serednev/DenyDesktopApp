# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\Orders.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1039, 900)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.order_list = QtWidgets.QListWidget(self.centralwidget)
        self.order_list.setGeometry(QtCore.QRect(510, 80, 211, 751))
        self.order_list.setObjectName("order_list")
        self.order_create_button = QtWidgets.QPushButton(self.centralwidget)
        self.order_create_button.setGeometry(QtCore.QRect(760, 360, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.order_create_button.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\ui\\../static/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.order_create_button.setIcon(icon)
        self.order_create_button.setObjectName("order_create_button")
        self.order_edit_button = QtWidgets.QPushButton(self.centralwidget)
        self.order_edit_button.setGeometry(QtCore.QRect(760, 180, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.order_edit_button.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\ui\\../static/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.order_edit_button.setIcon(icon1)
        self.order_edit_button.setObjectName("order_edit_button")
        self.order_delete_button = QtWidgets.QPushButton(self.centralwidget)
        self.order_delete_button.setGeometry(QtCore.QRect(760, 270, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.order_delete_button.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(".\\ui\\../static/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.order_delete_button.setIcon(icon2)
        self.order_delete_button.setObjectName("order_delete_button")
        self.calendar_order = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendar_order.setGeometry(QtCore.QRect(40, 80, 431, 261))
        self.calendar_order.setObjectName("calendar_order")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 40, 111, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(510, 29, 191, 41))
        self.label_2.setObjectName("label_2")
        self.route_order_list = QtWidgets.QComboBox(self.centralwidget)
        self.route_order_list.setGeometry(QtCore.QRect(40, 410, 81, 31))
        self.route_order_list.setObjectName("route_order_list")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 370, 91, 20))
        self.label_3.setObjectName("label_3")
        self.order_count_list = QtWidgets.QComboBox(self.centralwidget)
        self.order_count_list.setGeometry(QtCore.QRect(160, 410, 71, 31))
        self.order_count_list.setObjectName("order_count_list")
        self.order_count_list.addItem("")
        self.order_count_list.addItem("")
        self.order_count_list.addItem("")
        self.order_count_list.addItem("")
        self.order_count_list.addItem("")
        self.order_count_list.addItem("")
        self.order_count_list.addItem("")
        self.order_count_list.addItem("")
        self.order_count_list.addItem("")
        self.order_count_list.addItem("")
        self.order_count_list.addItem("")
        self.order_count_list.addItem("")
        self.order_count_list.addItem("")
        self.order_count_list.addItem("")
        self.order_count_list.addItem("")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 359, 81, 41))
        self.label_4.setObjectName("label_4")
        self.create_plan_order_button = QtWidgets.QPushButton(self.centralwidget)
        self.create_plan_order_button.setGeometry(QtCore.QRect(260, 400, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.create_plan_order_button.setFont(font)
        self.create_plan_order_button.setIcon(icon)
        self.create_plan_order_button.setObjectName("create_plan_order_button")
        self.time_order_edit = QtWidgets.QTimeEdit(self.centralwidget)
        self.time_order_edit.setGeometry(QtCore.QRect(760, 80, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.time_order_edit.setFont(font)
        self.time_order_edit.setObjectName("time_order_edit")
        self.add_time_to_plan_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_time_to_plan_button.setGeometry(QtCore.QRect(870, 60, 141, 61))
        self.add_time_to_plan_button.setObjectName("add_time_to_plan_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1039, 27))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtWidgets.QAction(MainWindow)
        self.action_6.setObjectName("action_6")
        self.action_8 = QtWidgets.QAction(MainWindow)
        self.action_8.setObjectName("action_8")
        self.action_9 = QtWidgets.QAction(MainWindow)
        self.action_9.setObjectName("action_9")
        self.action_11 = QtWidgets.QAction(MainWindow)
        self.action_11.setObjectName("action_11")
        self.action_12 = QtWidgets.QAction(MainWindow)
        self.action_12.setObjectName("action_12")
        self.menu.addSeparator()
        self.menu.addAction(self.action_5)
        self.menu.addAction(self.action_6)
        self.menu.addSeparator()
        self.menu.addAction(self.action_8)
        self.menu.addAction(self.action_9)
        self.menu.addSeparator()
        self.menu.addAction(self.action_11)
        self.menu.addAction(self.action_12)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Наряды"))
        self.order_create_button.setText(_translate("MainWindow", "Создать новый наряд\n"
"вне плана"))
        self.order_edit_button.setText(_translate("MainWindow", "Изменить выбранный наряд"))
        self.order_delete_button.setText(_translate("MainWindow", "Удалить выбранный наряд"))
        self.label.setText(_translate("MainWindow", "1. Дата наряда"))
        self.label_2.setText(_translate("MainWindow", "4. Наряды на выбранную\n"
"дату"))
        self.label_3.setText(_translate("MainWindow", "2. Маршрут"))
        self.order_count_list.setItemText(0, _translate("MainWindow", "1"))
        self.order_count_list.setItemText(1, _translate("MainWindow", "2"))
        self.order_count_list.setItemText(2, _translate("MainWindow", "3"))
        self.order_count_list.setItemText(3, _translate("MainWindow", "4"))
        self.order_count_list.setItemText(4, _translate("MainWindow", "5"))
        self.order_count_list.setItemText(5, _translate("MainWindow", "6"))
        self.order_count_list.setItemText(6, _translate("MainWindow", "7"))
        self.order_count_list.setItemText(7, _translate("MainWindow", "8"))
        self.order_count_list.setItemText(8, _translate("MainWindow", "9"))
        self.order_count_list.setItemText(9, _translate("MainWindow", "10"))
        self.order_count_list.setItemText(10, _translate("MainWindow", "11"))
        self.order_count_list.setItemText(11, _translate("MainWindow", "12"))
        self.order_count_list.setItemText(12, _translate("MainWindow", "13"))
        self.order_count_list.setItemText(13, _translate("MainWindow", "14"))
        self.order_count_list.setItemText(14, _translate("MainWindow", "15"))
        self.label_4.setText(_translate("MainWindow", "3. Кол-во\n"
"графиков"))
        self.create_plan_order_button.setText(_translate("MainWindow", "Создать планы нарядов"))
        self.add_time_to_plan_button.setText(_translate("MainWindow", "5. Запланировать\n"
"время выпуска"))
        self.menu.setTitle(_translate("MainWindow", "Администрирование"))
        self.action.setText(_translate("MainWindow", "Диспетчер"))
        self.action_2.setText(_translate("MainWindow", "Механик"))
        self.action_3.setText(_translate("MainWindow", "Бухгалтер"))
        self.action_5.setText(_translate("MainWindow", "Водитель"))
        self.action_6.setText(_translate("MainWindow", "Кондуктор"))
        self.action_8.setText(_translate("MainWindow", "Автобус"))
        self.action_9.setText(_translate("MainWindow", "Маршрут"))
        self.action_11.setText(_translate("MainWindow", "Механик"))
        self.action_12.setText(_translate("MainWindow", "Диспетчер"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
