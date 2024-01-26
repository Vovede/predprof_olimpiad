import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *

# from fileDataRead import *

class Monitoringiop(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('erty.ui', self)


        self.totalData = {}
        self.data = []
        self.liststations = set()
        self.sef = None

        self.navTab = {
            'Загрузка данных': [self.btnDownloadTab.clicked.connect(self.navigate), 1],
            'Визуализация данных': [self.btnVisualTab.clicked.connect(self.navigate), 2],
            'Анализ данных': [self.btnAnalizeTab.clicked.connect(self.navigate), 3],
            'Прогноз': [self.btnPredictTab.clicked.connect(self.navigate), 4],
            'Мониторинг': [self.btnMonitoringTab.clicked.connect(self.navigate), 5],
            'Экспорт': [self.btnExportTab.clicked.connect(self.navigate), 6]
        }

        self.downloadFileData.clicked.connect(self.loadTable)
        self.clearBtnTableWidget.clicked.connect(self.clearTableWidget)

        self.homeBtnDowloadTab.clicked.connect(self.homeGo)
        self.homeBtnVisualTab.clicked.connect(self.homeGo)
        self.homeBtnAnalisTab.clicked.connect(self.homeGo)
        self.homeBtnPredictTab.clicked.connect(self.homeGo)
        self.homeBtnMonitoringtab.clicked.connect(self.homeGo)

    def navigate(self):
        print(self.sender().text(), self.navTab[self.sender().text()][1])
        self.tabWidget.setCurrentIndex(self.navTab[self.sender().text()][1])

    def homeGo(self):
        self.tabWidget.setCurrentIndex(0)

    def clearTableWidget(self):
        self.tableWiget.clear()
        self.data = []

    def loadTable(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Monitoringiop()
    ex.show()
    sys.exit(app.exec_())
