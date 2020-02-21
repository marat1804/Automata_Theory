import re
import generator
import time


# mailto:[a-zA-Z0-9]+@[a-zA-Z0-9]+.[a-zA-Z]+(\?subject=[a-zA-Z0-9]{1,64})?

class Recognizer:
    def __init__(self, strings):
        self._f = open('result_1.txt', 'w')
        self.strings = strings
        self._result = {}

    def __del__(self):
        self._f.close()

    def recognize(self):
        n = time.perf_counter()
        j=0
        for i in range(len(self.strings)):
            if re.match(r'mailto:[a-zA-Z0-9]+@[a-zA-Z0-9]+.[a-zA-Z]+(\?subject=[a-zA-Z0-9]{1,64})?', self.strings[i]):
                print(self.strings[i]) # add to dict
                j += 1
                self._f.write(self.strings[i] + ' - yes'+'\n')
            else:
                self._f.write(self.strings[i] + ' - no'+'\n')
        n1 = time.perf_counter()
        print(n1-n, j)


if __name__ == '__main__':
    gen = generator.Generator()
    addr = gen.getFileContent()
    rec = Recognizer(addr)
    rec.recognize()