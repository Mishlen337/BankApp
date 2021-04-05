import sys  # sys нужен для передачи argv в QApplication
import time 
from PyQt5.QtWidgets import QApplication, QMainWindow , QPushButton , QWidget
import AuthorizationWindow
import ChooseReportWindow
import BankReportWindow
import BankListReportWindow
import ReportWindow

class MainWindow(QMainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.Authorization = AuthorizationWindow.Ui_AuthorizationWindow()
        self.ChooseReport = ChooseReportWindow.Ui_ChooseReportWindow()
        self.Report = ReportWindow.Ui_ReportWindow()
        self.BankReport = BankReportWindow.Ui_BankReportWindow()
        self.BankListReport = BankListReportWindow.Ui_BankListReportWindow()
        self.startUIAuthorization()

    def startUIAuthorization(self):
        self.Authorization.setupUi(self)
        self.Authorization.EnterPushButton.clicked.connect(self.startUIChooseReport)
        self.show()
        
    def startUIChooseReport(self):
        self.ChooseReport.setupUi(self)
        self.ChooseReport.BankPushButton.clicked.connect(self.startUIBankReport)
        self.ChooseReport.ListBankPushButton.clicked.connect(self.startUIBankListReport)
        self.ChooseReport.BackPushButton.clicked.connect(self.startUIAuthorization)
        self.show()

    def startUIBankReport(self):
        self.BankReport.setupUi(self)
        self.BankReport.BackPushButton.clicked.connect(self.startUIChooseReport)
        self.BankReport.FormPushButton.clicked.connect(self.startUIReport)
        self.show()

    def startUIBankListReport(self):
        self.BankListReport.setupUi(self)
        self.BankListReport.BackPushButton.clicked.connect(self.startUIChooseReport)
        self.BankListReport.FormPushButton.clicked.connect(self.startUIReport)
        self.show()

    def startUIReport(self):
        self.Report.setupUi(self)
        self.Report.BackPushButton.clicked.connect(self.startUIBankReport)
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
