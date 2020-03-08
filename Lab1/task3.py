import pyLexer
import generator
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
            addr = gen.getFile()
            rec = pyLexer.PLY(True)
            n1 = time.perf_counter()
            rec.parse_from_file(addr)
            n2 = time.perf_counter()
            rec.printDict()
            print(n2-n1, rec.parser.count)
            rec.saveRes()
            rec.saveTime(n2-n1)
        if n == 2:
            string = ''
            rec = pyLexer.PLY()
            rec.parse_from_console()
        if n == 0:
            break
    print('Bye')



