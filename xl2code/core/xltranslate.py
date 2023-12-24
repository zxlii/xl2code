class Xltranslate:
    def __init__(self, setting):
        self.setting = setting

    def Run(self):
        if not self.analysis():
            return
        self.execute()

    # 分析setting参数
    def analysis():
        return True
    
    # 开始执行
    def execute():
        pass