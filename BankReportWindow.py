# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/mikhailisakov/BankDB/BankReportWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BankReportWindow(object):
    def setupUi(self, BankReportWindow):
        BankReportWindow.setObjectName("BankReportWindow")
        BankReportWindow.resize(600, 450)
        BankReportWindow.setMinimumSize(QtCore.QSize(600, 450))
        BankReportWindow.setMaximumSize(QtCore.QSize(700, 500))
        self.centralwidget = QtWidgets.QWidget(BankReportWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.HeadingLabel = QtWidgets.QLabel(self.centralwidget)
        self.HeadingLabel.setMinimumSize(QtCore.QSize(200, 50))
        self.HeadingLabel.setObjectName("HeadingLabel")
        self.verticalLayout.addWidget(self.HeadingLabel, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.DescriptionTextBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.DescriptionTextBrowser.setMinimumSize(QtCore.QSize(100, 0))
        self.DescriptionTextBrowser.setObjectName("DescriptionTextBrowser")
        self.verticalLayout.addWidget(self.DescriptionTextBrowser)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 2, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.BankNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.BankNameLabel.setMinimumSize(QtCore.QSize(200, 50))
        self.BankNameLabel.setMaximumSize(QtCore.QSize(200, 50))
        self.BankNameLabel.setObjectName("BankNameLabel")
        self.horizontalLayout.addWidget(self.BankNameLabel)
        self.BankNameComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.BankNameComboBox.setMinimumSize(QtCore.QSize(300, 50))
        self.BankNameComboBox.setObjectName("BankNameComboBox")
        self.horizontalLayout.addWidget(self.BankNameComboBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.StartDateLabel = QtWidgets.QLabel(self.centralwidget)
        self.StartDateLabel.setMinimumSize(QtCore.QSize(250, 50))
        self.StartDateLabel.setMaximumSize(QtCore.QSize(250, 50))
        self.StartDateLabel.setObjectName("StartDateLabel")
        self.horizontalLayout_2.addWidget(self.StartDateLabel)
        self.StartDateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.StartDateEdit.setMaximumDate(QtCore.QDate(2018, 11, 30))
        self.StartDateEdit.setMinimumDate(QtCore.QDate(2018, 1, 1))
        self.StartDateEdit.setDate(QtCore.QDate(2018, 1, 1))
        self.StartDateEdit.setObjectName("StartDateEdit")
        self.horizontalLayout_2.addWidget(self.StartDateEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.EndDateLabel = QtWidgets.QLabel(self.centralwidget)
        self.EndDateLabel.setMinimumSize(QtCore.QSize(250, 50))
        self.EndDateLabel.setMaximumSize(QtCore.QSize(250, 50))
        self.EndDateLabel.setObjectName("EndDateLabel")
        self.horizontalLayout_3.addWidget(self.EndDateLabel)
        self.EndDateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.EndDateEdit.setMaximumDate(QtCore.QDate(2018, 12, 31))
        self.EndDateEdit.setMinimumDate(QtCore.QDate(2018, 2, 1))
        self.EndDateEdit.setDate(QtCore.QDate(2018, 2, 1))
        self.EndDateEdit.setObjectName("EndDateEdit")
        self.horizontalLayout_3.addWidget(self.EndDateEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.BackPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.BackPushButton.setMinimumSize(QtCore.QSize(200, 50))
        self.BackPushButton.setMaximumSize(QtCore.QSize(250, 50))
        self.BackPushButton.setObjectName("BackPushButton")
        self.horizontalLayout_4.addWidget(self.BackPushButton)
        self.FormPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.FormPushButton.setMinimumSize(QtCore.QSize(200, 50))
        self.FormPushButton.setMaximumSize(QtCore.QSize(250, 50))
        self.FormPushButton.setObjectName("FormPushButton")
        self.horizontalLayout_4.addWidget(self.FormPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        BankReportWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(BankReportWindow)
        self.statusbar.setObjectName("statusbar")
        BankReportWindow.setStatusBar(self.statusbar)

        self.retranslateUi(BankReportWindow)
        QtCore.QMetaObject.connectSlotsByName(BankReportWindow)

    def retranslateUi(self, BankReportWindow):
        _translate = QtCore.QCoreApplication.translate
        BankReportWindow.setWindowTitle(_translate("BankReportWindow", "Создание отчета для одного банка"))
        self.HeadingLabel.setText(_translate("BankReportWindow", "Выберите параметры отчета"))
        self.DescriptionTextBrowser.setHtml(_translate("BankReportWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Список возможных банков представлен в окне справа ниже.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Минимальная возможная дата: 01.01.2018.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Максимальная возможная дата: 31.12.2018.</p></body></html>"))
        self.BankNameLabel.setText(_translate("BankReportWindow", "Выберите название банка:"))
        self.StartDateLabel.setText(_translate("BankReportWindow", "Выберите дату начала отчета:"))
        self.StartDateEdit.setDisplayFormat(_translate("BankReportWindow", "MM.yyyy"))
        self.EndDateLabel.setText(_translate("BankReportWindow", "Выберите дату окончания отчета: "))
        self.EndDateEdit.setDisplayFormat(_translate("BankReportWindow", "MM.yyyy"))
        self.BackPushButton.setText(_translate("BankReportWindow", "Назад"))
        self.FormPushButton.setText(_translate("BankReportWindow", "Сформировать отчет"))
