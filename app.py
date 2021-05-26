#!/Users/mikhailisakov/BankDB/BankApp/env/bin/python 
#sys.path.insert(0, '/Users/mikhailisakov/BankDB/BankApp/app')
from widgets import authorization
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication([])
    window = authorization.Authorization()
    window.show()
    # Start the event loop.
    app.exec()
