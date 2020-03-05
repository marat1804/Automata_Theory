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
            match = re.fullmatch(
                r'[mM][aA][iI][Ll][Tt][Oo]:([a-zA-Z0-9]+)@[a-zA-Z0-9]+\.[a-zA-Z]+(\?[Ss][Uu][Bb][Jj][eE][cC][Tt]=[a-zA-Z0-9]{1,64})?',
                self.strings[i])
            if match is not None:
                self.AddToDict(match[1])
                j += 1
                self._f.write(self.strings[i] + ' - yes' + '\n')
            else:
                self._f.write(self.strings[i] + ' - no' + '\n')
        n1 = time.perf_counter()
        self.printDict()
        self.saveRes()
        self.saveTime(n1-n, j)
        print(n1 - n, j)

    def recognise(self, inn):
        match = re.fullmatch(
            r'[mM][aA][iI][Ll][Tt][Oo]:([a-zA-Z0-9]+)@[a-zA-Z0-9]+\.[a-zA-Z]+(\?[Ss][Uu][Bb][Jj][eE][cC][Tt]=[a-zA-Z0-9]{1,64})?',
            inn)
        if match is not None:
            self.AddToDict(match[1])
            print('Good string')
            #print(match[1])
        else:
            print('Bad string')

    def AddToDict(self, key):
        if self._result.get(key) is None:
            self._result[key] = 1
        else:
            num = self._result.get(key)
            self._result[key] = num + 1

    def printDict(self):
        for key, item in self._result.items():
            print(key + ' - ' + str(item))

    def saveRes(self):
        f = open(os.path.join(os.getcwd(), 'Task1', "result1.txt"), 'w')
        for key, item in self._result.items():
            f.write(key + ' - ' + str(item) + '\n')
        f.close()
        self.null()

    def saveTime(self, time, number):
        f = open(os.path.join(os.getcwd(), 'Task1', "time1.txt"), 'w')
        f.write(str(time)+'\n')
        f.write(str(number))
        f.close()
        self.null()

    def null(self):
        self._result ={}


if __name__ == '__main__':
    gen = generator.Generator()
    addr = gen.getFileContent()
    #f = open(os.path.join(os.getcwd(), 'PLY', "1.txt"), 'r')
    #addr = f.read()
    #addr = addr.split('\n')
    #f.close()
    rec = Recognizer(addr)
    rec.recognize()
    # a = 'MailTo:mnea@yluVHFmDqUZLdX9n3yjDfCZyESq5TYBbU16eCJXQDA0MOIeADEQzJOm4F.ILJMzZSscfjAxvBfZWhzzUfooHBLhHxtaBeJhCbqpTRHritafs'
    # print(re.fullmatch(r'[mM][aA][iI][Ll][Tt][Oo]:([a-zA-Z0-9]+)@[a-zA-Z0-9]+[.][a-zA-Z]+(\?[Ss][Uu][Bb][Jj][eE][cC][Tt]=[a-zA-Z0-9]{1,64})?', a))
