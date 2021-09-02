# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(881, 541)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(7)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(881, 440))
        MainWindow.setInputMethodHints(QtCore.Qt.ImhNone)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(881, 413))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMinimumSize(QtCore.QSize(561, 111))
        self.groupBox.setSizeIncrement(QtCore.QSize(7, 0))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.langLabel = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.langLabel.setFont(font)
        self.langLabel.setObjectName("langLabel")
        self.verticalLayout.addWidget(self.langLabel)
        self.lengthLabel = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lengthLabel.setFont(font)
        self.lengthLabel.setObjectName("lengthLabel")
        self.verticalLayout.addWidget(self.lengthLabel)
        self.completedLabel = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.completedLabel.setFont(font)
        self.completedLabel.setObjectName("completedLabel")
        self.verticalLayout.addWidget(self.completedLabel)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_5.addWidget(self.line)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scoreLabel = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.scoreLabel.setFont(font)
        self.scoreLabel.setObjectName("scoreLabel")
        self.verticalLayout_2.addWidget(self.scoreLabel)
        self.wwLabel = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.wwLabel.setFont(font)
        self.wwLabel.setObjectName("wwLabel")
        self.verticalLayout_2.addWidget(self.wwLabel)
        self.statusLabel = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.statusLabel.setFont(font)
        self.statusLabel.setObjectName("statusLabel")
        self.verticalLayout_2.addWidget(self.statusLabel)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.line_2 = QtWidgets.QFrame(self.groupBox)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_5.addWidget(self.line_2)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lombardLabel = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lombardLabel.setFont(font)
        self.lombardLabel.setObjectName("lombardLabel")
        self.verticalLayout_6.addWidget(self.lombardLabel)
        self.noiseLabel = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.noiseLabel.setFont(font)
        self.noiseLabel.setObjectName("noiseLabel")
        self.verticalLayout_6.addWidget(self.noiseLabel)
        self.noiseLabel_2 = QtWidgets.QLabel(self.groupBox)
        self.noiseLabel_2.setEnabled(True)
        self.noiseLabel_2.setMinimumSize(QtCore.QSize(153, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.noiseLabel_2.setFont(font)
        self.noiseLabel_2.setFocusPolicy(QtCore.Qt.TabFocus)
        self.noiseLabel_2.setObjectName("noiseLabel_2")
        self.verticalLayout_6.addWidget(self.noiseLabel_2)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        self.line_3 = QtWidgets.QFrame(self.groupBox)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_5.addWidget(self.line_3)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setMinimumSize(QtCore.QSize(100, 23))
        self.pushButton.setMaximumSize(QtCore.QSize(125, 23))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setMinimumSize(QtCore.QSize(124, 23))
        self.pushButton_2.setMaximumSize(QtCore.QSize(124, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_3.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setMinimumSize(QtCore.QSize(124, 20))
        self.pushButton_3.setMaximumSize(QtCore.QSize(124, 20))
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_3.addWidget(self.pushButton_3)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_10.addLayout(self.horizontalLayout_5)
        self.horizontalLayout.addWidget(self.groupBox)
        self.logoLabel = QtWidgets.QLabel(self.centralwidget)
        self.logoLabel.setMinimumSize(QtCore.QSize(251, 91))
        self.logoLabel.setMaximumSize(QtCore.QSize(251, 91))
        self.logoLabel.setText("")
        self.logoLabel.setPixmap(QtGui.QPixmap(":/images/vortex_logo_2.png"))
        self.logoLabel.setScaledContents(True)
        self.logoLabel.setObjectName("logoLabel")
        self.horizontalLayout.addWidget(self.logoLabel)
        self.verticalLayout_9.addLayout(self.horizontalLayout)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(861, 151))
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_4.setSpacing(8)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.verticalLayout_4.addWidget(self.tableWidget)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.precBox = QtWidgets.QTextBrowser(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.precBox.sizePolicy().hasHeightForWidth())
        self.precBox.setSizePolicy(sizePolicy)
        self.precBox.setObjectName("precBox")
        self.verticalLayout_5.addWidget(self.precBox)
        self.commandsLabel = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.commandsLabel.sizePolicy().hasHeightForWidth())
        self.commandsLabel.setSizePolicy(sizePolicy)
        self.commandsLabel.setObjectName("commandsLabel")
        self.verticalLayout_5.addWidget(self.commandsLabel)
        self.commandsBox = QtWidgets.QListWidget(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.commandsBox.sizePolicy().hasHeightForWidth())
        self.commandsBox.setSizePolicy(sizePolicy)
        self.commandsBox.setDragEnabled(False)
        self.commandsBox.setAlternatingRowColors(False)
        self.commandsBox.setObjectName("commandsBox")
        item = QtWidgets.QListWidgetItem()
        self.commandsBox.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.commandsBox.addItem(item)
        self.verticalLayout_5.addWidget(self.commandsBox)
        self.expectedLabel = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.expectedLabel.sizePolicy().hasHeightForWidth())
        self.expectedLabel.setSizePolicy(sizePolicy)
        self.expectedLabel.setObjectName("expectedLabel")
        self.verticalLayout_5.addWidget(self.expectedLabel)
        self.expectedBox = QtWidgets.QListWidget(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.expectedBox.sizePolicy().hasHeightForWidth())
        self.expectedBox.setSizePolicy(sizePolicy)
        self.expectedBox.setObjectName("expectedBox")
        self.verticalLayout_5.addWidget(self.expectedBox)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.horizontalLayout_4.setStretch(0, 4)
        self.horizontalLayout_4.setStretch(1, 9)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_4)
        self.verticalLayout_9.addWidget(self.groupBox_2)
        self.verticalLayout_11.addLayout(self.verticalLayout_9)
        self.verticalLayout_13.addLayout(self.verticalLayout_11)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.playButton = QtWidgets.QPushButton(self.centralwidget)
        self.playButton.setMinimumSize(QtCore.QSize(261, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.playButton.setFont(font)
        self.playButton.setToolTip("Play command")
        self.playButton.setToolTipDuration(-1)
        self.playButton.setShortcut("P")
        self.playButton.setObjectName("playButton")
        self.horizontalLayout_7.addWidget(self.playButton)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_7.addLayout(self.horizontalLayout_9)
        self.repeatButton = QtWidgets.QPushButton(self.centralwidget)
        self.repeatButton.setMinimumSize(QtCore.QSize(61, 41))
        self.repeatButton.setMaximumSize(QtCore.QSize(61, 41))
        self.repeatButton.setToolTip("Repeat current command")
        self.repeatButton.setObjectName("repeatButton")
        self.horizontalLayout_7.addWidget(self.repeatButton)
        self.cancel_button = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_button.setMinimumSize(QtCore.QSize(61, 41))
        self.cancel_button.setMaximumSize(QtCore.QSize(61, 41))
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout_7.addWidget(self.cancel_button)
        self.printButton = QtWidgets.QPushButton(self.centralwidget)
        self.printButton.setMinimumSize(QtCore.QSize(181, 41))
        self.printButton.setMaximumSize(QtCore.QSize(181, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.printButton.setFont(font)
        self.printButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.printButton.setToolTip("Make .csv file from the test results")
        self.printButton.setObjectName("printButton")
        self.horizontalLayout_7.addWidget(self.printButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_7.addLayout(self.horizontalLayout_10)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.wavLabel = QtWidgets.QLabel(self.centralwidget)
        self.wavLabel.setMinimumSize(QtCore.QSize(279, 17))
        self.wavLabel.setObjectName("wavLabel")
        self.verticalLayout_7.addWidget(self.wavLabel)
        self.gainLabel = QtWidgets.QLabel(self.centralwidget)
        self.gainLabel.setMinimumSize(QtCore.QSize(279, 16))
        self.gainLabel.setObjectName("gainLabel")
        self.verticalLayout_7.addWidget(self.gainLabel)
        self.horizontalLayout_7.addLayout(self.verticalLayout_7)
        self.verticalLayout_12.addLayout(self.horizontalLayout_7)
        spacerItem1 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_12.addItem(spacerItem1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setMinimumSize(QtCore.QSize(0, 40))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_3.addWidget(self.progressBar)
        spacerItem2 = QtWidgets.QSpacerItem(17, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_12.addLayout(self.horizontalLayout_3)
        self.verticalLayout_13.addLayout(self.verticalLayout_12)
        self.gridLayout.addLayout(self.verticalLayout_13, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 881, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOnline_guide = QtWidgets.QAction(MainWindow)
        self.actionOnline_guide.setObjectName("actionOnline_guide")
        self.actionResume = QtWidgets.QAction(MainWindow)
        self.actionResume.setObjectName("actionResume")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionAudio_device = QtWidgets.QAction(MainWindow)
        self.actionAudio_device.setObjectName("actionAudio_device")
        self.actionView_testlog = QtWidgets.QAction(MainWindow)
        self.actionView_testlog.setObjectName("actionView_testlog")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionResume)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionView_testlog)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionAudio_device)
        self.menuFile.addAction(self.actionQuit)
        self.menuAbout.addAction(self.actionOnline_guide)
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.commandsBox.setCurrentRow(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Current test"))
        self.langLabel.setText(_translate("MainWindow", "Lang:"))
        self.lengthLabel.setText(_translate("MainWindow", "Test length: "))
        self.completedLabel.setText(_translate("MainWindow", "Status: "))
        self.scoreLabel.setText(_translate("MainWindow", "Score: "))
        self.wwLabel.setText(_translate("MainWindow", "WW accuracy:"))
        self.statusLabel.setText(_translate("MainWindow", "Status: RUNNING"))
        self.lombardLabel.setText(_translate("MainWindow", "Lombard effect: enabled..."))
        self.noiseLabel.setText(_translate("MainWindow", "BG noise"))
        self.noiseLabel_2.setText(_translate("MainWindow", "BG noise + radio: "))
        self.pushButton.setText(_translate("MainWindow", "Disable"))
        self.pushButton_2.setText(_translate("MainWindow", "Measure"))
        self.pushButton_3.setText(_translate("MainWindow", "Measure"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Test x of x"))
        self.label_3.setText(_translate("MainWindow", "Test selection"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Result"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Note"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Timestamp"))
        self.label.setText(_translate("MainWindow", "Preconditions"))
        self.precBox.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.commandsLabel.setText(_translate("MainWindow", "Commands"))
        __sortingEnabled = self.commandsBox.isSortingEnabled()
        self.commandsBox.setSortingEnabled(False)
        item = self.commandsBox.item(0)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.commandsBox.item(1)
        item.setText(_translate("MainWindow", "New Item"))
        self.commandsBox.setSortingEnabled(__sortingEnabled)
        self.expectedLabel.setText(_translate("MainWindow", "Expected behaviour"))
        self.playButton.setText(_translate("MainWindow", "Play command"))
        self.repeatButton.setText(_translate("MainWindow", "Repeat"))
        self.repeatButton.setShortcut(_translate("MainWindow", "R"))
        self.cancel_button.setText(_translate("MainWindow", "Cancel"))
        self.cancel_button.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.printButton.setStatusTip(_translate("MainWindow", "Begin the test"))
        self.printButton.setText(_translate("MainWindow", "Print .CSV"))
        self.wavLabel.setText(_translate("MainWindow", "Wave file: "))
        self.gainLabel.setText(_translate("MainWindow", "Gain adjust:"))
        self.label_2.setText(_translate("MainWindow", "Progress"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "Help"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setStatusTip(_translate("MainWindow", "Start a new test"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOnline_guide.setText(_translate("MainWindow", "Manual"))
        self.actionOnline_guide.setStatusTip(_translate("MainWindow", "Visit the GitHub page of the creator"))
        self.actionOnline_guide.setShortcut(_translate("MainWindow", "F1"))
        self.actionResume.setText(_translate("MainWindow", "Resume..."))
        self.actionResume.setStatusTip(_translate("MainWindow", "Resume a test"))
        self.actionResume.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setStatusTip(_translate("MainWindow", "Quit the application"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionAbout.setStatusTip(_translate("MainWindow", "Version, metadata, generic information"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionAudio_device.setText(_translate("MainWindow", "Settings"))
        self.actionView_testlog.setText(_translate("MainWindow", "Consult testlog"))
from . import gui_imgs_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
