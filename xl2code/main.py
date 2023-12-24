import sys
# from xl2code.app import App
import argparse
from app import App
from xlsettings import Xlsettings


#main.py -i c:/test -o d:/aab -l lua -t pb
if __name__ == "__main__":

    # setting = Xlsettings()
    # parser = argparse.ArgumentParser("xl2code parameters inspection")
    # parser.add_argument('input', help='excel所在目录')
    # parser.add_argument('output', help='代码存储目录')
    # parser.add_argument('-l', '--lang', default='lua', choices=['lua','csharp','java'], help='语言类型')
    # parser.add_argument('-t', '--type', default='code', choices=['code','byte','pb'], help='生成的类型')
    # parser.add_argument('-d', '--data', help='数据存储目录')
    # args = parser.parse_args()

    # setting.input = args.input
    # setting.output = args.output
    # setting.lang = args.lang
    # setting.type = args.type
    # setting.data = args.data

    num = len(sys.argv)
    print(num)
    batchMode = num > 1
    app = App(batchMode)

    # print(args.input)
    # print(args.output)
    # print(args.lang)
    # print(args.type)
    # print(args.data)

    