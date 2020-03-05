import generator
import StateMC
import time


if __name__ == '__main__':
    while True:
        print('What do you want:\n'
              '0. Exit \n'
              '1. Read from file\n'
              '2. Read from console\n')
        n = int(input())
        if n == 1:
            print('Reading from file...')
            gen = generator.Generator()
            add = gen.getFileContent()
            check = StateMC.Version2()
            k = 0
            n1 = time.perf_counter()
            for i in range(len(add)):
                t, name = check.CheckString(add[i])
                if t:
                    k += 1
                print(i, t, name)
            n2 = time.perf_counter()
            check.printDict()
            check.saveRes()
            print(n2-n1, k)
            check.saveTime(n2-n1, k)
        if n == 2:
            string = ''
            check = StateMC.Version2()
            while True:
                print('Enter the string (to stop write stop)')
                string = input()
                if string != 'stop':
                    t, name = check.CheckString(string)
                    if t:
                        print('Good string with name - '+name)
                    else:
                        print('Bad string')
                else:
                    check.printDict()
                    break
        if n == 0:
            break
    print('Bye')
