import sqlite3
import sys
import sys
import pathlib
from map import Ui_Form
from addEditCoffeeForm import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QStatusBar
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class main_proga(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Coffee")
        self.con = sqlite3.connect(r"C:\Users\Shiro\PycharmProjects\Git_nd_yellow_circles\data\coffee.sqlite")
        self.show_info()
        self.pushButton.clicked.connect(self.show_info)
        self.pushButton_2.clicked.connect(self.register)

    def closeEvent(self, event):
        self.con.close()

    def show_info(self):
        cur = self.con.cursor()
        result = cur.execute("SELECT * FROM tabl").fetchall()
        self.tw_top.setRowCount(len(result))
        self.tw_top.setColumnCount(len(result[0]))
        self.tw_top.setHorizontalHeaderLabels([description[0] for description in cur.description])
        self.tw_top.verticalHeader().setVisible(False)
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tw_top.setItem(i, j, QTableWidgetItem(str(val)))

    def register(self):
        self.w = register_now()
        self.w.show()


class register_now(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("addEditCoffeeForm")
        self.status = QStatusBar()
        self.pushButton.clicked.connect(self.run)

    def run(self):
        try:
            if len(self.stroka1.text()) > 0:
                name = self.stroka1.text()
            else:
                 raise Exception("Нету названия")
            if len(self.stroka2.text()) > 0:
                objarka = self.stroka2.text()
            else:
                 raise Exception("Не написали степень обжарки")
            if len(self.stroka3.text()) > 0 and self.stroka3.text().isdigit():
                count = self.stroka3.text()
            else:
                 raise Exception("Неправильно ввели цирфы! валюту не надо")
            if len(self.stroka4.text()) > 0 and self.stroka4.text().isdigit():
                ves = self.stroka4.text()
            else:
                 raise Exception("Неправильно ввели цирфы! вес уже в граммах")
            if len(self.stroka5.text()) > 0 :
                O_vkyse = self.stroka5.text()
            else:
                 raise Exception("Не написали о вкусе")
            self.statusBar().showMessage(str("Все успешно!"))
        except Exception as e:
            self.statusBar().showMessage(str(e))
            return -1
        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        id_new = cur.execute("SELECT * FROM tabl ORDER BY ID DESC").fetchone()
        string = f"INSERT INTO tabl ('ID', 'название сорта', 'степень обжарки', 'молотый/в зернах', " \
                 f"'описание вкуса', 'цена', 'объем упаковки')" \
                 f" VALUES('{id_new[0] + 1}', '{name}', '{objarka}', {int(self.comboBox.currentText())}, '{O_vkyse}', {count}, {ves})"
        cur.execute(string)
        con.commit()
        cur.close()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = main_proga()
    ex.show()
    sys.exit(app.exec())

