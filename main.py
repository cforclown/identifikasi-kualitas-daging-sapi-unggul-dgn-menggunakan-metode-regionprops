import sys
from PySide2.QtWidgets import QApplication
from View.View import View


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow=View()
    sys.exit(app.exec_())
