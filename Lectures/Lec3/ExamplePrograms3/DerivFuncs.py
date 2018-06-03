#
from ComposeFuncs import *
#
# DerivFuncs.py
#
#***********************************************************
#          "symbolic" derivation of a function          
#***********************************************************

eps = 0.0005
def deriv(f):
   return lambda x : (f(x + eps) - f(x)) / eps
#
#***********************************************************
#          "symbolic" Nth derivation of a function           
#***********************************************************
def Nderiv(f, N):
   def selfCompLst(func,N):
      Lst = []
      for i in range(N):
         Lst.insert(0,func)
      return Lst   
   derivSeq = selfCompLst(deriv, N)
   d = fullCompose(*derivSeq)(f)
   return d
#
#**************************************************************
# computing the value of a derivative for a specific value of x      
#**************************************************************
def derivCompute(f, x):
   return (f(x + 0.0005) - f(x)) / 0.0005
#
   
f1 = lambda x: 3*x ** 3 + 2 *x ** 2 + 4 * x + 7
print(Nderiv(f1, 3)(2))