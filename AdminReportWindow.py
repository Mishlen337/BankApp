# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/mikhailisakov/BankDB/BankApp/AdminReportWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AdminReportWindow(object):
    def setupUi(self, AdminReportWindow):
        AdminReportWindow.setObjectName("AdminReportWindow")
        AdminReportWindow.resize(800, 509)
        self.centralwidget = QtWidgets.QWidget(AdminReportWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.HeadingLabel = QtWidgets.QLabel(self.centralwidget)
        self.HeadingLabel.setMinimumSize(QtCore.QSize(0, 50))
        self.HeadingLabel.setMaximumSize(QtCore.QSize(16777215, 50))
        self.HeadingLabel.setObjectName("HeadingLabel")
        self.verticalLayout.addWidget(self.HeadingLabel, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.StatusLabel = QtWidgets.QLabel(self.centralwidget)
        self.StatusLabel.setMinimumSize(QtCore.QSize(0, 50))
        self.StatusLabel.setMaximumSize(QtCore.QSize(16777215, 50))
        self.StatusLabel.setText("")
        self.StatusLabel.setObjectName("StatusLabel")
        self.verticalLayout.addWidget(self.StatusLabel)
        self.TableView = QtWidgets.QTableView(self.centralwidget)
        self.TableView.setMinimumSize(QtCore.QSize(0, 0))
        self.TableView.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.TableView.setObjectName("TableView")
        self.verticalLayout.addWidget(self.TableView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.BackPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.BackPushButton.setMinimumSize(QtCore.QSize(150, 50))
        self.BackPushButton.setMaximumSize(QtCore.QSize(200, 50))
        self.BackPushButton.setObjectName("BackPushButton")
        self.horizontalLayout.addWidget(self.BackPushButton)
        self.QuitPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.QuitPushButton.setMinimumSize(QtCore.QSize(150, 50))
        self.QuitPushButton.setMaximumSize(QtCore.QSize(200, 50))
        self.QuitPushButton.setObjectName("QuitPushButton")
        self.horizontalLayout.addWidget(self.QuitPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        AdminReportWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AdminReportWindow)
        self.statusbar.setObjectName("statusbar")
        AdminReportWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AdminReportWindow)
        QtCore.QMetaObject.connectSlotsByName(AdminReportWindow)

    def retranslateUi(self, AdminReportWindow):
        _translate = QtCore.QCoreApplication.translate
        AdminReportWindow.setWindowTitle(_translate("AdminReportWindow", "Вывод отчета"))
        self.HeadingLabel.setText(_translate("AdminReportWindow", "Вывод отчета с заданными вами ранее параметрами"))
        self.BackPushButton.setText(_translate("AdminReportWindow", "Назад"))
        self.QuitPushButton.setText(_translate("AdminReportWindow", "Выйти"))
