from widgets import connection
from PyQt5.QtWidgets import QApplication
if __name__ == '__main__':
    """Главная функция приложения"""
    app = QApplication([])
    window = connection.Connection()
    window.show()
    #Start the event loop.
    app.exec()
