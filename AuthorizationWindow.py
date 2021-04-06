# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/mikhailisakov/BankDB/BankApp/AuthorizationWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AuthorizationWindow(object):
    def setupUi(self, AuthorizationWindow):
        AuthorizationWindow.setObjectName("AuthorizationWindow")
        AuthorizationWindow.resize(663, 419)
        self.centralwidget = QtWidgets.QWidget(AuthorizationWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.HeadingLabel = QtWidgets.QLabel(self.centralwidget)
        self.HeadingLabel.setMinimumSize(QtCore.QSize(0, 50))
        self.HeadingLabel.setMaximumSize(QtCore.QSize(16777215, 50))
        self.HeadingLabel.setObjectName("HeadingLabel")
        self.verticalLayout.addWidget(self.HeadingLabel, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.DescriptionLabel = QtWidgets.QLabel(self.centralwidget)
        self.DescriptionLabel.setObjectName("DescriptionLabel")
        self.verticalLayout.addWidget(self.DescriptionLabel, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.ClientPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.ClientPushButton.setMinimumSize(QtCore.QSize(150, 50))
        self.ClientPushButton.setMaximumSize(QtCore.QSize(200, 50))
        self.ClientPushButton.setObjectName("ClientPushButton")
        self.horizontalLayout_6.addWidget(self.ClientPushButton)
        self.AdminPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.AdminPushButton.setMinimumSize(QtCore.QSize(150, 50))
        self.AdminPushButton.setMaximumSize(QtCore.QSize(200, 50))
        self.AdminPushButton.setObjectName("AdminPushButton")
        self.horizontalLayout_6.addWidget(self.AdminPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.AuthorizationHeadingLabel = QtWidgets.QLabel(self.centralwidget)
        self.AuthorizationHeadingLabel.setMinimumSize(QtCore.QSize(0, 50))
        self.AuthorizationHeadingLabel.setMaximumSize(QtCore.QSize(16777215, 50))
        self.AuthorizationHeadingLabel.setText("")
        self.AuthorizationHeadingLabel.setObjectName("AuthorizationHeadingLabel")
        self.verticalLayout.addWidget(self.AuthorizationHeadingLabel, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.UsernameLabel = QtWidgets.QLabel(self.centralwidget)
        self.UsernameLabel.setMinimumSize(QtCore.QSize(100, 50))
        self.UsernameLabel.setMaximumSize(QtCore.QSize(200, 50))
        self.UsernameLabel.setObjectName("UsernameLabel")
        self.horizontalLayout_8.addWidget(self.UsernameLabel)
        self.UsernameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.UsernameLineEdit.setText("")
        self.UsernameLineEdit.setObjectName("UsernameLineEdit")
        self.horizontalLayout_8.addWidget(self.UsernameLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.PasswordLabel = QtWidgets.QLabel(self.centralwidget)
        self.PasswordLabel.setMinimumSize(QtCore.QSize(100, 50))
        self.PasswordLabel.setObjectName("PasswordLabel")
        self.horizontalLayout_5.addWidget(self.PasswordLabel)
        self.PasswordLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.PasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PasswordLineEdit.setObjectName("PasswordLineEdit")
        self.horizontalLayout_5.addWidget(self.PasswordLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.BackPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.BackPushButton.setMinimumSize(QtCore.QSize(150, 50))
        self.BackPushButton.setMaximumSize(QtCore.QSize(200, 50))
        self.BackPushButton.setObjectName("BackPushButton")
        self.horizontalLayout_7.addWidget(self.BackPushButton)
        self.EnterPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.EnterPushButton.setMinimumSize(QtCore.QSize(150, 50))
        self.EnterPushButton.setMaximumSize(QtCore.QSize(200, 50))
        self.EnterPushButton.setObjectName("EnterPushButton")
        self.horizontalLayout_7.addWidget(self.EnterPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        AuthorizationWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AuthorizationWindow)
        self.statusbar.setObjectName("statusbar")
        AuthorizationWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AuthorizationWindow)
        QtCore.QMetaObject.connectSlotsByName(AuthorizationWindow)

    def retranslateUi(self, AuthorizationWindow):
        _translate = QtCore.QCoreApplication.translate
        AuthorizationWindow.setWindowTitle(_translate("AuthorizationWindow", "Авторизация"))
        self.HeadingLabel.setText(_translate("AuthorizationWindow", "Выберите права входа:"))
        self.DescriptionLabel.setText(_translate("AuthorizationWindow", "Обязательно нажмите одну из кнопок перед вводом логина и пароля!"))
        self.ClientPushButton.setText(_translate("AuthorizationWindow", "Клиент"))
        self.AdminPushButton.setText(_translate("AuthorizationWindow", "Админ"))
        self.UsernameLabel.setText(_translate("AuthorizationWindow", "Username:"))
        self.PasswordLabel.setText(_translate("AuthorizationWindow", "Password:"))
        self.BackPushButton.setText(_translate("AuthorizationWindow", "Назад"))
        self.EnterPushButton.setText(_translate("AuthorizationWindow", "Войти"))
