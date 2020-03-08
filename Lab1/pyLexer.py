import PLY.parserClass as parser
import os


class PLY():
    def __init__(self, file=False):
        self.parser = parser.MyParser(file)
        self.res = os.path.join(os.getcwd(), 'Task3', 'result_3.txt')
        self.dict = os.path.join(os.getcwd(), 'Task3', 'result3.txt')
        self.time = os.path.join(os.getcwd(), 'Task3', 'time3.txt')
        self.parser._overload_file = self.dict
        self.parser._result_file = self.res
        self.A = dict()

    def parse_from_file(self, string):
        self.parser.check_string(string)

    def parse_from_console(self):
        self.A.clear()
        working = True
        print('Input your line or "stop" to exit:')

        while working:
            user_string = input()
            if user_string == "stop":
                break
            if user_string != "":
                user_string += ("\n")
            self.parser.check_string(user_string)
            if self.parser.get_A().keys():
                print("- yes\n")
                res = list(self.parser.get_A().keys())[0]
                # добавляем её в массив
                if self.A.get(res) is None:
                    self.A.setdefault(res, 1)
                else:
                    self.A[res] += 1
            else:
                print("- no\n")
        print('Statistic: \n')
        for key in self.A:
            if self.A.get(key) >= 1:
                print(str(key) + ' ' + str(self.A.get(key)) + '\n')

    def printDict(self):
        for key, item in self.parser.a.items():
            print(key + ' - ' + str(item))

    def saveRes(self):
        f = open(self.dict, 'w')
        for key, item in self.parser.a.items():
            f.write(key + ' - ' + str(item) + '\n')
        f.close()
        self.null()

    def saveTime(self, time):
        f = open(self.time, 'w')
        f.write(str(time) + '\n')
        f.write(str(self.parser.count))
        f.close()
        self.null()

    def null(self):
        self.parser.a = {}

    def changeFile(self):
        self.parser._file = not self.parser._file
