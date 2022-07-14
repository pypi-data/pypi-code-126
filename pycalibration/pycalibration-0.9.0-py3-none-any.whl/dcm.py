import pandas #json
import ply.lex as lex
import ply.yacc as yacc
# DCM format 1.0

class DCMParser(object):
    param = dict()

    """
    Base class for a lexer/parser that has the rules defined as methods
    """
    tokens = (
        'FESTWERT',
        'WERT',
        'TEXTSTRING',
        'END',
        'FESTWERTEBLOCK',
        'KENNFELD',
        'KENNLINIE',
        'STX',
        'STY',
        'FESTKENNLINIE',
        'STUETZSTELLENVERTEILUNG',
        'SST',
        'GRUPPENKENNLINIE',
        'SSTX',
        'TEXT',
        'VALUE',
        'STRING',
        'COMMENT'
    )

    def __init__(self, **kw):
        start='dcm'
        lex.lex(module=self)#, debug=self.debug)
        yacc.yacc(module=self) #, debug=self.debug, debugfile=self.debugfile, tabmodule=self.tabmodule)

    def t_FESTWERT(self,t):
        r'FESTWERT'
        return t

    def t_WERT(self,t):
        r'WERT'
        return t

    def t_TEXTSTRING(self,t):
        r'TEXTSTRING'
        return t

    def t_TEXT(self,t):
        r'TEXT'
        return t

    def t_END(self,t):
        r'END'
        return t

    def t_FESTWERTEBLOCK(self,t):
        r'FESTWERTEBLOCK'
        return t

    def t_KENNFELD(self,t):
        r'KENNFELD'
        return t

    def t_KENNLINIE(self,t):
        r'KENNLINIE'
        return t

    def t_STX(self,t):
        r'ST/X'
        return t

    def t_STY(self,t):
        r'ST/Y'
        return t

    def t_FESTKENNLINIE(self,t):
        r'FESTKENNLINIE'
        return t

    def t_STUETZSTELLENVERTEILUNG(self,t):
        r'STUETZSTELLENVERTEILUNG'
        return t

    def t_SST(self,t):
        r'SST'
        return t

    def t_GRUPPENKENNLINIE(self,t):
        r'GRUPPENKENNLINIE'
        return t

    def t_SSTX(self,t):
        r'\*SSTX'
        return t

    def t_VALUE(self,t):
        r'[\-0-9.]+'
        return t

    def t_STRING(self,t):
        r'[a-zA-Z\-0-9_\[\]]+' # | (.*?)(\[)(.*?)(\])'
        #t.value = t.value[1:-1]
        return t

    def t_NUMBER(self, t):
        r'\d+'
        try:
            t.value = int(t.value)
        except ValueError:
            print("Integer value too large %s" % t.value)
            t.value = 0
        # print "parsed number %s" % repr(t.value)
        return t

    def t_COMMENT(self,t):
        r'\* .*'
        pass

    t_ignore = " \t"

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += t.value.count("\n")

    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    def p_dcm(self,p):
        ''' dcm : functions
        '''

    def p_functions(self,p):
        ''' functions : functions function
                | function
        '''

    def p_function_fw(self, p):
        '''function : FESTWERT STRING WERT VALUE END'''
        self.param[p[2]]={'X': float(p[4]), 'Y': None, 'Z':None}
        #p[0]=dict({'name':p[2],'X':json.dumps(p[4]),'Y':None,'Z':None})

    def p_function_kl(self, p):
        '''function : KENNLINIE STRING VALUE stxs werts END'''
        self.param[p[2]]={'X': [float(x) for x in p[4]], 'Y': [float(x) for x in p[5]], 'Z':None}

    def p_function_fkl(self, p):
        '''function : FESTKENNLINIE STRING VALUE stxs werts END'''
        self.param[p[2]]={'X': [float(x) for x in p[4]], 'Y': [float(x) for x in p[5]], 'Z':None}

    def p_function_ssv(self, p):
        '''function : STUETZSTELLENVERTEILUNG STRING VALUE stxs END'''
        self.param[p[2]] = {'X': [float(x) for x in p[4]], 'Y': None, 'Z': None}

    def p_function_gkl(self, p):
        '''function : GRUPPENKENNLINIE STRING VALUE SSTX STRING stxs werts END'''
        self.param[p[2]] = {'X': [float(x) for x in p[6]], 'Y': [float(x) for x in p[7]], 'Z': None}

    def p_function_txtstr(self, p):
        '''function : TEXTSTRING STRING TEXT STRING END'''
        self.param[p[2]] = {'X': p[4], 'Y': None, 'Z': None}

    def p_stxs(self,p):#STX
        ''' stxs : stxs stx
                  | stx
        '''
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = p[1] + [p[2]]

    def p_stx(self,p): #STX
        '''stx : STX VALUE
                | VALUE'''
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = p[2]

    def p_stys(self,p):#STY
        ''' stys : stys sty
                 | sty
        '''
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = p[1] + [p[2]]

    def p_sty(self,p): #STY
        '''sty : STY VALUE
                | VALUE'''
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = p[2]

    def p_werts(self,p): #WERT
        ''' werts : werts wert
                 | wert
        '''
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = p[1] + [p[2]]

    def p_wert(self,p): #WERT
        '''wert : WERT VALUE
                | VALUE'''
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = p[2]

    def Process(self,text):
        lex.input(text)
        yacc.parse(text)
        return self.param

