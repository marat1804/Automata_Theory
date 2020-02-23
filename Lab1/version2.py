import version2_sm
import string


class Version2:

    def __init__(self):
        self._fsm = version2_sm.AppClass_sm(self)
        self._is_acceptable = False
        self._mailto = ''
        self._name = ''

    # Uncomment to see debug output.
    # self._fsm.setDebugFlag(True)

    def CheckString(self, text):
        self._fsm.enterStartState()
        text.lower()
        for c in text:
            if c in string.ascii_lowercase:
                self._fsm.Letter()
            elif c in string.digits:
                self._fsm.Digit()
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
        self._mailto = ''
        self._name = ''


if __name__ == '__main__':
    check = Version2()
    t = check.CheckString('mAIlTO:nmae@0CoJvTbzfKGl01ehHbtVniyDKR0GqfYnhQQgW8GqflgYWtCNYcifihWgyzEf.l4KziFfLLqKiYyRMyOQmChvZOlMyYde6F0lzYVXohAACljrAWCQ?sUBjECt=Xm27NhlMesqUOKX')
    print(t)
