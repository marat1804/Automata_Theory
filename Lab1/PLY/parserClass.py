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

    #def p_addr_list(self, p):
       # """addr_list : addr
       # | addr_list addr """

    def p_addr_1(self, p):
        """addr : MAILTO NAME SERVER SUBJECT"""
        print('addr_1')
        if self._file:
            self._f.write(p[1]+p[2]+p[3] + ' - yes\n')
        if self.a.get(p[2]) is None:
            self.a.setdefault(p[2],1)
        else:
            self.a[p[2]] += 1
        self.count += 1

    def p_addr_2(self, p):
        """addr : MAILTO NAME SERVER"""
        print('addr_2')
        if self._file:
            self._f.write(p[1]+p[2]+p[3] + ' - yes\n')
        if self.a.get(p[2]) is None:
            self.a.setdefault(p[2],1)
        else:
            self.a[p[2]] += 1
        self.count += 1

    def p_addr_zero_err_type(self, p):
        """addr : err_list NL"""
        print('arr_err_0')
        if self._file:
            self._f.write(p[1] + ' - no\n')

    def p_addr_first_err_type(self, p):
        """addr : MAILTO NAME NL"""
        print('arr_err_1')
        if self._file:
            self._f.write(p[1] + p[2] + p[3] + ' - no\n')

    def p_addr_second_err_type(self,p):
        """addr : MAILTO NAME err_list NL"""
        print('arr_err_2')
        if self._file:
            self._f.write(p[1] + p[2] + p[3] + ' - no\n')

    def p_addr_third_err_type(self,p):
        """addr : MAILTO err_list NL"""
        print('arr_err_3')
        if self._file:
            self._f.write(p[1] + p[2] + p[3] + ' - no\n')

    def p_err_list_type3(self, p):
        """err_list : err_list err"""
        print('error_3')
        p[0] = p[1]
        p[0] += p[2]

    def p_err_list_type2(self, p):
        """err_list : """
        print('error_2')

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
    parser = MyParser(True)
    print(parser.check_string('mAIltO:anme421Qc2icgOzsZ3h6Cu.QfVKtHRNcsDawFHUPsmAHXdq?subject=7tzveaMDBTKvnrEO0nWpFP2egl5EMeYJklAhBDSKrqiPkTRKCjJTZanBTMfAS96enmxV \n maiLtO:enam316119@hFM2Pc4LHIRF6sZWZnaZFstDNPf6Rg9Ih3zfRZKjG9xBZrzvIMJ5q.bs?subject=WVpiVHKuITUrX'))
    print(parser.count)
    print(parser.a)
