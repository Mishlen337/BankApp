import sys  # sys нужен для передачи argv в QApplication
import time 
from PyQt5.QtWidgets import QApplication, QMainWindow , QPushButton , QWidget
import AuthorizationWindow
import ChooseReportWindow
import BankReportWindow
import BankListReportWindow
import ReportWindow
import AuthorizationDBQuery
import AdminChooseSettingsWindow
class MainWindow(QMainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.Authorization = AuthorizationWindow.Ui_AuthorizationWindow()
        self.ChooseReport = ChooseReportWindow.Ui_ChooseReportWindow()
        self.AdminChooseSettings = AdminChooseSettingsWindow.Ui_AdminChooseSettingsWindow()
        self.Report = ReportWindow.Ui_ReportWindow()
        self.BankReport = BankReportWindow.Ui_BankReportWindow()
        self.BankListReport = BankListReportWindow.Ui_BankListReportWindow()
        self.startUIAuthorization()

    def startUIAuthorization(self):
        self.Authorization.setupUi(self)
        self.Authorization.AdminPushButton.clicked.connect(self.adminAuthorization)
        self.Authorization.ClientPushButton.clicked.connect(self.clientAuthorization)
        self.show()

    def adminAuthorization(self):
        self.Authorization.AuthorizationHeadingLabel.setText("Введите пароль админа")
        self.Authorization.ClientPushButton.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.Authorization.AdminPushButton.setStyleSheet("background-color: red")
        self.Authorization.EnterPushButton.clicked.connect(self.checkAdminAuthorization)

    def clientAuthorization(self):
        self.Authorization.AuthorizationHeadingLabel.setText("Введите пароль клиента")
        self.Authorization.AdminPushButton.setStyleSheet("background-color: rgb(255, 255, 255)")
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
        self.BankReport.FormPushButton.clicked.connect(self.startUIFormBankReport)
        self.show()

    def startUIAdminBankListReport(self):
        self.BankListReport.setupUi(self)
        self.BankListReport.BackPushButton.clicked.connect(self.startUIAdminChooseSettings)
        self.BankListReport.FormPushButton.clicked.connect(self.startUIFormBankListReport)
        self.show()

    def startUIBankReport(self):
        self.BankReport.setupUi(self)
        self.BankReport.BackPushButton.clicked.connect(self.startUIChooseReport)
        self.BankReport.FormPushButton.clicked.connect(self.startUIFormBankReport)
        self.show()

    def startUIBankListReport(self):
        self.BankListReport.setupUi(self)
        self.BankListReport.BackPushButton.clicked.connect(self.startUIChooseReport)
        self.BankListReport.FormPushButton.clicked.connect(self.startUIFormBankListReport)
        self.show()

    def startUIFormBankReport(self):
        self.Report.setupUi(self)
        #TODO querying to DB for Bank report
        self.Report.BackPushButton.clicked.connect(self.startUIBankReport)
        self.Report.QuitPushButton.clicked.connect(self.quitApp)
        self.show()
    

    def startUIFormBankListReport(self):
        self.Report.setupUi(self)
        #TODO querying to DB for BankList report
        self.Report.BackPushButton.clicked.connect(self.startUIBankListReport)
        self.Report.QuitPushButton.clicked.connect(self.quitApp)
        self.show()

    def quitApp(self):
        raise SystemExit(1)
    
def main():
    app = QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MainWindow()  # Создаём объект класса BankApp
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()