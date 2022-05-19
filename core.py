
from PySide2.QtWidgets import QApplication
from notas import MainWindow
import sys

app = QApplication()

window = MainWindow()
window.show()

sys.exit(app.exec_())