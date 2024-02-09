import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from matplotlib.figure import Figure
import random
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# from fileDataRead import *

class Monitoringiop(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('pytpyt.txt', self)


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
        self.pushBtnCheckboxesClear.clicked.connect(self.mainf)
        self.visualizationBtn.clicked.connect(self.mnte)
        self.clearBtnGraphView.clicked.connect(self.saus)
        self.pushButton_7.clicked.connect(self.file)
        self.clearBtnTableWidget.clicked.connect(self.delete)
        self.pushButton_12.clicked.connect(self.button)
        self.pushButton_11.clicked.connect(self.wefb)
        self.pushButton_10.clicked.connect(self.fgert)

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
        self.tableWidget.clear()
        self.data = []

    def loadTable(self):
        print('Загрузить из файла')

    def mainf(self): # сброс
        print('сброс')

    def mnte(self):
        print('визуализация')

    def saus(self):
        print('очистить')

    def file(self):
        print('Загрузить по ссылке')

    def delete(self):
        print('очистить2')

    def button(self):
        print('Обновить')

    def wefb(self):
        print('Прогноз')

    def fgert(self):
        # fig1 = plt.figure()
        # fig1.set_size_inches(5, 2.550)
        # x1 = [1, 2, 3, 4, 5, 45, 45, 23, 44, 56, 63, 23, 56]
        # y1 = [25, 32, 34, 20, 25, 45, 45, 23, 45, 45, 34, 45, 47]
        # er = plt.plot(x1, y1)

        self.scene1 = QGraphicsScene()
        self.graphicsView_3.setScene(self.scene1)
        self.figure1 = Figure()
        self.axes1 = self.figure1.gca()
        self.axes1.set_title("My Plot")
        x1 = [random.randrange(1, 2) for _ in range(10)]
        y1 = [random.randrange(1, 10) for _ in range(10)]
        self.axes1.clear()
        self.axes1.plot(x1, y1)
        self.canvas1 = FigureCanvas(self.figure1)
        self.proxy_widgeter = self.scene1.addWidget(self.canvas1)

        self.scene2 = QGraphicsScene()
        self.graphicsView_2.setScene(self.scene2)
        self.figure2 = Figure()
        self.axes2 = self.figure2.gca()
        self.axes2.set_title("My Plot")
        x2 = [random.randrange(1, 14) for _ in range(10)]
        y2 = [random.randrange(1, 14) for _ in range(10)]
        self.axes2.clear()
        self.axes2.plot(x2, y2)
        self.canvas2 = FigureCanvas(self.figure2)
        self.proxy_widgeter = self.scene2.addWidget(self.canvas2)

        self.scene4 = QGraphicsScene()
        self.graphicsView_4.setScene(self.scene4)
        self.figure4 = Figure()
        self.axes4 = self.figure4.gca()
        self.axes4.set_title("My Plot")
        x4 = [random.randrange(1, 14) for _ in range(5)]
        y4 = [random.randrange(1, 14) for _ in range(5)]
        self.axes4.clear()
        self.axes4.plot(x4, y4)
        self.canvas4 = FigureCanvas(self.figure4)
        self.proxy_widgeter = self.scene4.addWidget(self.canvas4)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Monitoringiop()
    ex.show()
    sys.exit(app.exec_())
