from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QTextBrowser, QPushButton
from ui.panel_main import Ui_PanelMain

class PanelMainMediator(QMainWindow, Ui_PanelMain):
    def __init__(self):
        super().__init__()

        # 初始化 UI
        self.ui = Ui_PanelMain()
        self.ui.setupUi(self)

        # # 获取UI文件中的小部件对象
        # self.textbrowser = self.ui.textBrowser
        # self.bt_1 = self.ui.bt_1
        # self.bt_2 = self.ui.bt_2
        # self.bt_3 = self.ui.bt_3
        # self.bt_4 = self.ui.bt_4
        # self.bt_5 = self.ui.bt_5
        # self.bt_6 = self.ui.bt_6
        # self.bt_7 = self.ui.bt_7
        # self.bt_8 = self.ui.bt_8
        # self.bt_9 = self.ui.bt_9
        # self.bt_0 = self.ui.bt_0
        # self.bt_add = self.ui.bt_add
        # self.bt_divide = self.ui.bt_divide
        # self.bt_CE = self.ui.bt_CE
        # self.bt_minus = self.ui.bt_minus
        # self.bt_multiply = self.ui.bt_multiply
        # self.bt_equal = self.ui.bt_equal

        # # 连接信号和槽
        # self.bt_1.clicked.connect(self.bt_click)
        # self.bt_2.clicked.connect(self.bt_click)
        # self.bt_3.clicked.connect(self.bt_click)
        # self.bt_4.clicked.connect(self.bt_click)
        # self.bt_5.clicked.connect(self.bt_click)
        # self.bt_6.clicked.connect(self.bt_click)
        # self.bt_7.clicked.connect(self.bt_click)
        # self.bt_8.clicked.connect(self.bt_click)
        # self.bt_9.clicked.connect(self.bt_click)
        # self.bt_0.clicked.connect(self.bt_click)
        # self.bt_add.clicked.connect(self.bt_add_click)
        # self.bt_equal.clicked.connect(self.bt_equal_click)
        # self.bt_divide.clicked.connect(self.bt_divide_click)
        # self.bt_CE.clicked.connect(self.bt_CE_click)
        # self.bt_multiply.clicked.connect(self.bt_multiply_click)
        # self.bt_minus.clicked.connect(self.bt_minus_click)