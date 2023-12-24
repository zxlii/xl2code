# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'panel_main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGraphicsView, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_PanelMain(object):
    def setupUi(self, PanelMain):
        if not PanelMain.objectName():
            PanelMain.setObjectName(u"PanelMain")
        PanelMain.setEnabled(True)
        PanelMain.resize(428, 312)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PanelMain.sizePolicy().hasHeightForWidth())
        PanelMain.setSizePolicy(sizePolicy)
        PanelMain.setMinimumSize(QSize(428, 284))
        PanelMain.setMaximumSize(QSize(428, 428))
        PanelMain.setAutoFillBackground(False)
        self.actionexport = QAction(PanelMain)
        self.actionexport.setObjectName(u"actionexport")
        self.actiondoc = QAction(PanelMain)
        self.actiondoc.setObjectName(u"actiondoc")
        self.actionsave = QAction(PanelMain)
        self.actionsave.setObjectName(u"actionsave")
        self.actionquit = QAction(PanelMain)
        self.actionquit.setObjectName(u"actionquit")
        self.actionabout = QAction(PanelMain)
        self.actionabout.setObjectName(u"actionabout")
        self.actionExcel = QAction(PanelMain)
        self.actionExcel.setObjectName(u"actionExcel")
        self.action_4 = QAction(PanelMain)
        self.action_4.setObjectName(u"action_4")
        self.centralwidget = QWidget(PanelMain)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 408, 181))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setAutoFillBackground(False)

        self.horizontalLayout.addWidget(self.label)

        self.pathInput = QLineEdit(self.verticalLayoutWidget)
        self.pathInput.setObjectName(u"pathInput")

        self.horizontalLayout.addWidget(self.pathInput)

        self.btnInputFileDlg = QPushButton(self.verticalLayoutWidget)
        self.btnInputFileDlg.setObjectName(u"btnInputFileDlg")
        self.btnInputFileDlg.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout.addWidget(self.btnInputFileDlg)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.pathOutput = QLineEdit(self.verticalLayoutWidget)
        self.pathOutput.setObjectName(u"pathOutput")

        self.horizontalLayout_2.addWidget(self.pathOutput)

        self.btnOutputFileDlg = QPushButton(self.verticalLayoutWidget)
        self.btnOutputFileDlg.setObjectName(u"btnOutputFileDlg")
        self.btnOutputFileDlg.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_2.addWidget(self.btnOutputFileDlg)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.pathOutput_2 = QLineEdit(self.verticalLayoutWidget)
        self.pathOutput_2.setObjectName(u"pathOutput_2")

        self.horizontalLayout_5.addWidget(self.pathOutput_2)

        self.btnOutputFileDlg_2 = QPushButton(self.verticalLayoutWidget)
        self.btnOutputFileDlg_2.setObjectName(u"btnOutputFileDlg_2")
        self.btnOutputFileDlg_2.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_5.addWidget(self.btnOutputFileDlg_2)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.rdoCsharp = QRadioButton(self.verticalLayoutWidget)
        self.rdoCsharp.setObjectName(u"rdoCsharp")

        self.horizontalLayout_3.addWidget(self.rdoCsharp)

        self.rdoLua = QRadioButton(self.verticalLayoutWidget)
        self.rdoLua.setObjectName(u"rdoLua")

        self.horizontalLayout_3.addWidget(self.rdoLua)

        self.rdoJava = QRadioButton(self.verticalLayoutWidget)
        self.rdoJava.setObjectName(u"rdoJava")

        self.horizontalLayout_3.addWidget(self.rdoJava)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.rdoPb = QRadioButton(self.verticalLayoutWidget)
        self.rdoPb.setObjectName(u"rdoPb")

        self.horizontalLayout_4.addWidget(self.rdoPb)

        self.rdoBytes = QRadioButton(self.verticalLayoutWidget)
        self.rdoBytes.setObjectName(u"rdoBytes")

        self.horizontalLayout_4.addWidget(self.rdoBytes)

        self.rdoCode = QRadioButton(self.verticalLayoutWidget)
        self.rdoCode.setObjectName(u"rdoCode")

        self.horizontalLayout_4.addWidget(self.rdoCode)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.line_4 = QFrame(self.verticalLayoutWidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_4)

        self.btnCheck = QPushButton(self.centralwidget)
        self.btnCheck.setObjectName(u"btnCheck")
        self.btnCheck.setGeometry(QRect(260, 200, 151, 31))
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(20, 200, 81, 71))
        self.btnGen = QPushButton(self.centralwidget)
        self.btnGen.setObjectName(u"btnGen")
        self.btnGen.setGeometry(QRect(260, 240, 151, 31))
        self.graphicsView_2 = QGraphicsView(self.centralwidget)
        self.graphicsView_2.setObjectName(u"graphicsView_2")
        self.graphicsView_2.setGeometry(QRect(130, 200, 81, 71))
        PanelMain.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(PanelMain)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 428, 21))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_4 = QMenu(self.menubar)
        self.menu_4.setObjectName(u"menu_4")
        PanelMain.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(PanelMain)
        self.statusbar.setObjectName(u"statusbar")
        PanelMain.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menu.addAction(self.actionexport)
        self.menu.addAction(self.actionsave)
        self.menu.addAction(self.actionquit)
        self.menu_4.addAction(self.actiondoc)
        self.menu_4.addAction(self.actionabout)

        self.retranslateUi(PanelMain)

        QMetaObject.connectSlotsByName(PanelMain)
    # setupUi

    def retranslateUi(self, PanelMain):
        PanelMain.setWindowTitle(QCoreApplication.translate("PanelMain", u"xl2code", None))
        self.actionexport.setText(QCoreApplication.translate("PanelMain", u"\u5bfc\u5165(\u5bfc\u5165\u5df2\u6709\u8bbe\u7f6e)", None))
        self.actiondoc.setText(QCoreApplication.translate("PanelMain", u"\u6587\u6863", None))
        self.actionsave.setText(QCoreApplication.translate("PanelMain", u"\u4fdd\u5b58(\u4fdd\u5b58\u5f53\u524d\u8bbe\u7f6e)", None))
        self.actionquit.setText(QCoreApplication.translate("PanelMain", u"\u9000\u51fa", None))
        self.actionabout.setText(QCoreApplication.translate("PanelMain", u"\u5173\u4e8e", None))
        self.actionExcel.setText(QCoreApplication.translate("PanelMain", u"Excel\u6587\u4ef6", None))
        self.action_4.setText(QCoreApplication.translate("PanelMain", u"\u5bfc\u51fa\u8bbe\u7f6e", None))
        self.label.setText(QCoreApplication.translate("PanelMain", u"\u8f93\u5165\u8def\u5f84:", None))
        self.btnInputFileDlg.setText(QCoreApplication.translate("PanelMain", u"...", None))
        self.label_2.setText(QCoreApplication.translate("PanelMain", u"\u8f93\u51fa\u8def\u5f84:", None))
        self.pathOutput.setText("")
        self.btnOutputFileDlg.setText(QCoreApplication.translate("PanelMain", u"...", None))
        self.label_4.setText(QCoreApplication.translate("PanelMain", u"\u8f93\u51fa\u8def\u5f84:", None))
        self.pathOutput_2.setText("")
        self.btnOutputFileDlg_2.setText(QCoreApplication.translate("PanelMain", u"...", None))
        self.label_3.setText(QCoreApplication.translate("PanelMain", u"\u76ee\u6807\u8bed\u8a00:", None))
        self.rdoCsharp.setText(QCoreApplication.translate("PanelMain", u"C#", None))
        self.rdoLua.setText(QCoreApplication.translate("PanelMain", u"Lua", None))
        self.rdoJava.setText(QCoreApplication.translate("PanelMain", u"Java", None))
        self.label_5.setText(QCoreApplication.translate("PanelMain", u"\u8f93\u51fa\u683c\u5f0f:", None))
        self.rdoPb.setText(QCoreApplication.translate("PanelMain", u"PB-Bytes", None))
        self.rdoBytes.setText(QCoreApplication.translate("PanelMain", u"Bytes", None))
        self.rdoCode.setText(QCoreApplication.translate("PanelMain", u"Code", None))
        self.btnCheck.setText(QCoreApplication.translate("PanelMain", u"\u68c0\u67e5", None))
        self.btnGen.setText(QCoreApplication.translate("PanelMain", u"\u751f\u6210", None))
        self.menu.setTitle(QCoreApplication.translate("PanelMain", u"\u6587\u4ef6", None))
        self.menu_2.setTitle(QCoreApplication.translate("PanelMain", u"\u8bbe\u7f6e", None))
        self.menu_4.setTitle(QCoreApplication.translate("PanelMain", u"\u5e2e\u52a9", None))
    # retranslateUi

