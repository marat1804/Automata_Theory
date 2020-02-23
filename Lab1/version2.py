import version2_sm
import string
import generator
import time


class Version2:

    def __init__(self):
        self._fsm = version2_sm.AppClass_sm(self)
        self._is_acceptable = False
        self._counter = 0
        self._name = ''
        self.add = ''
        self._fsm.enterStartState()

    # Uncomment to see debug output.
    # self._fsm.setDebugFlag(True)

    def CheckString(self, text):
        self._fsm.MailTo()
        text = text.lower()
        for c in text:
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
        return self._is_acceptable

    def Acceptable(self):
        self._is_acceptable = True

    def Unacceptable(self):
        self._is_acceptable = False

    def ClearSMC(self):
        self._is_acceptable = False
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

    def checkSubject(self):
        return self._name == 'subject'

    def Memorise(self, letter):
        if letter in string.ascii_lowercase or letter in string.digits:
            self._name += letter

    def remName(self):
        self.add = self._name
        self._name = ''

    def lenText(self):
        return 0 < self._counter <= 64

    def nonZero(self):
        return self._counter != 0


if __name__ == '__main__':
    f = open('result_2.txt','w')
    gen = generator.Generator()
    add = gen.getFileContent()
    check = Version2()
    k = 0
    n1 = time.perf_counter()
    for i in range(len(add)):
        t = check.CheckString(add[i])
        print(i, t)
        if t:
            f.write(add[i]+' - yes '+'\n')
            k += 1
        else:
            f.write(add[i] + ' - no ' + '\n')
    f.close()
    n2 = time.perf_counter()
    print(n2-n1, k)
