import re
import generator
import time
import os


# mailto:[a-zA-Z0-9]+@[a-zA-Z0-9]+.[a-zA-Z]+(\?subject=[a-zA-Z0-9]{1,64})?

class Recognizer:
    def __init__(self, strings):

        self._f = open(os.path.join(os.getcwd(), 'Task1', "result_1.txt"), 'w')
        self.strings = strings
        self._result = {}

    def __del__(self):
        self._f.close()

    def recognize(self):
        n = time.perf_counter()
        j = 0
        for i in range(len(self.strings)):
            if re.fullmatch(r'[mM][aA][iI][Ll][Tt][Oo]:[a-zA-Z0-9]+@[a-zA-Z0-9]+[.][a-zA-Z]+(\?[Ss][Uu][Bb][Jj][eE][cC][Tt]=[a-zA-Z0-9]{1,64})?', self.strings[i]):
                self.AddToDict(self.strings[i].split(':')[1].split('@')[0])
                j += 1
                self._f.write(self.strings[i] + ' - yes'+'\n')
            else:
                self._f.write(self.strings[i] + ' - no'+'\n')
        n1 = time.perf_counter()
        self.printDict()
        self.saveRes()
        print(n1-n, j)

    def AddToDict(self, key):
        if self._result.get(key) is None:
            self._result[key] = 1
        else:
            num = self._result.get(key)
            self._result[key] = num+1

    def printDict(self):
        for key, item in self._result.items():
            print(key + ' - ' + str(item))

    def saveRes(self):
        f = open(os.path.join(os.getcwd(), 'Task1', "result1.txt"), 'w')
        for key, item in self._result.items():
            f.write(key + ' - ' + str(item)+'\n')
        f.close()


if __name__ == '__main__':
    gen = generator.Generator()
    addr = gen.getFileContent()
    rec = Recognizer(addr)
    rec.recognize()
    #a = 'mailto:dd124374s321@d.s,..dasd.ru'
    #print(re.fullmatch(r'[mM][aA][iI][Ll][Tt][Oo]:[a-zA-Z0-9]+@[a-zA-Z0-9]+[.][a-zA-Z]+(\?[Ss][Uu][Bb][Jj][eE][cC][Tt]=[a-zA-Z0-9]{1,64})?',a))

