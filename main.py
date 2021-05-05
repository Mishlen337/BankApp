# -*- coding: utf-8 -*-
import sys
import bank_db_query
import pandas as pd
from bank_analize import AuthorizationDBQuery, TableBank
from bank_analize import config
from PyQt5.QtWidgets import QApplication, QMainWindow , QPushButton , QWidget, QFileDialog
from bank_analize.forms import AuthorizationWindow, ChooseReportWindow, BankReportWindow, BankListReportWindow, ReportWindow, AdminChooseSettingsWindow, AdminReportWindow, SettingsWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Authorization = AuthorizationWindow.Ui_AuthorizationWindow()
        self.ChooseReport = ChooseReportWindow.Ui_ChooseReportWindow()
        self.AdminChooseSettings = AdminChooseSettingsWindow.Ui_AdminChooseSettingsWindow()
        self.Report = ReportWindow.Ui_ReportWindow()
        self.AdminReport = AdminReportWindow.Ui_AdminReportWindow()
        self.BankReport = BankReportWindow.Ui_BankReportWindow()
        self.BankListReport = BankListReportWindow.Ui_BankListReportWindow()
        self.Settings = SettingsWindow.Ui_SettingsWindow()
        self.startUIAuthorization()

    def startUIAuthorization(self):
        self.Authorization.setupUi(self)
        self.Authorization.AdminPushButton.clicked.connect(self.adminAuthorization)
        self.Authorization.ClientPushButton.clicked.connect(self.clientAuthorization)
        self.Authorization.QuitPushButton.clicked.connect(self.quitApp)
        self.show()

    def adminAuthorization(self):
        self.Authorization.AuthorizationHeadingLabel.setText("Введите пароль админа")
        self.Authorization.ClientPushButton.setStyleSheet(f"background-color: {config.background_color}")
        self.Authorization.AdminPushButton.setStyleSheet("background-color: red")
        self.Authorization.EnterPushButton.clicked.connect(self.checkAdminAuthorization)

    def clientAuthorization(self):
        self.Authorization.AuthorizationHeadingLabel.setText("Введите пароль клиента")
        self.Authorization.AdminPushButton.setStyleSheet(f"background-color: {config.background_color}")
        self.Authorization.ClientPushButton.setStyleSheet("background-color: red")
        self.Authorization.EnterPushButton.clicked.connect(self.checkClientAuthorization)

    def checkAdminAuthorization(self):
        username = self.Authorization.UsernameLineEdit.text()
        password = self.Authorization.PasswordLineEdit.text()
        if AuthorizationDBQuery.admin_verification(username, password):
            self.startUIAdminChooseSettings()
        else:
            self.Authorization.AuthorizationHeadingLabel.setText("Неверный пароль админа. Попробуйте еще раз")

    def checkClientAuthorization(self):
        username = self.Authorization.UsernameLineEdit.text()
        password = self.Authorization.PasswordLineEdit.text()
        if AuthorizationDBQuery.client_verification(username, password):
            self.startUIChooseReport()
        else:
            self.Authorization.AuthorizationHeadingLabel.setText("Неверный пароль клиента. Попробуйте еще раз")

    def startUIAdminChooseSettings(self):
        self.AdminChooseSettings.setupUi(self)
        self.AdminChooseSettings.BankPushButton.clicked.connect(self.startUIAdminBankReport)
        self.AdminChooseSettings.BankListPushButton.clicked.connect(self.startUIAdminBankListReport)
        self.AdminChooseSettings.BackPushButton.clicked.connect(self.startUIAuthorization)
        self.AdminChooseSettings.SettingsPushButton.clicked.connect(self.startUIAdminSettings)
        self.show()

    def startUIChooseReport(self):
        self.ChooseReport.setupUi(self)
        self.ChooseReport.BankPushButton.clicked.connect(self.startUIBankReport)
        self.ChooseReport.BankListPushButton.clicked.connect(self.startUIBankListReport)
        self.ChooseReport.BackPushButton.clicked.connect(self.startUIAuthorization)
        self.show()

    def startUIAdminBankReport(self):
        self.BankReport.setupUi(self)
        self.BankReport.BackPushButton.clicked.connect(self.startUIAdminChooseSettings)
        self.BankReport.FormPushButton.clicked.connect(self.startUIAdminFormBankReport)
        self.show()

    def startUIAdminBankListReport(self):
        self.BankListReport.setupUi(self)
        self.BankListReport.BackPushButton.clicked.connect(self.startUIAdminChooseSettings)
        self.BankListReport.FormPushButton.clicked.connect(self.startUIAdminFormBankListReport)
        self.show()

    def startUIAdminSettings(self):
        self.Settings.setupUi(self)
        self.Settings.BackPushButton.clicked.connect(self.startUIAdminChooseSettings)
        self.Settings.PathPushButton.clicked.connect(self.OnPathPushButton)
        self.Settings.SizeComboBox.addItems(config.size_list)
        self.Settings.BackgoundComboBox.addItems(config.background_color_list)
        self.Settings.ApplyDesignPushButton.clicked.connect(self.OnApplyDesignPushButton)

    def OnPathPushButton(self):
        directory = QFileDialog.getExistingDirectory(
            self, 'Select a directory','.')
        self.Settings.PathLine.setText(directory)
        self.Settings.ApplyPathPushButton.clicked.connect(self.OnApplyPathPushButton)

    def OnApplyPathPushButton(self):
        config.excel_path = self.Settings.PathLine.text()

    def OnApplyDesignPushButton(self):
        config.size = int(self.Settings.SizeComboBox.currentText())
        config.background_color = self.Settings.BackgoundComboBox.currentText()
        self.setStyleSheet(f"background-color: {config.background_color};font-size: {config.size}px;")

    def startUIBankReport(self):
        self.BankReport.setupUi(self)
        self.BankReport.BackPushButton.clicked.connect(self.startUIChooseReport)
        self.BankReport.FormPushButton.clicked.connect(self.calculateBankReport)
        self.BankReport.BankNameComboBox.addItems(bank_db_query.bank_names_query())
        self.show()

    def calculateBankReport(self):
        start_date = self.BankReport.StartDateEdit.text()
        end_date = self.BankReport.EndDateEdit.text()
        bank = self.BankReport.BankNameComboBox.currentText()
        data = pd.DataFrame(bank_db_query.bank_query(bank, start_date, end_date), columns = config.columns)
        self.startUIFormReport(data)

    def startUIBankListReport(self):
        self.BankListReport.setupUi(self)
        self.BankListReport.BackPushButton.clicked.connect(self.startUIChooseReport)
        self.BankListReport.FormPushButton.clicked.connect(self.calculateBankListReport)
        self.BankListReport.BankListWidget.addItems(bank_db_query.bank_names_query())
        self.show()

    def calculateBankListReport(self):
        bank_list = [item.text() for item in self.BankListReport.BankListWidget.selectedItems()]
        b_date = self.BankListReport.DateEdit.text()
        data = pd.DataFrame(bank_db_query.bank_list_query(bank_list, b_date), columns = config.columns)
        self.startUIFormReport(data)

    def startUIAdminFormBankReport(self):
        self.AdminReport.setupUi(self)
        self.AdminReport.BackPushButton.clicked.connect(self.startUIAdminBankReport)
        self.AdminReport.QuitPushButton.clicked.connect(self.quitApp)
        self.show()
    
    def startUIAdminFormBankListReport(self):
        self.AdminReport.setupUi(self)
        self.AdminReport.BackPushButton.clicked.connect(self.startUIAdminBankListReport)
        self.AdminReport.QuitPushButton.clicked.connect(self.quitApp)
        self.show()
    
    def startUIFormReport(self, data: pd.DataFrame):
        self.Report.setupUi(self)
        self.Report.BackPushButton.clicked.connect(self.startUIBankReport)
        self.Report.QuitPushButton.clicked.connect(self.quitApp)
        self.Report.ExportPushButton.clicked.connect(lambda: self.exportReport(data))
        self.Report.TableView.setModel(TableBank.TableModel(data))
        self.show()

    def exportReport(self, data: pd.DataFrame):
        self.Report.StatusLabel.setText(f"Экспорт данных произошел успешно в папку {config.excel_path}")
        data.to_excel(f"{config.excel_path}/output.xlsx")

    def quitApp(self):
        raise SystemExit(1)
    
def main():
    app = QApplication(sys.argv) 
    window = MainWindow() 
    app.exec_()

if __name__ == '__main__': 
    main() 