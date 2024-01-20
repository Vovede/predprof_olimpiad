import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit


class Expl(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 1600, 900)
        self.setWindowTitle("Мониторинг метеоданных")
        self.btn = QPushButton("решить", self)
        self.btn.move(750, 400)
        self.btn.resize(150, 50)
        self.btn.clicked.connect(self.txt)

        self.lbl = QLabel(self)
        self.lbl.move(800, 300)
        self.lbl.setText("ответ")
        self.lbl.resize(100, 100)

        self.textEdit = QLineEdit(self)
        self.textEdit.move(750, 300)
        self.textEdit.resize(150, 30)

    def txt(self):
        s = self.textEdit.text()
        self.lbl.setText(str(eval(s)))


app = QApplication(sys.argv)
ex = Expl()
ex.show()
sys.exit(app.exec())
