# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Тесты\v1_0.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainProgram(object):
    drawId = 1
    newDrawId = 1
    def setupUi(self, MainProgram):
        MainProgram.setObjectName("MainProgram")
        MainProgram.resize(800, 589)
        MainProgram.setMinimumSize(QtCore.QSize(400, 600))
        #MainProgram.setMaximumSize(QtCore.QSize(800, 800))
        self.centralwidget = QtWidgets.QWidget(MainProgram)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(17, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")

        self.cbox_forms = QtWidgets.QComboBox(self.centralwidget) 
        self.cbox_forms.addItems(["Diagrams","Lists","Conclusions"])
        self.cbox_forms.activated[str].connect(self.onChanged)

        self.verticalLayout.addWidget(self.textEdit)
        self.verticalLayout.addWidget(self.cbox_forms)
        #self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        #self.graphicsView.setObjectName("graphicsView")
        #self.verticalLayout.addWidget(self.graphicsView)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(48, 250, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(13, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout)


        spacerForIndex1 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        spacerForIndex2 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalBox = QtWidgets.QHBoxLayout()
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setObjectName("<")
        self.horizontalBox.addWidget(self.pushButton1)
        self.horizontalBox.addItem(spacerForIndex1)
        self.indexInfo = QtWidgets.QLabel(self.centralwidget)
        self.horizontalBox.addWidget(self.indexInfo)

        #self.horizontalBox.addWidget(self.self.cbox)
        self.horizontalBox.addItem(spacerForIndex2)
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setObjectName(">")
        self.horizontalBox.addWidget(self.pushButton2)
        self.verticalLayout_3.addLayout(self.horizontalBox)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        MainProgram.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainProgram)
        self.statusBar.setObjectName("statusBar")
        MainProgram.setStatusBar(self.statusBar)


        self.text1 = QtWidgets.QLabel(self.centralwidget)
        self.text2 = QtWidgets.QLabel(self.centralwidget)

        self.retranslateUi(MainProgram)
        QtCore.QMetaObject.connectSlotsByName(MainProgram)

    def retranslateUi(self, MainProgram):
        _translate = QtCore.QCoreApplication.translate
        MainProgram.setWindowTitle(_translate("MainProgram", "MainWindow"))
        self.pushButton.setText(_translate("MainProgram", "Начать обработку"))
        self.pushButton1.setText(_translate("MainProgram", "<-"))
        self.pushButton2.setText(_translate("MainProgram", "->"))

    def onChanged(self, text):
        if text == "Diagrams":
            self.newDrawId = 1
        if text == "Lists":
            self.newDrawId = 2
        if text == "Conclusions":
            self.newDrawId = 3
