# -*- coding: utf-8 -*-
"""Python application for bank analization."""
import sys
from datetime import datetime
import pandas as pd
from bank_analize import bank_db_query
from bank_analize import AuthorizationDBQuery, TableBank, config
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from bank_analize.forms import AuthorizationWindow,ChooseReportWindow, BankReportWindow,\
                                BankListReportWindow, ReportWindow, AdminChooseSettingsWindow,\
                                AdminReportWindow, SettingsWindow

class MainWindow(QMainWindow):
    """Application class for bank analization."""
    def __init__(self):
        """Initialize form objects."""
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
        """Shows inital form for user authorization."""
        self.Authorization.setupUi(self)
        self.Authorization.AdminPushButton.clicked.connect(self.adminAuthorization)
        self.Authorization.ClientPushButton.clicked.connect(self.clientAuthorization)
        self.Authorization.QuitPushButton.clicked.connect(self.quitApp)
        self.show()

    def adminAuthorization(self):
        """Shows admin form authorization."""
        self.Authorization.AuthorizationHeadingLabel.setText("Введите пароль админа")
        self.Authorization.ClientPushButton.setStyleSheet(f"background-color: \
                                                            {config.background_color}")
        self.Authorization.AdminPushButton.setStyleSheet("background-color: red")
        self.Authorization.EnterPushButton.clicked.connect(self.checkAdminAuthorization)

    def checkAdminAuthorization(self):
        """Checks admin login and password in authorization db."""
        username = self.Authorization.UsernameLineEdit.text()
        password = self.Authorization.PasswordLineEdit.text()
        if AuthorizationDBQuery.admin_verification(username, password):
            self.startUIAdminChooseSettings()
        else:
            self.Authorization.AuthorizationHeadingLabel.setText("Неверный пароль админа. \
                                                                    Попробуйте еще раз")

    def startUIAdminChooseSettings(self):
        """Shows admin choose settings form."""
        self.AdminChooseSettings.setupUi(self)
        self.AdminChooseSettings.BankPushButton.clicked.connect(self.startUIAdminBankReport)
        self.AdminChooseSettings.BankListPushButton.clicked.connect(self.startUIAdminBankListReport)
        self.AdminChooseSettings.BackPushButton.clicked.connect(self.startUIAuthorization)
        self.AdminChooseSettings.SettingsPushButton.clicked.connect(self.startUIAdminSettings)
        self.show()

    def startUIAdminBankReport(self):
        """Shows admin form for bank report to determine arguments."""
        self.BankReport.setupUi(self)
        self.BankReport.BackPushButton.clicked.connect(self.startUIAdminChooseSettings)
        self.BankReport.FormPushButton.clicked.connect(self.calculateAdminBankReport)
        self.BankReport.BankNameComboBox.addItems(bank_db_query.bank_names_query())
        self.show()

    def calculateAdminBankReport(self):
        """Saves in the mart and calculates admin bank report using determined arguments."""
        start_date = self.BankReport.StartDateEdit.text()
        end_date = self.BankReport.EndDateEdit.text()
        bank = self.BankReport.BankNameComboBox.currentText()
        data = pd.DataFrame(bank_db_query.bank_query(bank, start_date, end_date),
                                                        columns = config.columns)
        self.startUIAdminFormReport(data)

    def startUIAdminBankListReport(self):
        """Shows admin form for bank list report to determine arguments."""
        self.BankListReport.setupUi(self)
        self.BankListReport.BackPushButton.clicked.connect(self.startUIAdminChooseSettings)
        self.BankListReport.FormPushButton.clicked.connect(self.calculateAdminBankListReport)
        self.BankListReport.BankListWidget.addItems(bank_db_query.bank_names_query())
        self.show()

    def calculateAdminBankListReport(self):
        """Saves in the mart and calculates admin bank list report using determined arguments."""
        bank_list = [item.text() for item in self.BankListReport.BankListWidget.selectedItems()]
        b_date = self.BankListReport.DateEdit.text()
        data = pd.DataFrame(bank_db_query.bank_list_query(bank_list, b_date),
                                                            columns = config.columns)
        self.startUIAdminFormReport(data)

    def startUIAdminSettings(self):
        """Shows admin choose settings form for design and path."""
        self.Settings.setupUi(self)
        self.Settings.BackPushButton.clicked.connect(self.startUIAdminChooseSettings)
        self.Settings.PathPushButton.clicked.connect(self.OnPathPushButton)
        self.Settings.SizeComboBox.addItems(config.size_list)
        self.Settings.BackgoundComboBox.addItems(config.background_color_list)
        self.Settings.ApplyDesignPushButton.clicked.connect(self.OnApplyDesignPushButton)

    def OnPathPushButton(self):
        """Shows admin settings window to determine path to excel reports."""
        directory = QFileDialog.getExistingDirectory(
            self, 'Select a directory','.')
        self.Settings.PathLine.setText(directory)
        self.Settings.ApplyPathPushButton.clicked.connect(self.OnApplyPathPushButton)

    def OnApplyPathPushButton(self):
        """Applies path settings in config file."""
        config.excel_path = self.Settings.PathLine.text()

    def OnApplyDesignPushButton(self):
        """Applies design settings in config file and changes style of the app."""
        config.size = int(self.Settings.SizeComboBox.currentText())
        config.background_color = self.Settings.BackgoundComboBox.currentText()
        self.setStyleSheet(f"background-color: {config.background_color};font-size: \
                                {config.size}px;")

    def startUIAdminFormReport(self, data: pd.DataFrame):
        """Shows admin report to illustrate it in the table."""
        self.AdminReport.setupUi(self)
        self.AdminReport.BackPushButton.clicked.connect(self.startUIAdminChooseSettings)
        self.AdminReport.QuitPushButton.clicked.connect(self.quitApp)
        self.AdminReport.TableView.setModel(TableBank.TableModel(data))
        self.show()

    def clientAuthorization(self):
        """Shows client form authorization."""
        self.Authorization.AuthorizationHeadingLabel.setText("Введите пароль клиента")
        self.Authorization.AdminPushButton.setStyleSheet(f"background-color: \
                                                            {config.background_color}")
        self.Authorization.ClientPushButton.setStyleSheet("background-color: red")
        self.Authorization.EnterPushButton.clicked.connect(self.checkClientAuthorization)

    def checkClientAuthorization(self):
        """Checks client login and password in authorization db."""
        username = self.Authorization.UsernameLineEdit.text()
        password = self.Authorization.PasswordLineEdit.text()
        if AuthorizationDBQuery.client_verification(username, password):
            self.startUIChooseReport()
        else:
            self.Authorization.AuthorizationHeadingLabel.setText("Неверный пароль клиента. \
                                                                    Попробуйте еще раз")

    def startUIChooseReport(self):
        """Shows client choose settings form."""
        self.ChooseReport.setupUi(self)
        self.ChooseReport.BankPushButton.clicked.connect(self.startUIBankReport)
        self.ChooseReport.BankListPushButton.clicked.connect(self.startUIBankListReport)
        self.ChooseReport.BackPushButton.clicked.connect(self.startUIAuthorization)
        self.show()

    def startUIBankReport(self):
        """Shows client form for bank report to determine arguments."""
        self.BankReport.setupUi(self)
        self.BankReport.BackPushButton.clicked.connect(self.startUIChooseReport)
        self.BankReport.FormPushButton.clicked.connect(self.calculateBankReport)
        self.BankReport.BankNameComboBox.addItems(bank_db_query.bank_names_query())
        self.show()

    def calculateBankReport(self):
        """Saves in the mart and calculates client bank report using determined arguments."""
        start_date = self.BankReport.StartDateEdit.text()
        end_date = self.BankReport.EndDateEdit.text()
        bank = self.BankReport.BankNameComboBox.currentText()
        data = pd.DataFrame(bank_db_query.bank_query(bank, start_date, end_date),
                                columns = config.columns)
        self.startUIFormReport(data)

    def startUIBankListReport(self):
        """Shows client form for bank list report to determine arguments."""
        self.BankListReport.setupUi(self)
        self.BankListReport.BackPushButton.clicked.connect(self.startUIChooseReport)
        self.BankListReport.FormPushButton.clicked.connect(self.calculateBankListReport)
        self.BankListReport.BankListWidget.addItems(bank_db_query.bank_names_query())
        self.show()

    def calculateBankListReport(self):
        """Saves in the mart and calculates client bank list report using determined arguments."""
        bank_list = [item.text() for item in self.BankListReport.BankListWidget.selectedItems()]
        b_date = self.BankListReport.DateEdit.text()
        data = pd.DataFrame(bank_db_query.bank_list_query(bank_list, b_date),
                                columns = config.columns)
        self.startUIFormReport(data)

    def startUIFormReport(self, data: pd.DataFrame):
        """
        Recieves data in dataframe format. 
        Shows client report to illustrate it in the table.
        """
        self.Report.setupUi(self)
        self.Report.BackPushButton.clicked.connect(self.startUIChooseReport)
        self.Report.QuitPushButton.clicked.connect(self.quitApp)
        self.Report.ExportPushButton.clicked.connect(lambda: self.exportReport(data))
        self.Report.TableView.setModel(TableBank.TableModel(data))
        self.show()

    def exportReport(self, data: pd.DataFrame):
        """
        Recieves data in dataframe format.
        Exports data to excel file in particular folder.
        """
        current_time = datetime.now().strftime("%d.%m.%Y - %H:%M:%S")
        report_name = f"БО {current_time}.xlsx"
        data.to_excel(f"{config.excel_path}/{report_name}")
        self.Report.StatusLabel.setText(f"Экспорт данных произошел успешно в папку \
                                            {config.excel_path}")

    def quitApp(self):
        """Quits app"""
        raise SystemExit(1)

def main():
    """Invokes application"""
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec_()

if __name__ == '__main__':
    """Calls function to run application"""
    main()
