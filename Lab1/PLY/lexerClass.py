# coding=utf8
import ply.lex as lex


class MyLexer(object):
    states = (
        ('name', 'inclusive'),
        ('tail', 'inclusive')
    )

    tokens = (
        'MAILTO', 'NAME', 'SERVER', 'NL', 'ANY'
    )

    def t_MAILTO(self, t):
        r'(?mi)^mailto:'
        if t.lexer.current_state() == 'INITIAL':
            t.lexer.begin('name')
        return t

    def t_NL(self, t):
        r'(\n)'
        t.lexer.lineno += len(t.value)
        return t

    def t_name_NAME(self, t):
        r'([a-zA-Z0-9]+)'
        t.lexer.begin('tail')
        return t

    def t_tail_SERVER(self, t):
        r'@[a-zA-Z0-9]+\.[a-zA-Z]+(\?[Ss][Uu][Bb][Jj][eE][cC][Tt]=[a-zA-Z0-9]{1,64})?'
        t.lexer.begin('INITIAL')
        return t

    def t_ANY(self,t):
        r'(.)'
        t.lexer.begin('INITIAL')

    def t_tail_NL(self, t):
        r'(\n)'
        t.lexer.lineno += len(t.value)
        t.lexer.begin('INITIAL')
        return t

    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.begin('INITIAL')

    def t_name_error(self, t):
        print("Illegal character in NAME '%s'" % t.value[0])
        t.lexer.begin('INITIAL')

    def t_tail_error(self, t):
        print("Illegal character in TAIL'%s'" % t.value[0])
        t.lexer.begin('INITIAL')

    def input(self, data):
        return self.lexer.input(data)

    def token(self):
        return self.lexer.token()

    def __init__(self):
        self.lexer = lex.lex(module=self)


if __name__ == '__main__':
    f = open('1.txt', 'r')
    add = f.read()
    f.close()
    lexer = MyLexer()
    lexer.input('MAIlto:nmae@ZefofkpSb6QHKtFb0BWYrz2lPF9KP441jw20wi9QhEz8Mymdy4UAV14d9jG2Ajwk1QA9baqQSfmL0Y.VKwapLZbEvAro?sUBjEct=HBMA')
    #lexer.input('MAilTO:eanm89140@ssDUwdpcJCpUnAyOQEBwuirJMQoXYS.YEjDwjHGxqvSoTjtOLLrzdjPuuMFJdiMZpnfatGPCcBqSLLUqUnzPTyayVxH?subject=21710341519738066704318859566987860891621791630985757978783218')
    while True:
        tok = lexer.token()
        print(tok)
        if not tok:
            break
        if tok.type == 'NAME':
            print('\n###')
            print(tok.type, tok.value, '\n###\n')
