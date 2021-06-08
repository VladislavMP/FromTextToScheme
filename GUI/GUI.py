import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen, QPainterPath
from PyQt5.QtCore import Qt, QRectF
import design
import diagrams
import lists
import conclusions

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainProgram):

    param1 = 10
    param2 = 10
    param3 = 10
    param4 = 10
    diagram = [[]]
    index = 0
    list = [[]]
    concl = [[]]
    drawId = 0
    max_index = 1

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.start_work)
        self.pushButton1.clicked.connect(self.decIndex)
        self.pushButton2.clicked.connect(self.incIndex)
        #sys.exit(app.exec_())

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        if self.drawId == 1 and len(self.diagram) > 1: self.drawRectangles(qp)
        if self.drawId == 2 and len(self.list) > 1: self.drawList(qp)
        if self.drawId == 3 and len(self.concl) > 1: 
            self.drawConcl(qp)
        qp.end()

    def drawT(self, qp, text, x, y):
        qp.drawText(x, y, text)

    def drawT(self, qp, text, x, y, width, height):
        rect = QRectF(x, y, width, height)
        qp.drawText(rect, Qt.TextWordWrap | Qt.AlignCenter, text)

    def drawArrowV(self, qp, xpoint, ypoint, xarrow, yarrow):
        path = QPainterPath()
        path.moveTo(xpoint + xarrow / 3, ypoint)
        path.lineTo(xpoint + xarrow / 3 * 2, ypoint)
        path.lineTo(xpoint + xarrow / 3 * 2, ypoint + yarrow / 4 * 3)
        path.lineTo(xpoint + xarrow, ypoint + yarrow / 4 * 3)
        path.lineTo(xpoint + xarrow / 2, ypoint + yarrow)
        path.lineTo(xpoint, ypoint + yarrow / 4 * 3)
        path.lineTo(xpoint + xarrow / 3, ypoint + yarrow / 4 * 3)
        path.lineTo(xpoint + xarrow / 3, ypoint)
        qp.drawPath(path)

    def drawArrowH(self, qp, xpoint, ypoint, xarrow, yarrow):
        path = QPainterPath()
        path.moveTo(xpoint, ypoint + yarrow / 3)
        path.lineTo(xpoint, ypoint + yarrow / 3 * 2) 
        path.lineTo(xpoint + xarrow / 4 * 3, ypoint + yarrow / 3 * 2) 
        path.lineTo(xpoint + xarrow / 4 * 3, ypoint + yarrow) 
        path.lineTo(xpoint + xarrow, ypoint + yarrow / 2) 
        path.lineTo(xpoint + xarrow / 4 * 3, ypoint) 
        path.lineTo(xpoint + xarrow / 4 * 3, ypoint + yarrow / 3)
        path.lineTo(xpoint, ypoint + yarrow / 3)
        qp.drawPath(path)

    def drawRectangles(self, qp):
        col = QColor(200, 200, 200)
        col.setNamedColor('#000000')
        qp.setPen(col)
        qp.setBrush(QColor(200, 0, 0))
        max = -1
        for i in range(len(self.diagram[self.index * 2])):
            self.diagram[self.index * 2][i] = float(self.diagram[self.index * 2][i])
        for i in range(len(self.diagram[self.index * 2])):
            if self.diagram[self.index * 2][i] > max:
                max = self.diagram[self.index * 2][i]
        for i in range(len(self.diagram[self.index * 2])):
        #self.diagram[self.index].sort()
        #for i in range(len(self.diagram[self.index])):
            height = self.diagram[self.index * 2][i]/max * 200
            xpoint = self.size().width()/(len(self.diagram[self.index * 2]) + 1) * (i + 1) - 30
            ypoint = self.size().height() - 150 - height
            width = 60
            qp.drawRect(xpoint, ypoint, width, height)
            self.drawT(qp, str(self.diagram[self.index * 2][i]), xpoint, ypoint + height - 10, 60, 60)
            qp.setBrush(QColor((150 * i) % 250, (75 * i) % 250, (30 * i) % 250))
        qp.setBrush(QColor(200, 0, 0))
        for i in range(len(self.diagram[self.index * 2 + 1])):
            ypoint = self.size().height() - 380 + 20 * i
            self.drawT(qp, str(self.diagram[self.index * 2 + 1][i]), 10, ypoint, 60, 60)
            qp.drawRect(5, ypoint + 25, 10, 10)
            qp.setBrush(QColor((150 * i) % 250, (75 * i) % 250, (30 * i) % 250))
    def drawList(self, qp):
        col = QColor(200, 200, 200)
        col.setNamedColor('#000000')
        qp.setPen(col)
        qp.setBrush(QColor(255, 255, 255))
        xpoint = 30
        ypoint = self.size().height() - 130 - 200
        xrect = self.size().width() - 60
        yrect = 50
        lines = 0
        last_line = 0
        qp.drawRect(xpoint, ypoint, xrect, yrect)
        self.drawT(qp, self.list[self.index][0], xpoint, ypoint, xrect, yrect) 
        lines = int((len(self.list[self.index]) - 1) / 3)
        count = 0
        current_line = 0
        for i in range(len(self.list[self.index])):
            if i != 0 and i<10:
                if current_line < lines:
                    xrect = (self.size().width() - 60) / 3
                else: xrect = (self.size().width() - 60) / ((len(self.list[self.index]) - 1) % 3 + 1)
                yrect = 40 
                xpoint = 30 + xrect * (i % 3)                                                   
                ypoint = self.size().height() - 230 + yrect * current_line
                qp.drawRect(xpoint, ypoint, xrect, yrect)
                self.drawT(qp, self.list[self.index][i], xpoint, ypoint, xrect, yrect)
                self.drawArrowV(qp, xpoint + xrect / 2, self.size().height() - 180 - 100, 25, 50)
                count = count + 1
                if (count == 3): 
                    current_line = current_line + 1
                    count = 0
                
    def drawConcl(self, qp):
        col = QColor(200, 200, 200)
        col.setNamedColor('#000000')
        qp.setPen(col)
        qp.setBrush(QColor(255, 255, 255))
        xpoint = 30
        ypoint = self.size().height() - 70 - 200
        xrect = (self.size().width() - 60) / 3
        yrect = 120
        qp.drawRect(xpoint, ypoint, xrect, yrect)
        self.drawT(qp, self.concl[self.index][0], xpoint, ypoint, xrect, yrect) 

        xpoint = (self.size().width() - 60) / 3 + 30 + 5
        xrect = (self.size().width() - 60) / 3 - 10
        yrect = 25
        ypoint = self.size().height() - 70 - 160 + yrect / 2

        self.drawArrowH(qp, xpoint, ypoint, xrect, yrect)

        xpoint = (self.size().width() - 60) / 3 * 2 + 30
        ypoint = self.size().height() - 70 - 200
        xrect = (self.size().width() - 60) / 3
        yrect = 120
        qp.drawRect(xpoint, ypoint, xrect, yrect)
        self.drawT(qp, self.concl[self.index][1], xpoint, ypoint, xrect, yrect) 

    def start_work(self):
        text = self.textEdit.toPlainText()
        self.diagram = diagrams.diagram(text)
        self.list = lists.list(text)
        self.concl = conclusions.concl(text)
        #self.diagram = [[123, 314],[]]
        #self.list = [["Для повышения выносливости применяют", "пробежки на длительные дистанции", "небольшие силовые упражнения", "124", "14", "35"], []]
        #self.concl = [["Идет дождь", "нужно взять зонт"]]
        #print(self.size().height())
        self.drawId = self.newDrawId
        self.index = 0
        if self.drawId == 1:
            self.max_index = int((len(self.diagram) - 1) / 2)
        if self.drawId == 2:
            self.max_index = len(self.list) - 1
        if self.drawId == 3:
            self.max_index = len(self.concl) - 1
        self.indexInfo.setText( str(self.index + 1) + "/" + str(self.max_index)) #  1/?
        self.update()

    def decIndex(self):
        self.index = self.index - 1 
        if self.index == -1:
            self.index = self.max_index - 1
        self.indexInfo.setText( str(self.index + 1) + "/" + str(self.max_index))
        self.update()

    def incIndex(self):
        self.index = self.index + 1 
        if self.index == self.max_index:
            self.index = 0
        self.indexInfo.setText(str(self.index + 1) + "/" + str(self.max_index))
        self.update()

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()