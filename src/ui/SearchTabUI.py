# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src\ui\SearchTab.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(990, 790)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 3, 1, 1)
        self.searchTypeCombo = QtWidgets.QComboBox(Dialog)
        self.searchTypeCombo.setObjectName("searchTypeCombo")
        self.searchTypeCombo.addItem("")
        self.searchTypeCombo.addItem("")
        self.searchTypeCombo.addItem("")
        self.searchTypeCombo.addItem("")
        self.searchTypeCombo.addItem("")
        self.searchTypeCombo.addItem("")
        self.searchTypeCombo.addItem("")
        self.gridLayout.addWidget(self.searchTypeCombo, 1, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 5, 1, 1)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 5, 1, 1)
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 4, 3, 1, 1)
        self.graphMinDepthSpin = QtWidgets.QSpinBox(Dialog)
        self.graphMinDepthSpin.setMinimum(1)
        self.graphMinDepthSpin.setProperty("value", 1)
        self.graphMinDepthSpin.setObjectName("graphMinDepthSpin")
        self.gridLayout.addWidget(self.graphMinDepthSpin, 4, 4, 1, 1)
        self.graphDepthSpin = QtWidgets.QSpinBox(Dialog)
        self.graphDepthSpin.setMinimum(1)
        self.graphDepthSpin.setMaximum(99)
        self.graphDepthSpin.setProperty("value", 5)
        self.graphDepthSpin.setObjectName("graphDepthSpin")
        self.gridLayout.addWidget(self.graphDepthSpin, 3, 4, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.minProfitSpinBox = QtWidgets.QSpinBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minProfitSpinBox.sizePolicy().hasHeightForWidth())
        self.minProfitSpinBox.setSizePolicy(sizePolicy)
        self.minProfitSpinBox.setMinimum(100)
        self.minProfitSpinBox.setMaximum(99999999)
        self.minProfitSpinBox.setProperty("value", 1000)
        self.minProfitSpinBox.setObjectName("minProfitSpinBox")
        self.horizontalLayout.addWidget(self.minProfitSpinBox)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 5, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.startingsystemlayout = QtWidgets.QHBoxLayout()
        self.startingsystemlayout.setObjectName("startingsystemlayout")
        self.currentSystemCombo = QtWidgets.QComboBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentSystemCombo.sizePolicy().hasHeightForWidth())
        self.currentSystemCombo.setSizePolicy(sizePolicy)
        self.currentSystemCombo.setMinimumSize(QtCore.QSize(100, 0))
        self.currentSystemCombo.setEditable(True)
        self.currentSystemCombo.setMaxVisibleItems(100)
        self.currentSystemCombo.setObjectName("currentSystemCombo")
        self.startingsystemlayout.addWidget(self.currentSystemCombo)
        self.currentStationCombo = QtWidgets.QComboBox(Dialog)
        self.currentStationCombo.setMinimumSize(QtCore.QSize(100, 0))
        self.currentStationCombo.setEditable(True)
        self.currentStationCombo.setMaxVisibleItems(100)
        self.currentStationCombo.setObjectName("currentStationCombo")
        self.startingsystemlayout.addWidget(self.currentStationCombo)
        self.getCurrentBtn = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.getCurrentBtn.sizePolicy().hasHeightForWidth())
        self.getCurrentBtn.setSizePolicy(sizePolicy)
        self.getCurrentBtn.setObjectName("getCurrentBtn")
        self.startingsystemlayout.addWidget(self.getCurrentBtn)
        self.gridLayout.addLayout(self.startingsystemlayout, 1, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.maxDistanceSpinBox = QtWidgets.QSpinBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maxDistanceSpinBox.sizePolicy().hasHeightForWidth())
        self.maxDistanceSpinBox.setSizePolicy(sizePolicy)
        self.maxDistanceSpinBox.setMinimumSize(QtCore.QSize(75, 0))
        self.maxDistanceSpinBox.setMinimum(1)
        self.maxDistanceSpinBox.setMaximum(500)
        self.maxDistanceSpinBox.setProperty("value", 50)
        self.maxDistanceSpinBox.setObjectName("maxDistanceSpinBox")
        self.gridLayout.addWidget(self.maxDistanceSpinBox, 1, 6, 1, 1)
        self.windowCountSpinBox = QtWidgets.QSpinBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.windowCountSpinBox.sizePolicy().hasHeightForWidth())
        self.windowCountSpinBox.setSizePolicy(sizePolicy)
        self.windowCountSpinBox.setMinimumSize(QtCore.QSize(75, 0))
        self.windowCountSpinBox.setMinimum(1)
        self.windowCountSpinBox.setMaximum(9999999)
        self.windowCountSpinBox.setProperty("value", 1)
        self.windowCountSpinBox.setObjectName("windowCountSpinBox")
        self.gridLayout.addWidget(self.windowCountSpinBox, 4, 6, 1, 1)
        self.windowSizeSpinBox = QtWidgets.QSpinBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.windowSizeSpinBox.sizePolicy().hasHeightForWidth())
        self.windowSizeSpinBox.setSizePolicy(sizePolicy)
        self.windowSizeSpinBox.setMinimumSize(QtCore.QSize(75, 0))
        self.windowSizeSpinBox.setMinimum(100)
        self.windowSizeSpinBox.setMaximum(999999)
        self.windowSizeSpinBox.setProperty("value", 200)
        self.windowSizeSpinBox.setObjectName("windowSizeSpinBox")
        self.gridLayout.addWidget(self.windowSizeSpinBox, 3, 6, 1, 1)
        self.targetsystemlayout = QtWidgets.QHBoxLayout()
        self.targetsystemlayout.setObjectName("targetsystemlayout")
        self.targetSystemCombo = QtWidgets.QComboBox(Dialog)
        self.targetSystemCombo.setMinimumSize(QtCore.QSize(100, 0))
        self.targetSystemCombo.setEditable(True)
        self.targetSystemCombo.setMaxVisibleItems(100)
        self.targetSystemCombo.setObjectName("targetSystemCombo")
        self.targetsystemlayout.addWidget(self.targetSystemCombo)
        self.targetStationCombo = QtWidgets.QComboBox(Dialog)
        self.targetStationCombo.setMinimumSize(QtCore.QSize(100, 0))
        self.targetStationCombo.setEditable(True)
        self.targetStationCombo.setMaxVisibleItems(100)
        self.targetStationCombo.setObjectName("targetStationCombo")
        self.targetsystemlayout.addWidget(self.targetStationCombo)
        self.targetGetCurrentBtn = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.targetGetCurrentBtn.sizePolicy().hasHeightForWidth())
        self.targetGetCurrentBtn.setSizePolicy(sizePolicy)
        self.targetGetCurrentBtn.setObjectName("targetGetCurrentBtn")
        self.targetsystemlayout.addWidget(self.targetGetCurrentBtn)
        self.gridLayout.addLayout(self.targetsystemlayout, 3, 2, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout)
        self.searchBtn = QtWidgets.QPushButton(Dialog)
        self.searchBtn.setAutoDefault(False)
        self.searchBtn.setDefault(False)
        self.searchBtn.setObjectName("searchBtn")
        self.verticalLayout_5.addWidget(self.searchBtn)
        self.SearchResultTable = QtWidgets.QTableView(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SearchResultTable.sizePolicy().hasHeightForWidth())
        self.SearchResultTable.setSizePolicy(sizePolicy)
        self.SearchResultTable.setToolTipDuration(1)
        self.SearchResultTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
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
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.retranslateUi(Dialog)
        self.searchTypeCombo.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.currentSystemCombo, self.getCurrentBtn)
        Dialog.setTabOrder(self.getCurrentBtn, self.searchTypeCombo)
        Dialog.setTabOrder(self.searchTypeCombo, self.graphDepthSpin)
        Dialog.setTabOrder(self.graphDepthSpin, self.graphMinDepthSpin)
        Dialog.setTabOrder(self.graphMinDepthSpin, self.searchBtn)
        Dialog.setTabOrder(self.searchBtn, self.SearchResultTable)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_8.setText(_translate("Dialog", "Max hops"))
        self.searchTypeCombo.setToolTip(_translate("Dialog", "<html><head/><body><pre align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"file-elitemerchantreadme-LC94\"/><span style=\" font-family:\'Courier New,courier\';\">- - -</span><span style=\" font-family:\'Courier New,courier\';\"> Exports from current station - - -</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"file-elitemerchantreadme-LC95\"/><span style=\" font-family:\'Courier New,courier\';\">T</span><span style=\" font-family:\'Courier New,courier\';\">his attempts to find an outgoing trade route from the current station.</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"file-elitemerchantreadme-LC96\"/><span style=\" font-family:\'Courier New,courier\';\">T</span><span style=\" font-family:\'Courier New,courier\';\">his is triggered by automatic searches as your location updates.</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"file-elitemerchantreadme-LC97\"/><span style=\" font-family:\'Courier New,courier\';\">I</span><span style=\" font-family:\'Courier New,courier\';\">f you write a different system to the &quot;starting system&quot; field, exports from</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"file-elitemerchantreadme-LC98\"/><span style=\" font-family:\'Courier New,courier\';\">t</span><span style=\" font-family:\'Courier New,courier\';\">his system are shown instead.</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"file-elitemerchantreadme-LC99\"/><span style=\" font-family:\'Courier New,courier\';\">I</span><span style=\" font-family:\'Courier New,courier\';\">f you are getting 0 results, try reducing min/max hops to 1 and lowering </span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"file-elitemerchantreadme-LC100\"/><span style=\" font-family:\'Courier New,courier\';\">m</span><span style=\" font-family:\'Courier New,courier\';\">inimum profit. But it is also possible you are at a dead-end.</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"file-elitemerchantreadme-LC101\"/><span style=\" font-family:\'Courier New,courier\';\">T</span><span style=\" font-family:\'Courier New,courier\';\">his is why it\'s advisable to always have min hops set to 2 to minimize the</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"file-elitemerchantreadme-LC102\"/><span style=\" font-family:\'Courier New,courier\';\">d</span><span style=\" font-family:\'Courier New,courier\';\">anger of deadends.</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"file-elitemerchantreadme-LC103\"/><span style=\" font-family:\'Courier New,courier\';\">- - --</span><span style=\" font-family:\'Courier New,courier\';\"> Exports from current system - - -</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"file-elitemerchantreadme-LC104\"/><span style=\" font-family:\'Courier New,courier\';\">S</span><span style=\" font-family:\'Courier New,courier\';\">ame as current station, but shows all stations in the system.</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"file-elitemerchantreadme-LC105\"/><span style=\" font-family:\'Courier New,courier\';\">T</span><span style=\" font-family:\'Courier New,courier\';\">his is triggered by automatic searches as your location updates.</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"file-elitemerchantreadme-LC106\"/><span style=\" font-family:\'Courier New,courier\';\">- - -</span><span style=\" font-family:\'Courier New,courier\';\"> Loop route - - -</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"file-elitemerchantreadme-LC107\"/><span style=\" font-family:\'Courier New,courier\';\">T</span><span style=\" font-family:\'Courier New,courier\';\">his finds trade routes which end up in the starting station.</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"file-elitemerchantreadme-LC108\"/><span style=\" font-family:\'Courier New,courier\';\">T</span><span style=\" font-family:\'Courier New,courier\';\">he loops are ordered by profit/h.</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"file-elitemerchantreadme-LC109\"/><span style=\" font-family:\'Courier New,courier\';\">F</span><span style=\" font-family:\'Courier New,courier\';\">or more variety, add a few minimum hops.</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"file-elitemerchantreadme-LC110\"/><span style=\" font-family:\'Courier New,courier\';\">- - -</span><span style=\" font-family:\'Courier New,courier\';\"> Long route - - -</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"file-elitemerchantreadme-LC111\"/><span style=\" font-family:\'Courier New,courier\';\">T</span><span style=\" font-family:\'Courier New,courier\';\">his finds connecting trade routes and arranges them by profit/h.</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"file-elitemerchantreadme-LC112\"/><span style=\" font-family:\'Courier New,courier\';\">S</span><span style=\" font-family:\'Courier New,courier\';\">etting minimum hops to a bigger value gives you a grand tour of the galaxy</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"file-elitemerchantreadme-LC113\"/><span style=\" font-family:\'Courier New,courier\';\">w</span><span style=\" font-family:\'Courier New,courier\';\">ith no repeated stations.</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"file-elitemerchantreadme-LC114\"/><span style=\" font-family:\'Courier New,courier\';\">T</span><span style=\" font-family:\'Courier New,courier\';\">he end of the route may be a deadend or a route the optimization algorithm</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"file-elitemerchantreadme-LC115\"/><span style=\" font-family:\'Courier New,courier\';\">d</span><span style=\" font-family:\'Courier New,courier\';\">eems unprofitable. Using \'Exports from current system\' is a recommended</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"file-elitemerchantreadme-LC116\"/><span style=\" font-family:\'Courier New,courier\';\">a</span><span style=\" font-family:\'Courier New,courier\';\">ction after finishing a long route.</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"file-elitemerchantreadme-LC117\"/><span style=\" font-family:\'Courier New,courier\';\">- - -</span><span style=\" font-family:\'Courier New,courier\';\"> Single trades - - -</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"file-elitemerchantreadme-LC118\"/><span style=\" font-family:\'Courier New,courier\';\">T</span><span style=\" font-family:\'Courier New,courier\';\">his is the traditional min-max single one direction trade search available</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"file-elitemerchantreadme-LC119\"/><span style=\" font-family:\'Courier New,courier\';\">e</span><span style=\" font-family:\'Courier New,courier\';\">verywhere. For the sake of nostalgia.</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"file-elitemerchantreadme-LC120\"/><span style=\" font-family:\'Courier New,courier\';\">- - -</span><span style=\" font-family:\'Courier New,courier\';\"> Long route on way to target - - -</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"file-elitemerchantreadme-LC121\"/><span style=\" font-family:\'Courier New,courier\';\">W</span><span style=\" font-family:\'Courier New,courier\';\">ith this you can pick a target system and calculate a high profit series of</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"file-elitemerchantreadme-LC122\"/><span style=\" font-family:\'Courier New,courier\';\">t</span><span style=\" font-family:\'Courier New,courier\';\">rade hops between the starting system and your target.</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"file-elitemerchantreadme-LC123\"/><span style=\" font-family:\'Courier New,courier\';\">I</span><span style=\" font-family:\'Courier New,courier\';\">t is essentially \'long route\' search, with the additional criteria that</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"file-elitemerchantreadme-LC124\"/><span style=\" font-family:\'Courier New,courier\';\">e</span><span style=\" font-family:\'Courier New,courier\';\">ach hop must be closer to your target.</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"file-elitemerchantreadme-LC125\"/><span style=\" font-family:\'Courier New,courier\';\">N</span><span style=\" font-family:\'Courier New,courier\';\">ote that a profitable route to target is not guaranteed and the route may</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"file-elitemerchantreadme-LC126\"/><span style=\" font-family:\'Courier New,courier\';\">e</span><span style=\" font-family:\'Courier New,courier\';\">nd somewhere near the target. Also the route is not direct and might wander</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"file-elitemerchantreadme-LC127\"/><span style=\" font-family:\'Courier New,courier\';\">q</span><span style=\" font-family:\'Courier New,courier\';\">uite a bit on the way, spiraling down toward your target as dictated by</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"file-elitemerchantreadme-LC128\"/><span style=\" font-family:\'Courier New,courier\';\">p</span><span style=\" font-family:\'Courier New,courier\';\">rofit/h.</span></pre></body></html>"))
        self.searchTypeCombo.setItemText(0, _translate("Dialog", "Exports from current Station"))
        self.searchTypeCombo.setItemText(1, _translate("Dialog", "Exports from current System"))
        self.searchTypeCombo.setItemText(2, _translate("Dialog", "Loop route"))
        self.searchTypeCombo.setItemText(3, _translate("Dialog", "Long route"))
        self.searchTypeCombo.setItemText(4, _translate("Dialog", "Single trades"))
        self.searchTypeCombo.setItemText(5, _translate("Dialog", "Long route on way to Target"))
        self.searchTypeCombo.setItemText(6, _translate("Dialog", "Direct current to target trades"))
        self.label_2.setText(_translate("Dialog", "Search window size"))
        self.label_5.setText(_translate("Dialog", "Target system"))
        self.label_7.setText(_translate("Dialog", "Search Type"))
        self.label_6.setText(_translate("Dialog", "Search windows"))
        self.label_14.setText(_translate("Dialog", "Min hops"))
        self.graphMinDepthSpin.setToolTip(_translate("Dialog", "<html><head/><body><pre align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\';\">Require at least this many trade stops before accepting a trade route.</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\';\">This has some impact on search time, but not to a significant degree.</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\';\">It\'s fun to pick \'long route\' search and set this to a high value for</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\';\">a grand tour.</span></pre></body></html>"))
        self.graphDepthSpin.setToolTip(_translate("Dialog", "<html><head/><body><pre align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\';\">How many trade stops do we want at most with our search.</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\';\">This value is primarily for optimizing searches with too much data.</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\';\">This may be necessary if you set min profit too low or max distance</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\';\">too high.</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\';\">If you\'re worried about a setting, set this to 1 and give it a go.</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\';\">If it\'s still fast, bump it to 2 and see how it goes.</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\';\">For most use you can confidently set this at 99 and no route will</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\';\">ever reach it, due to the route optimization algorithm culling</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\';\">the tail as the average profit/h falls.</span></pre></body></html>"))
        self.minProfitSpinBox.setToolTip(_translate("Dialog", "<html><head/><body><pre align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\';\">This is a hard limit for basic single trade exchange.<br/>Its primary function is to limit the number of<br/>possibilities and speed up searching.<br/>1000 is a good fast value for most trading, but might<br/>give low or no results if you\'re desperate or in a<br/>short range vessel.</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\';\">WARNING! DATA DROWNING HAZARD!</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\';\">Lowering this will flood the tool with more trade data.</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\';\">If you set this lower, please also limit max hops<br/>and/or search windows.</span></pre></body></html>"))
        self.label_3.setText(_translate("Dialog", "Max distance"))
        self.label.setText(_translate("Dialog", "Starting system"))
        self.getCurrentBtn.setText(_translate("Dialog", "Current"))
        self.label_4.setText(_translate("Dialog", "Min profit"))
        self.maxDistanceSpinBox.setToolTip(_translate("Dialog", "<html><head/><body><pre align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\';\">This is the maximum distance in light years a trade route can be at.</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\';\">This is primarily an optimization parameter, as higher than 50ly is</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\';\">rarely more profitable due to the distance(=time) cost. For smaller</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\';\">vessels with smaller tanks or jump ranges it\'s a good idea to lower</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\';\">this further for performance.</span></pre></body></html>"))
        self.windowCountSpinBox.setToolTip(_translate("Dialog", "<html><head/><body><pre align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\';\">How many windows should we search? Setting this to 1 will search the cube of set</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\';\">size centered around the current system. The default is 7, which is the current</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\';\">and 6 closest search windows. To search galaxy-wide, set this to 9999999999999.</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\';\">At window size 200, the galaxy size is just 64 windows, so it is not that heavy</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\';\">of an operation - just impractical for constant use, where 7 is  a nice balance.</span></pre></body></html>"))
        self.windowSizeSpinBox.setToolTip(_translate("Dialog", "<html><head/><body><pre align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\';\">The data is queried from the galaxy in cubes of this size.(value 200 -&gt; 200^3ly)</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\';\">Purely an optimization option. You may play around with this but 200 seems pretty</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\';\">fast. Multiple search windows overlap by the amount of your current max distance</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\';\">so no trade routes are missed, so for efficiency reasons it\'s good to have this</span></pre><pre align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\';\">significantly larger than that value.</span></pre></body></html>"))
        self.targetSystemCombo.setToolTip(_translate("Dialog", "<html><head/><body><p>Only used for &quot;long route on way to target&quot; search.</p></body></html>"))
        self.targetGetCurrentBtn.setText(_translate("Dialog", "Current"))
        self.searchBtn.setText(_translate("Dialog", "Search"))

