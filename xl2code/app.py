
import argparse
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QTextBrowser, QPushButton
from ui.panel_main_mediator import PanelMainMediator
from xlsettings import Xlsettings

# 取消或禁用控制台/终端的快速编辑模式
# kernel32 = ctypes.windll.kernel32
# kernel32.SetConsoleMode(kernel32.GetStdHandle(-10), (0x4 | 0x80 | 0x20 | 0x2 | 0x10 | 0x1 | 0x00 | 0x100))

class App:

    def __init__(self, batchMode) -> None:
        self.batchMode = batchMode
        self.setting = Xlsettings()
        self.start()
    
    def start(self):
        if self.batchMode:
            num = len(sys.argv)
            if num < 4:
                print("参数数量小于4个")
                return
            self.analysis_args()
            self.do_real_job()

        else:
            if not QApplication.instance():
                app = QApplication(sys.argv)
            else:
                app = QApplication.instance()
            mainWindow = PanelMainMediator()
            mainWindow.show()
            app.exec()

    def open_main_panel(self):
        pass

    def do_real_job(self):
        self.analysis_args()
        pass

    def analysis_args(self):
        parser = argparse.ArgumentParser("xl2code parameters inspection")
        parser.add_argument('input', help='excel所在目录')
        parser.add_argument('output', help='代码存储目录')
        parser.add_argument('-l', '--lang', default='lua', choices=['lua','csharp','java'], help='语言类型')
        parser.add_argument('-t', '--type', default='code', choices=['code','byte','pb'], help='生成的类型')
        parser.add_argument('-d', '--data', help='数据存储目录')
        args = parser.parse_args()

        self.setting.input = args.input
        self.setting.output = args.output
        self.setting.lang = args.lang
        self.setting.type = args.type
        self.setting.data = args.data