# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pydemowindow.ui'
#
# Created: Thu Oct 13 14:42:07 2011
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_PyDemoWindow(object):
    def setupUi(self, PyDemoWindow):
        PyDemoWindow.setObjectName(_fromUtf8("PyDemoWindow"))
        PyDemoWindow.resize(722, 747)
        self.centralwidget = QtGui.QWidget(PyDemoWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.horizontalLayout.addWidget(self.graphicsView)
        PyDemoWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(PyDemoWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 722, 18))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        PyDemoWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(PyDemoWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        PyDemoWindow.setStatusBar(self.statusbar)
        self.dockWidget = QtGui.QDockWidget(PyDemoWindow)
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(self.dockWidgetContents)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.textEdit = QtGui.QTextEdit(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout.addWidget(self.textEdit)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(self.dockWidgetContents)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.dockWidgetContents)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.dockWidgetContents)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.label_13 = QtGui.QLabel(self.dockWidgetContents)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout.addWidget(self.label_13, 4, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.dockWidgetContents)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.frameWidthBox = QtGui.QSpinBox(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameWidthBox.sizePolicy().hasHeightForWidth())
        self.frameWidthBox.setSizePolicy(sizePolicy)
        self.frameWidthBox.setMinimumSize(QtCore.QSize(64, 0))
        self.frameWidthBox.setProperty(_fromUtf8("value"), 2)
        self.frameWidthBox.setObjectName(_fromUtf8("frameWidthBox"))
        self.gridLayout.addWidget(self.frameWidthBox, 5, 10, 1, 1)
        self.label_12 = QtGui.QLabel(self.dockWidgetContents)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout.addWidget(self.label_12, 7, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.scaleDownBox = QtGui.QSpinBox(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scaleDownBox.sizePolicy().hasHeightForWidth())
        self.scaleDownBox.setSizePolicy(sizePolicy)
        self.scaleDownBox.setMinimumSize(QtCore.QSize(64, 0))
        self.scaleDownBox.setMaximum(9999)
        self.scaleDownBox.setObjectName(_fromUtf8("scaleDownBox"))
        self.horizontalLayout_2.addWidget(self.scaleDownBox)
        self.label_3 = QtGui.QLabel(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 10, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 17, 0, 1, 1)
        self.label_14 = QtGui.QLabel(self.dockWidgetContents)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout.addWidget(self.label_14, 8, 0, 1, 1)
        self.label_15 = QtGui.QLabel(self.dockWidgetContents)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout.addWidget(self.label_15, 12, 0, 1, 1)
        self.label_16 = QtGui.QLabel(self.dockWidgetContents)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout.addWidget(self.label_16, 9, 0, 1, 1)
        self.label_17 = QtGui.QLabel(self.dockWidgetContents)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout.addWidget(self.label_17, 10, 0, 1, 1)
        self.leftPaddingBox = QtGui.QSpinBox(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftPaddingBox.sizePolicy().hasHeightForWidth())
        self.leftPaddingBox.setSizePolicy(sizePolicy)
        self.leftPaddingBox.setMinimumSize(QtCore.QSize(64, 0))
        self.leftPaddingBox.setProperty(_fromUtf8("value"), 40)
        self.leftPaddingBox.setObjectName(_fromUtf8("leftPaddingBox"))
        self.gridLayout.addWidget(self.leftPaddingBox, 12, 10, 1, 1)
        self.rightPaddingBox = QtGui.QSpinBox(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightPaddingBox.sizePolicy().hasHeightForWidth())
        self.rightPaddingBox.setSizePolicy(sizePolicy)
        self.rightPaddingBox.setMinimumSize(QtCore.QSize(64, 0))
        self.rightPaddingBox.setProperty(_fromUtf8("value"), 40)
        self.rightPaddingBox.setObjectName(_fromUtf8("rightPaddingBox"))
        self.gridLayout.addWidget(self.rightPaddingBox, 10, 10, 1, 1)
        self.topPaddingBox = QtGui.QSpinBox(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topPaddingBox.sizePolicy().hasHeightForWidth())
        self.topPaddingBox.setSizePolicy(sizePolicy)
        self.topPaddingBox.setMinimumSize(QtCore.QSize(64, 0))
        self.topPaddingBox.setProperty(_fromUtf8("value"), 40)
        self.topPaddingBox.setObjectName(_fromUtf8("topPaddingBox"))
        self.gridLayout.addWidget(self.topPaddingBox, 9, 10, 1, 1)
        self.label_18 = QtGui.QLabel(self.dockWidgetContents)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout.addWidget(self.label_18, 11, 0, 1, 1)
        self.bottomPaddingBox = QtGui.QSpinBox(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bottomPaddingBox.sizePolicy().hasHeightForWidth())
        self.bottomPaddingBox.setSizePolicy(sizePolicy)
        self.bottomPaddingBox.setMinimumSize(QtCore.QSize(64, 0))
        self.bottomPaddingBox.setProperty(_fromUtf8("value"), 10)
        self.bottomPaddingBox.setObjectName(_fromUtf8("bottomPaddingBox"))
        self.gridLayout.addWidget(self.bottomPaddingBox, 11, 10, 1, 1)
        self.label_19 = QtGui.QLabel(self.dockWidgetContents)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayout.addWidget(self.label_19, 13, 0, 1, 1)
        self.textIntervalBox = QtGui.QSpinBox(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textIntervalBox.sizePolicy().hasHeightForWidth())
        self.textIntervalBox.setSizePolicy(sizePolicy)
        self.textIntervalBox.setMinimumSize(QtCore.QSize(64, 0))
        self.textIntervalBox.setProperty(_fromUtf8("value"), 10)
        self.textIntervalBox.setObjectName(_fromUtf8("textIntervalBox"))
        self.gridLayout.addWidget(self.textIntervalBox, 13, 10, 1, 1)
        self.label_20 = QtGui.QLabel(self.dockWidgetContents)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout.addWidget(self.label_20, 14, 0, 1, 1)
        self.bottomTextPaddingBox = QtGui.QSpinBox(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bottomTextPaddingBox.sizePolicy().hasHeightForWidth())
        self.bottomTextPaddingBox.setSizePolicy(sizePolicy)
        self.bottomTextPaddingBox.setMinimumSize(QtCore.QSize(64, 0))
        self.bottomTextPaddingBox.setProperty(_fromUtf8("value"), 20)
        self.bottomTextPaddingBox.setObjectName(_fromUtf8("bottomTextPaddingBox"))
        self.gridLayout.addWidget(self.bottomTextPaddingBox, 14, 10, 1, 1)
        self.backgroundColorEdit = QtGui.QLineEdit(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backgroundColorEdit.sizePolicy().hasHeightForWidth())
        self.backgroundColorEdit.setSizePolicy(sizePolicy)
        self.backgroundColorEdit.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier"))
        self.backgroundColorEdit.setFont(font)
        self.backgroundColorEdit.setText(_fromUtf8("#000000"))
        self.backgroundColorEdit.setObjectName(_fromUtf8("backgroundColorEdit"))
        self.gridLayout.addWidget(self.backgroundColorEdit, 2, 10, 1, 1)
        self.fontColorEdit = QtGui.QLineEdit(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fontColorEdit.sizePolicy().hasHeightForWidth())
        self.fontColorEdit.setSizePolicy(sizePolicy)
        self.fontColorEdit.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier"))
        self.fontColorEdit.setFont(font)
        self.fontColorEdit.setText(_fromUtf8("#ffffff"))
        self.fontColorEdit.setObjectName(_fromUtf8("fontColorEdit"))
        self.gridLayout.addWidget(self.fontColorEdit, 3, 10, 1, 1)
        self.frameColorEdit = QtGui.QLineEdit(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameColorEdit.sizePolicy().hasHeightForWidth())
        self.frameColorEdit.setSizePolicy(sizePolicy)
        self.frameColorEdit.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier"))
        self.frameColorEdit.setFont(font)
        self.frameColorEdit.setText(_fromUtf8("#ffffff"))
        self.frameColorEdit.setObjectName(_fromUtf8("frameColorEdit"))
        self.gridLayout.addWidget(self.frameColorEdit, 4, 10, 1, 1)
        self.label_7 = QtGui.QLabel(self.dockWidgetContents)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.frameSpacingBox = QtGui.QSpinBox(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameSpacingBox.sizePolicy().hasHeightForWidth())
        self.frameSpacingBox.setSizePolicy(sizePolicy)
        self.frameSpacingBox.setMinimumSize(QtCore.QSize(64, 0))
        self.frameSpacingBox.setProperty(_fromUtf8("value"), 5)
        self.frameSpacingBox.setObjectName(_fromUtf8("frameSpacingBox"))
        self.gridLayout.addWidget(self.frameSpacingBox, 6, 10, 1, 1)
        self.label_8 = QtGui.QLabel(self.dockWidgetContents)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 15, 0, 1, 1)
        self.imageQualityBox = QtGui.QSpinBox(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageQualityBox.sizePolicy().hasHeightForWidth())
        self.imageQualityBox.setSizePolicy(sizePolicy)
        self.imageQualityBox.setMinimumSize(QtCore.QSize(64, 0))
        self.imageQualityBox.setMaximum(100)
        self.imageQualityBox.setProperty(_fromUtf8("value"), 85)
        self.imageQualityBox.setObjectName(_fromUtf8("imageQualityBox"))
        self.gridLayout.addWidget(self.imageQualityBox, 15, 10, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.bigFontComboBox = QtGui.QFontComboBox(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bigFontComboBox.sizePolicy().hasHeightForWidth())
        self.bigFontComboBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times"))
        font.setPointSize(32)
        self.bigFontComboBox.setCurrentFont(font)
        self.bigFontComboBox.setObjectName(_fromUtf8("bigFontComboBox"))
        self.horizontalLayout_3.addWidget(self.bigFontComboBox)
        self.bigFontSizeBox = QtGui.QSpinBox(self.dockWidgetContents)
        self.bigFontSizeBox.setMinimum(1)
        self.bigFontSizeBox.setProperty(_fromUtf8("value"), 32)
        self.bigFontSizeBox.setObjectName(_fromUtf8("bigFontSizeBox"))
        self.horizontalLayout_3.addWidget(self.bigFontSizeBox)
        self.gridLayout.addLayout(self.horizontalLayout_3, 7, 10, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.smallFontComboBox = QtGui.QFontComboBox(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.smallFontComboBox.sizePolicy().hasHeightForWidth())
        self.smallFontComboBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(20)
        self.smallFontComboBox.setCurrentFont(font)
        self.smallFontComboBox.setObjectName(_fromUtf8("smallFontComboBox"))
        self.horizontalLayout_4.addWidget(self.smallFontComboBox)
        self.smallFontSizeBox = QtGui.QSpinBox(self.dockWidgetContents)
        self.smallFontSizeBox.setMinimum(1)
        self.smallFontSizeBox.setProperty(_fromUtf8("value"), 20)
        self.smallFontSizeBox.setObjectName(_fromUtf8("smallFontSizeBox"))
        self.horizontalLayout_4.addWidget(self.smallFontSizeBox)
        self.gridLayout.addLayout(self.horizontalLayout_4, 8, 10, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.dockWidget.setWidget(self.dockWidgetContents)
        PyDemoWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget)
        self.actionOpen = QtGui.QAction(PyDemoWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.action = QtGui.QAction(PyDemoWindow)
        self.action.setObjectName(_fromUtf8("action"))
        self.actionExit = QtGui.QAction(PyDemoWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionSaveAs = QtGui.QAction(PyDemoWindow)
        self.actionSaveAs.setObjectName(_fromUtf8("actionSaveAs"))
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(PyDemoWindow)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL(_fromUtf8("triggered()")), PyDemoWindow.close)
        QtCore.QMetaObject.connectSlotsByName(PyDemoWindow)

    def retranslateUi(self, PyDemoWindow):
        PyDemoWindow.setWindowTitle(QtGui.QApplication.translate("PyDemoWindow", "PyDemo", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("PyDemoWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("PyDemoWindow", "Text:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("PyDemoWindow", "Scale down to", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("PyDemoWindow", "Background color", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("PyDemoWindow", "Font color", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("PyDemoWindow", "Frame color", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("PyDemoWindow", "Frame width", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("PyDemoWindow", "Big font", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("PyDemoWindow", "pixels", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("PyDemoWindow", "Small font", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("PyDemoWindow", "Left padding", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("PyDemoWindow", "Top padding", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("PyDemoWindow", "Right padding", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("PyDemoWindow", "Bottom padding", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("PyDemoWindow", "Text interval", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("PyDemoWindow", "Bottom text padding", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("PyDemoWindow", "Frame spacing", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("PyDemoWindow", "Image quality", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("PyDemoWindow", "&Open...", None, QtGui.QApplication.UnicodeUTF8))
        self.action.setText(QtGui.QApplication.translate("PyDemoWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("PyDemoWindow", "E&xit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveAs.setText(QtGui.QApplication.translate("PyDemoWindow", "&Save as...", None, QtGui.QApplication.UnicodeUTF8))

