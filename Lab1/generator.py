import random
import string
import os


class Generator:

    def __init__(self, num=1000000):
        self._num = num
        self._f = open(os.path.join(os.getcwd(),'Mails',"addresses.txt"), 'r')
        self._prob1 = 0.33
        self._prob2 = 0.66
        self._prob_half = 0.5
        self._prob0 = 0.2

    def rand(self):
        return random.random()

    def __del__(self):
        self._f.close()

    def generateFile(self):
        self._f.close()
        self._f = open(os.path.join(os.getcwd(),'Mails',"addresses.txt"), 'w')
        for i in range(self._num):
            address = self.mailto()+self.name()+self.dogSign()+self.generateString()+self.dot() + \
                      self.generateString() + self.text()+'\n'
            self._f.write(address)

    def generateString(self, a=-5, b=80):
        letters = random.randint(a, b)
        r = self.rand()
        if r < self._prob1:
            return ''.join(random.choices(string.ascii_letters + string.digits, k=letters))
        elif r < self._prob2:
            return ''.join(random.choices(string.ascii_letters, k=letters))
        else:
            return ''.join(random.choices(string.digits, k=letters))

    def upper(self, string):
        if self.rand() > self._prob_half:
            return string
        else:
            a = []
            for i in range(len(string)):
                a.append(string[i])
            for i in range(random.randint(0,len(a))):
                j=random.randint(0,len(a)-1)
                a[j]=a[j].upper()
            return ''.join(a)

    def mailto(self):
        if self.rand() > self._prob_half:
            return self.upper('mailto:')
        else:
            return ''

    def name(self):
        name = ['n', 'a', 'm', 'e']
        random.shuffle(name)
        return ''.join(name)+''.join(random.choices('/_~',k=random.randint(-7,2)))+''.join(random.choices(string.digits, k=random.randint(-5,6)))

    def dogSign(self):
        if self.rand() > self._prob_half:
            return '@'
        else:
            return ''

    def dot(self):
        if self.rand() > self._prob0:
            return '.'
        else:
            return ''

    def text(self):
        text = self.generateString()
        if len(text) != 0:
            r = self.rand()
            if r > self._prob1:
                text = self.upper('?subject=')+text
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

    def getFile(self):
        add = self._f.read()
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
