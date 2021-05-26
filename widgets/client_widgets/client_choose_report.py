import sys
sys.path.insert(0, '/Users/mikhailisakov/BankDB/BankApp')
from PyQt5 import QtWidgets, uic
from widgets import authorization
from widgets.client_widgets.form_report import form_bank, form_bank_list

class ChooseReport(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        """
        Виджет, позволяющий выбрать клиенту вид отчета
        (для одного банка, для нескольких банков).
        """
        super().__init__(*args, **kwargs)
        uic.loadUi('./ui/client_ui/ChooseReportWindow.ui', self)
        #Инициализация кнопок, выходящих в форму
        self.BackPushButton.clicked.connect(self.OnBackPushButton)
        self.BankPushButton.clicked.connect(self.OnBankPushButton)
        self.BankListPushButton.clicked.connect(self.OnBankListPushButton)

    def OnBackPushButton(self):
        """
        Обработка нажатия на кнопку "Назад".
        Остановка показа формы выбора отчета и переход к форме авторизации.
        """
        self.reject()
        authorization.Authorization(parent = self).show()
    
    def OnBankPushButton(self):
        """
        Обработка нажатия на кнопку "Отчет для одного банка"
        Остановка показа формы выбора отчета и переход к форме формирования отчета
        """
        self.reject()
        form_bank.FormBankReport(parent = self).show()

    def OnBankListPushButton(self):
        """
        Обработка нажатия на кнопку "Отчет для нескольких банков"
        Остановка показа формы выбора отчета и переход к форме формирования отчета
        """
        self.reject()
        form_bank.FormBankReport(parent = self).show()

