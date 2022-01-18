import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from view import MainView

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    root = MainView.MainView()
    root.setupUi(mainWindow)
    root.show()
    sys.exit(app.exec_())
