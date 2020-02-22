import random
import string
from collections import Counter


class Generator:

    def __init__(self, num=1000000):
        self._num = num
        self._f = open('addresses.txt', 'r')

    def rand(self):
        return random.random()

    def __del__(self):
        self._f.close()

    def generateFile(self):
        self._f.close()
        self._f = open('addresses.txt', 'w')
        for i in range(self._num):
            address = self.mailto()+self.name()+self.dogSign()+self.generateString()+self.dot() + \
                      self.generateString() + self.text()+'\n'
            self._f.write(address)

    def generateString(self, a=-5, b=80):
        letters = random.randint(a, b)
        r = self.rand()
        if r < 0.33:
            return ''.join(random.choices(string.ascii_letters + string.digits, k=letters))
        elif r < 0.66:
            return ''.join(random.choices(string.ascii_letters, k=letters))
        else:
            return ''.join(random.choices(string.digits, k=letters))

    def mailto(self):
        if self.rand() > 0.4:
            return 'mailto:'
        else:
            return ''

    def name(self):
        name = ['n', 'a', 'm', 'e']
        random.shuffle(name)
        return ''.join(name)+''.join(random.choices(string.digits, k=random.randint(-5,6)))

    def dogSign(self):
        if self.rand() > 0.4:
            return '@'
        else:
            return ''

    def dot(self):
        if self.rand() > 0.2:
            return '.'
        else:
            return ''

    def text(self):
        text = self.generateString()
        if len(text) != 0:
            r = self.rand()
            if r > 0.3:
                text = '?subject='+text
                return text
            else:
                return text
        else:
            return ''

    def getFileContent(self):
        add = self._f.read()
        add = add.split('\n')
        del add[self._num]
        return add


if __name__ == '__main__':
    gen = Generator()
    gen.generateFile()
    '''
    add = gen.getFileContent()
    a = []
    for i in range(len(add)):
        a.append(add[i].split(' ')[1].split('@')[0])

    counter = Counter(a)
    print(a)
    print('####')
    for items, count in counter.items():
        if count >1:
            print(items, count)
            '''
    '''
    f = open('addresses.txt', 'r')
    add = f.read()
    addr = add.split('\n')
    print(len(addr))
    print(addr[999999])
    '''
    #print(gen.name())
