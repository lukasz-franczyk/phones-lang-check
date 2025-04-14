from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem
from data.connect_to_db import DatabaseConnection
import sqlite3


class MainTable(QTableWidget):
    def __init__(self):
        super().__init__()
        self.table_phones = QTableWidget()
        self.table_phones.setColumnCount(6)
        self.table_phones.setHorizontalHeaderLabels(('Id', 'Manufacturer', 'EAN', 'Code', 'Name', 'Set_id'))
        self.table_phones.verticalHeader().setVisible(False)
        self.table_phones.setColumnHidden(0, True)

        self.table_lang = QTableWidget()
        self.table_lang.setColumnCount(4)
        self.table_lang.setHorizontalHeaderLabels(('Id', 'ISO Name', 'Code', 'Endonyms'))
        self.table_lang.verticalHeader().setVisible(False)
        self.table_lang.setColumnHidden(0, True)

        self.table_lang_set = QTableWidget()
        self.table_lang_set.setColumnCount(3)
        self.table_lang_set.setHorizontalHeaderLabels(('Id', 'Set_nr', 'Sets'))
        self.table_lang_set.verticalHeader().setVisible(False)

    def load_data_phones(self):
        connection = DatabaseConnection().connect()
        result = connection.execute('SELECT * FROM Phones')
        self.table_phones.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.table_phones.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                print(row_data)
                self.table_phones.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                self.table_phones.resizeColumnsToContents()
        connection.close()

    def load_data_languages(self):
        connection = DatabaseConnection().connect()
        result = connection.execute('SELECT * FROM Languages_names')
        self.table_lang.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.table_lang.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table_lang.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                self.table_phones.resizeColumnsToContents()
        connection.close()

    def load_data(self):
        connection = DatabaseConnection().connect()
        result = connection.execute('SELECT id, ean, CONCAT(manufacturer, \' \', name) AS phone_name, languages FROM Phones')
        print(result)
        self.table_phones.setColumnCount(4)
        self.table_phones.setHorizontalHeaderLabels(('Id', 'EAN', 'Name', 'Languages'))
        self.table_phones.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.table_phones.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                print(row_data)
                self.table_phones.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                self.table_phones.resizeColumnsToContents()
        connection.close()

    def load_data_lang_set(self):
        connection = DatabaseConnection().connect()
        result = connection.execute('SELECT * FROM Languages_sets')
        self.table_lang_set.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.table_lang_set.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                print(row_data)
                self.table_lang_set.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                self.table_lang_set.resizeColumnsToContents()
        connection.close()