class DCM(object):
    '''
    DCM class import and export DCM file format
    '''
    def __init__(self):
        super().__init__()

    def Output(self,filename):
        self.f = open(filename, 'w')

    def Import(self,filename):
        file = open(filename, 'r')
        text=file.read()
        file.close()
        self.parser=DCMParser()
        self.param=self.parser.Process(text)

    # def __del__(self):
    #     self.FESTWERT('calg_nr_parmVersion_U16c', self.release_id)
    #     self.f.close()

    def Close(self):
        #self.FESTWERT('calg_nr_parmVersion_U16c', self.Value('calg_nr_parmVersion_U16c')['X']+1)
        self.f.close()

    def FESTWERT(self, name, value):
        self.f.write('FESTWERT %s\n' %(name))
        self.f.write('WERT %s\n' %(value))
        self.f.write('END\n\n')

    def FESTWERTEBLOCK(self, name, valueList):
        self.f.write('FESTWERTEBLOCK %s\n' % (name))
        self.f.write('WERT %s\n' % (valueList))
        self.f.write('END\n\n')

    def KENNFELD(self, name, x, y):
        pass

    def FESTKENNFELD(self):
        pass

    def KENNLINIE(self,name,x,v):
        self.param[name]={'X':x, 'Y':v, 'Z':None}
        self.f.write('KENNLINIE %s %i\n' %(name,len(x)))
        self.f.write('%s' %(self.STX(x)))
        self.f.write('%s' %(self.WERT(v)))
        self.f.write('END\n\n')

    def FESTKENNLINIE(self,name,x,v):
        self.f.write('FESTKENNLINIE %s %i\n' %(name,len(x)))
        self.f.write('%s' %(self.STX(x)))
        self.f.write('%s' %(self.WERT(v)))
        self.f.write('END\n\n')

    def STUETZSTELLENVERTEILUNG(self,name,v):
        self.f.write('STUETZSTELLENVERTEILUNG %s %i\n' %(name,len(v)))
        self.f.write('*SST\n')
        self.f.write('%s' %(self.STX(v)))
        self.f.write('END\n\n')

    def GRUPPENKENNLINIE(self,name,xaxis,x,y):
        self.f.write('GRUPPENKENNLINIE %s %i\n' %(name,len(x)))
        self.f.write('*SSTX %s\n' %(xaxis))
        self.f.write('%s' % (self.STX(x)))
        self.f.write('%s' %(self.WERT(y)))
        self.f.write('END\n\n')

    def STX(self, data):
        res = ""
        for block in [data[i:i + 6] for i in range(0, len(data), 6)]:
            res = '%s\tST/X' % res
            for i in block:
                res = '%s\t%s' % (res, i)
            res = '%s\n' % res
        return res

    def STY(self, data):
        res = ""
        for block in [data[i:i + 6] for i in range(0, len(data), 6)]:
            res = '%s\tST/Y' % res
            for i in block:
                res = '%s\t%s' % (res, i)
            res = '%s\n' % res
        return res

    def WERT(self, data):
        res = ""
        for block in [data[i:i + 6] for i in range(0, len(data), 6)]:
            res = '%s\tWERT' % res
            for i in block:
                res = '%s\t%s' % (res, i)
            res = '%s\n' % res
        return res

    def Value(self, name):
        return self.param[name]
        # try:
        #     x = json.loads(self.param[name]["X"])
        # except:
        #     x = None
        # try:
        #     y = json.loads(self.param[name]["Y"])
        # except:
        #     y = None
        # try:
        #     z = json.loads(self.param[name]["Z"])
        # except:
        #     z = None
        # return x, y, z
