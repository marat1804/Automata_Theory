from SMC import version2_sm
import string
import generator
import time
import os


class Version2:

    def __init__(self):
        self._fsm = version2_sm.AppClass_sm(self)
        self._is_acceptable = True
        self._counter = 0
        self._name = ''
        self.add = ''
        self._fsm.enterStartState()
        self._result = {}
        self._f = open(os.path.join(os.getcwd(), 'Task2', "result_2.txt"), 'w')
        self._f1 = open(os.path.join(os.getcwd(), 'Task2', "result2.txt"), 'w')

    # Uncomment to see debug output.
    # self._fsm.setDebugFlag(True)

    def CheckString(self, text):
        self._fsm.MailTo()
        text = text.lower()
        for c in text:
            if not self._is_acceptable:
                break
            if c in string.ascii_lowercase:
                self._fsm.Letter(c)
            elif c in string.digits:
                self._fsm.Digit(c)
            elif c == ':':
                self._fsm.Colom()
            elif c == '@':
                self._fsm.At()
            elif c == '.':
                self._fsm.Dot()
            elif c == '?':
                self._fsm.Question()
            elif c == '=':
                self._fsm.Eq()
            else:
                self._fsm.Unknown()
        self._fsm.EOS()
        self.AddToDict(self.add)
        self.writeFile(text)
        return self._is_acceptable, self.add

    def writeFile(self, text):
        if self._is_acceptable:
            self._f.write(text + ' - yes '+'\n')
        else:
            self._f.write(text + ' - no ' + '\n')

    def AddToDict(self, key):
        if not self._is_acceptable:
            return
        if self._result.get(key) is None:
            self._result[key]=1
        else:
            num = self._result.get(key)
            self._result[key]=num+1

    def Acceptable(self):
        self._is_acceptable = True

    def Unacceptable(self):
        self._is_acceptable = False

    def ClearSMC(self):
        self._is_acceptable = True
        self._counter = 0
        self._name = ''
        self.add = ''

    def lenMailTo(self):
        return self._counter != 6

    def counterInc(self):
        self._counter += 1

    def counterZero(self):
        self._counter = 0

    def checkMail(self):
        t = self._name == "mailto"
        self._name = ''
        return t

    def clearMem(self):
        self._name =''

    def checkSubject(self):
        return self._name == 'subject'

    def Memorise(self, letter):
        self._name += letter

    def remName(self):
        self.add = self._name
        self._name = ''

    def lenText(self):
        return 0 < self._counter <= 64

    def nonZero(self):
        return self._counter != 0

    def __del__(self):
        self.saveRes()
        self._f.close()
        self._f1.close()

    def saveRes(self):
        for key, item in self._result.items():
            self._f1.write(key + ' - ' + str(item)+'\n')


if __name__ == '__main__':
    gen = generator.Generator()
    add = gen.getFileContent()
    check = Version2()
    k = 0
    n1 = time.perf_counter()
    for i in range(len(add)):
        t = check.CheckString(add[i])
        if t[0]:
            k += 1
        print(i, t)
    n2 = time.perf_counter()
    print(n2-n1, k)