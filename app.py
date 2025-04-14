import sys
import sqlite3
from data.main_tables import MainTable
from project_const import MAIN_WINDOW_TITLE, MAIN_WINDOW_ICON
from PyQt6 import QtWidgets
from PyQt6.QtCore import QSize, Qt, QPoint
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidget, \
    QTableWidgetItem, QHBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(MAIN_WINDOW_TITLE)
        self.setWindowIcon(QIcon(MAIN_WINDOW_ICON))
        self.setMinimumSize(600, 400)

        layout = QHBoxLayout()

        self.tables = MainTable()

        layout.addWidget(self.tables.table_phones, 3)
        layout.addWidget(self.tables.table_lang_set, 2)
        layout.setContentsMargins(5,0,5,0)
        layout.setSpacing(10)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        with open("assets/styles.css", "r") as style_file:
            self.setStyleSheet(style_file.read())


app = QApplication(sys.argv)
main_window = MainWindow()
# with open("assets/styles.css","r") as file:
#     app.setStyleSheet(file.read())
main_window.show()
main_window.resize(1024, 600)
main_window.tables.load_data_phones()
main_window.tables.load_data_lang_set()
sys.exit(app.exec())