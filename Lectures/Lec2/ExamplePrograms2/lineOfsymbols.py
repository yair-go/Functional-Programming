#
# lineOfsymbols.py
#
class LineOfSymbols:

    def __init__(self, ln, symb) :
        self.len = ln
        self.symb = symb
        
    def printIt(self):
        print(self.returnStr())

    def returnStr(self):
        return self.symb * self.len

    def id(self):
        return self.len
