# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src\ui\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1465, 1042)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.maxDistanceTxt = QtWidgets.QLineEdit(self.tab)
        self.maxDistanceTxt.setObjectName("maxDistanceTxt")
        self.gridLayout.addWidget(self.maxDistanceTxt, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.currentSystemTxt = QtWidgets.QLineEdit(self.tab)
        self.currentSystemTxt.setObjectName("currentSystemTxt")
        self.horizontalLayout_3.addWidget(self.currentSystemTxt)
        self.getCurrentBtn = QtWidgets.QPushButton(self.tab)
        self.getCurrentBtn.setObjectName("getCurrentBtn")
        self.horizontalLayout_3.addWidget(self.getCurrentBtn)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.minProfitTxt = QtWidgets.QLineEdit(self.tab)
        self.minProfitTxt.setObjectName("minProfitTxt")
        self.horizontalLayout.addWidget(self.minProfitTxt)
        self.profitPhChk = QtWidgets.QCheckBox(self.tab)
        self.profitPhChk.setObjectName("profitPhChk")
        self.horizontalLayout.addWidget(self.profitPhChk)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 1, 1, 1)
        self.windowCountTxt = QtWidgets.QLineEdit(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.windowCountTxt.sizePolicy().hasHeightForWidth())
        self.windowCountTxt.setSizePolicy(sizePolicy)
        self.windowCountTxt.setObjectName("windowCountTxt")
        self.gridLayout.addWidget(self.windowCountTxt, 4, 5, 1, 1)
        self.windowSizeTxt = QtWidgets.QLineEdit(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.windowSizeTxt.sizePolicy().hasHeightForWidth())
        self.windowSizeTxt.setSizePolicy(sizePolicy)
        self.windowSizeTxt.setObjectName("windowSizeTxt")
        self.gridLayout.addWidget(self.windowSizeTxt, 3, 5, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 4, 1, 1)
        self.minPadSizeCombo = QtWidgets.QComboBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minPadSizeCombo.sizePolicy().hasHeightForWidth())
        self.minPadSizeCombo.setSizePolicy(sizePolicy)
        self.minPadSizeCombo.setObjectName("minPadSizeCombo")
        self.minPadSizeCombo.addItem("")
        self.minPadSizeCombo.addItem("")
        self.minPadSizeCombo.addItem("")
        self.gridLayout.addWidget(self.minPadSizeCombo, 1, 5, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 4, 1, 1)
        self.searchTypeCombo = QtWidgets.QComboBox(self.tab)
        self.searchTypeCombo.setObjectName("searchTypeCombo")
        self.searchTypeCombo.addItem("")
        self.searchTypeCombo.addItem("")
        self.searchTypeCombo.addItem("")
        self.searchTypeCombo.addItem("")
        self.gridLayout.addWidget(self.searchTypeCombo, 1, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 2, 1, 1)
        self.graphDepthSpin = QtWidgets.QSpinBox(self.tab)
        self.graphDepthSpin.setMinimum(1)
        self.graphDepthSpin.setMaximum(99)
        self.graphDepthSpin.setProperty("value", 3)
        self.graphDepthSpin.setObjectName("graphDepthSpin")
        self.gridLayout.addWidget(self.graphDepthSpin, 3, 3, 1, 1)
        self.graphMinDepthSpin = QtWidgets.QSpinBox(self.tab)
        self.graphMinDepthSpin.setMinimum(1)
        self.graphMinDepthSpin.setProperty("value", 1)
        self.graphMinDepthSpin.setObjectName("graphMinDepthSpin")
        self.gridLayout.addWidget(self.graphMinDepthSpin, 4, 3, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 4, 2, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout)
        self.searchBtn = QtWidgets.QPushButton(self.tab)
        self.searchBtn.setAutoDefault(False)
        self.searchBtn.setDefault(False)
        self.searchBtn.setObjectName("searchBtn")
        self.verticalLayout_5.addWidget(self.searchBtn)
        self.SearchResultTable = QtWidgets.QTableView(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SearchResultTable.sizePolicy().hasHeightForWidth())
        self.SearchResultTable.setSizePolicy(sizePolicy)
        self.SearchResultTable.setToolTipDuration(1)
        self.SearchResultTable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.SearchResultTable.setSortingEnabled(False)
        self.SearchResultTable.setCornerButtonEnabled(False)
        self.SearchResultTable.setObjectName("SearchResultTable")
        self.SearchResultTable.horizontalHeader().setCascadingSectionResizes(True)
        self.SearchResultTable.horizontalHeader().setHighlightSections(False)
        self.SearchResultTable.horizontalHeader().setMinimumSectionSize(10)
        self.SearchResultTable.horizontalHeader().setSortIndicatorShown(False)
        self.SearchResultTable.horizontalHeader().setStretchLastSection(False)
        self.SearchResultTable.verticalHeader().setVisible(False)
        self.SearchResultTable.verticalHeader().setCascadingSectionResizes(False)
        self.SearchResultTable.verticalHeader().setHighlightSections(False)
        self.verticalLayout_5.addWidget(self.SearchResultTable)
        self.verticalLayout_4.addLayout(self.verticalLayout_5)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)
        self.unladenRangeTxt = QtWidgets.QLineEdit(self.tab_2)
        self.unladenRangeTxt.setObjectName("unladenRangeTxt")
        self.gridLayout_2.addWidget(self.unladenRangeTxt, 0, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 1)
        self.currentlyNearAtTxt = QtWidgets.QLineEdit(self.tab_2)
        self.currentlyNearAtTxt.setReadOnly(True)
        self.currentlyNearAtTxt.setObjectName("currentlyNearAtTxt")
        self.gridLayout_2.addWidget(self.currentlyNearAtTxt, 3, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 2, 0, 1, 1)
        self.currenlyAtSystemTxt = QtWidgets.QLineEdit(self.tab_2)
        self.currenlyAtSystemTxt.setReadOnly(True)
        self.currenlyAtSystemTxt.setObjectName("currenlyAtSystemTxt")
        self.gridLayout_2.addWidget(self.currenlyAtSystemTxt, 2, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 3, 0, 1, 1)
        self.loadedRangeTXt = QtWidgets.QLineEdit(self.tab_2)
        self.loadedRangeTXt.setObjectName("loadedRangeTXt")
        self.gridLayout_2.addWidget(self.loadedRangeTXt, 1, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 4, 0, 1, 1)
        self.dockingRequestStatusTxt = QtWidgets.QLineEdit(self.tab_2)
        self.dockingRequestStatusTxt.setReadOnly(True)
        self.dockingRequestStatusTxt.setObjectName("dockingRequestStatusTxt")
        self.gridLayout_2.addWidget(self.dockingRequestStatusTxt, 4, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.statusMessageTxt = QtWidgets.QLabel(self.centralwidget)
        self.statusMessageTxt.setText("")
        self.statusMessageTxt.setObjectName("statusMessageTxt")
        self.horizontalLayout_2.addWidget(self.statusMessageTxt)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_6.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1465, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.editMenu = QtWidgets.QMenu(self.menubar)
        self.editMenu.setObjectName("editMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.optionsMenu = QtWidgets.QAction(MainWindow)
        self.optionsMenu.setObjectName("optionsMenu")
        self.exitMenu = QtWidgets.QAction(MainWindow)
        self.exitMenu.setObjectName("exitMenu")
        self.menuFile.addAction(self.exitMenu)
        self.editMenu.addAction(self.optionsMenu)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.editMenu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.minPadSizeCombo.setCurrentIndex(2)
        self.searchTypeCombo.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Elite Merchant"))
        self.label_3.setText(_translate("MainWindow", "Max distance"))
        self.maxDistanceTxt.setText(_translate("MainWindow", "30"))
        self.label_4.setText(_translate("MainWindow", "Min profit"))
        self.currentSystemTxt.setText(_translate("MainWindow", "Sol"))
        self.getCurrentBtn.setText(_translate("MainWindow", "Get current"))
        self.label.setText(_translate("MainWindow", "Current system"))
        self.minProfitTxt.setText(_translate("MainWindow", "1000"))
        self.profitPhChk.setText(_translate("MainWindow", "Cr/h"))
        self.windowCountTxt.setText(_translate("MainWindow", "1"))
        self.windowSizeTxt.setText(_translate("MainWindow", "100"))
        self.label_6.setText(_translate("MainWindow", "Search windows"))
        self.label_2.setText(_translate("MainWindow", "Search window size"))
        self.minPadSizeCombo.setItemText(0, _translate("MainWindow", "any"))
        self.minPadSizeCombo.setItemText(1, _translate("MainWindow", "M"))
        self.minPadSizeCombo.setItemText(2, _translate("MainWindow", "L"))
        self.label_5.setText(_translate("MainWindow", "Min pad size"))
        self.searchTypeCombo.setItemText(0, _translate("MainWindow", "Single trip"))
        self.searchTypeCombo.setItemText(1, _translate("MainWindow", "Round trip"))
        self.searchTypeCombo.setItemText(2, _translate("MainWindow", "Loop route"))
        self.searchTypeCombo.setItemText(3, _translate("MainWindow", "Long route"))
        self.label_7.setText(_translate("MainWindow", "Search Type"))
        self.label_8.setText(_translate("MainWindow", "Max hops"))
        self.label_14.setText(_translate("MainWindow", "Min hops"))
        self.searchBtn.setText(_translate("MainWindow", "Search"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Profit search"))
        self.label_9.setText(_translate("MainWindow", "Ship unladen jump range"))
        self.label_10.setText(_translate("MainWindow", "Ship fully loaded jump range"))
        self.label_11.setText(_translate("MainWindow", "Current system"))
        self.label_12.setText(_translate("MainWindow", "Curretly near at"))
        self.label_13.setText(_translate("MainWindow", "Docking request sent"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Ship status"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.editMenu.setTitle(_translate("MainWindow", "Edit"))
        self.optionsMenu.setText(_translate("MainWindow", "Options"))
        self.exitMenu.setText(_translate("MainWindow", "Exit"))

