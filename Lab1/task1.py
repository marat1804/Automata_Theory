import RegExp
import generator


if __name__ == '__main__':
    print('What do you want:\n'
          '1. Read from file\n'
          '2. Read from console\n')
    n = int(input())
    if n == 1:
        print('Reading from file...')
        gen = generator.Generator()
        addr = gen.getFileContent()
        rec = RegExp.Recognizer(addr)
        rec.recognize()
    if n == 2:
        string = ''
        rec = RegExp.Recognizer('')
        while True:
            print('Enter the string (to stop write stop)')
            string = input()
            if string != 'stop':
                rec.recognise(inn=string)
            else:
                break
    print('Bye')



