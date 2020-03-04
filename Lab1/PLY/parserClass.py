from PLY.lexerClass import MyLexer
import ply.yacc as yacc


class MyParser(object):
    tokens = MyLexer.tokens
    a = dict()
    _overload_file = 'Task3.txt'
    _result_file = 'result.txt'
    count = 0

    def get_A(self):
        return self.a

    def __init__(self, from_file=False):
        self._file = from_file
        self.lexer = MyLexer()
        self.parser = yacc.yacc(module=self, optimize=1, debug=False, write_tables=False)

    def check_string(self, code):
        if self._file:
            self._f = open(self._result_file, 'w')
        result = self.parser.parse(code)
        print(self.count)
        if self._file:
            self._f.close()
        return result

    def p_addr_4(self, p):
        """addr : MAILTO NAME SERVER """
        print('addr_4')
        if self._file:
            self._f.write(p[1]+p[2]+p[3] + ' - yes\n')
        if self.a.get(p[2]) is None:
            self.a.setdefault(p[2],1)
        else:
            self.a[p[2]] += 1
        self.count += 1

    def p_addr_3(self, p):
        """addr : MAILTO NAME SERVER SUBJECT """
        print('addr_3')
        if self._file:
            self._f.write(p[1] + p[2] + p[3] + p[4] +' - yes\n')
        if self.a.get(p[2]) is None:
            self.a.setdefault(p[2], 1)
        else:
            self.a[p[2]] += 1
        self.count += 1
    '''
    def p_addr_2(self, p):
        """addr : NL MAILTO NAME SERVER"""
        print('addr_2')
        if self._file:
            self._f.write(p[2]+p[3]+p[4] + ' - yes\n')
        if self.a.get(p[3]) is None:
            self.a.setdefault(p[3],1)
        else:
            self.a[p[3]] += 1
        self.count += 1

    def p_addr_1(self, p):
        """addr : NL MAILTO NAME SERVER SUBJECT"""
        print('addr_1')
        if self._file:
            self._f.write(p[2] + p[3] + p[4] +p[5] + ' - yes\n')
        if self.a.get(p[3]) is None:
            self.a.setdefault(p[3], 1)
        else:
            self.a[p[3]] += 1
        self.count += 1

    def p_addr_5(self, p):
        """addr : MAILTO NAME SERVER NL"""
        print('addr_5')
        if self._file:
            self._f.write(p[1]+p[2]+p[3] + ' - yes\n')
        if self.a.get(p[2]) is None:
            self.a.setdefault(p[2],1)
        else:
            self.a[p[2]] += 1
        self.count += 1

    def p_addr_6(self, p):
        """addr :  MAILTO NAME SERVER SUBJECT NL"""
        print('addr_6')
        if self._file:
            self._f.write(p[1] + p[2] + p[3] +p[4] + ' - yes\n')
        if self.a.get(p[2]) is None:
            self.a.setdefault(p[2], 1)
        else:
            self.a[p[2]] += 1
        self.count += 1
    '''
    def p_addr_zero_err_type(self, p):
        """addr : err_list """
        print('arr_err_0')
        #if self._file:
            #self._f.write(p[1] + ' - no\n')

    def p_addr_third_err_type(self,p):
        """addr : MAILTO err_list """
        print('arr_err_3')
        if self._file:
            self._f.write(p[1] + p[2] + p[3] + ' - no\n')

    def p_addr_first_err_type(self, p):
        """addr : MAILTO NAME err_list"""
        print('arr_err_1')
        if self._file:
            self._f.write(p[1] + p[2] + p[3] + ' - no\n')

    def p_addr_second_err_type(self,p):
        """addr : MAILTO NAME SERVER err_list"""
        print('arr_err_2')
        if self._file:
            self._f.write(p[1] + p[2] + p[3] + ' - no\n')

    def p_err_list_type3(self, p):
        """err_list : err_list err """
        print('error_3')
        p[0] = p[1]
        p[0] += p[2]

    def p_err_list_type2(self, p):
        """err_list : """
        print('error_3')
        p[0] = p[1]
        p[0] += p[2]

    def p_err_list_type1(self, p):
        """err_list : err"""
        print('error_1')
        p[0] = p[1]

    def p_err_list_type0(self, p):
        """err_list : NL"""
        print('error_0')
        p[0] = p[1]

    def p_err(self, p):
        """err : ANY"""
        p[0] = p[1]

    def p_error(self, p):
        print('Unexpected token', p)


if __name__ == '__main__':
    f = open('addresses.txt', 'r')
    add = f.read()
    #print(add)
    f.close()
    parser = MyParser()
    print(parser.check_string(add))
    #print(parser.check_string('mailto:eman620@NJxvCqeazvWClhtnrjFJOEQvNkGIJFWfabVDxcEDVuwiBKfJJZxiwzzkErXeLhz.kddsIKinJlcuUWTQSLtljuJLHGeovwAooKpLQBuhWCbahLlKzEJWerljGoCf'))
    print(parser.a)
