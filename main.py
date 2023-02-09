import sqlite3
import sys
from map import Ui_Form
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem

class Qwidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Coffee")
        self.con = sqlite3.connect("coffee.sqlite")
        cur = self.con.cursor()
        self.show_info()


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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Qwidget()
    ex.show()
    sys.exit(app.exec())

