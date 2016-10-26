# $Id: CommandLineParams.py,v 1.1 2012/11/16 14:51:49 mschrode Exp $

import sys

class CommandLineParams:
    """
    Access parameters specified as command-line arguments.

    Parses the command-line arguments and searches for key-value
    pairs of the form <key>=<value>. The values can be accessed
    lateron with the key using the 'value' method.

    Usage:

       # Create a CommandLineParams object. This stores the
       # parameters given as command-line arguments
       p = CommandLineParams()   

       ...

       # Access the parameter values.
       v = p.value(<key name>,<default value>)
     
    In CMSSW, use the CommandLineParams before declaring the
    process, otherwise edmConfigHash will fail. This leads for
    example to failing grid-control jobs.
    """


    params = dict()

    def __init__(self):
        """
        Parses the command-line arguments

        Expects a space-separated list of key-value pairs
        (multiple values for one key should be separated by commas)

           <key1>=<value1> <key2>=<value2>
           
        No spaces allowed in either <key> or <value> or
        between <key>, '=', and <value>!
        """
        if hasattr(sys,"argv"):
            for arg in sys.argv:
                val = arg.split('=',1)
                if len(val)==2:
                    vlist = val[1].split(',')
                    if len(vlist)==1:
                        self.SetOrAppend(val[0],val[1],True)
                    else:
                        self.params[val[0]] = []
                        for v in vlist:
                            self.SetOrAppend(val[0],v,False)


    def SetOrAppend(self,key,val,set):
        if self.isBool(val):
            if set: self.params[key] = self.toBool(val)
            else:   self.params[key].append(self.toBool(val))
        elif self.isInt(val):
            if set: self.params[key] = int(val)
            else:   self.params[key].append(int(val))
        elif self.isFloat(val):
            if set: self.params[key] = float(val)
            else:   self.params[key].append(float(val))
        else:
            if set: self.params[key] = val
            else:   self.params[key].append(val)


    def printParameters(self):
        """Print the stored key-value pairs"""
        max = 0
        for key in self.params:
            if len(key) > max:
                max = len(key)
        for key in self.params:
            line = "  "+key
            for i in xrange(max-len(key)):
                line += " "
            line += "  : "+str(self.params[key])
            print line


    def value(self,key,default):
        """
        Return the value associated with a certain key

        param key: name of the key (string)
        param default: default value, assigned if key is not found
        """
        if key in self.params:
            return self.params[key]
        else:
            return default


    def isBool(self,expr):
        return expr.lower() in ("true","false")


    def toBool(self,expr):
        if expr.lower() == "true":
            return True
        else:
            return False


    def isFloat(self,expr):
        try:
            float(expr)
            return True
        except ValueError:
            return False


    def isInt(self,expr):
        try:
            int(expr)
            return True
        except ValueError:
            return False
