__author__ = 'andersson48'


class _debugPrinter:

    def __init__(self):
        self._DebugMode=True
        print "asdf", self._DebugMode


    def on(self,_state=True):
        self._DebugMode = _state
        #print _DebugMode
        return self._DebugMode



    def off(self,_state=True):
        self._DebugMode = not _state
        return self._DebugMode

    def p(self,*args):
        #print self._DebugMode
        if self._DebugMode:
            print(args)



