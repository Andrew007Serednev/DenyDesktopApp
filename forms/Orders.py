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
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.orderList = QtWidgets.QListWidget(self.centralwidget)
        self.orderList.setGeometry(QtCore.QRect(510, 80, 211, 751))
        self.orderList.setObjectName("orderList")
        self.orderCreateButton = QtWidgets.QPushButton(self.centralwidget)
        self.orderCreateButton.setGeometry(QtCore.QRect(760, 80, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.orderCreateButton.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\ui\\../static/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.orderCreateButton.setIcon(icon)
        self.orderCreateButton.setObjectName("orderCreateButton")
        self.orderChangeButton = QtWidgets.QPushButton(self.centralwidget)
        self.orderChangeButton.setGeometry(QtCore.QRect(760, 170, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.orderChangeButton.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\ui\\../static/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.orderChangeButton.setIcon(icon1)
        self.orderChangeButton.setObjectName("orderChangeButton")
        self.orderDeleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.orderDeleteButton.setGeometry(QtCore.QRect(760, 260, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.orderDeleteButton.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(".\\ui\\../static/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.orderDeleteButton.setIcon(icon2)
        self.orderDeleteButton.setObjectName("orderDeleteButton")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(40, 80, 431, 261))
        self.calendarWidget.setObjectName("calendarWidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 40, 91, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(510, 40, 211, 20))
        self.label_2.setObjectName("label_2")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Путевые листы"))
        self.orderCreateButton.setText(_translate("MainWindow", "Создать новый наряд"))
        self.orderChangeButton.setText(_translate("MainWindow", "Изменить выбранный наряд"))
        self.orderDeleteButton.setText(_translate("MainWindow", "Удалить выбранный наряд"))
        self.label.setText(_translate("MainWindow", "Дата наряда"))
        self.label_2.setText(_translate("MainWindow", "Наряды на выбранную дату"))
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
