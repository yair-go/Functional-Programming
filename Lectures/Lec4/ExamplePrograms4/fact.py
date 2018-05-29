#
# fact.py
#
# Iterative (non-Functional) version
# 
def fact1(N):
   result = 1
   for i in range(N,1,-1):
      result *= i
   return result
#
# Functional versions
#
# Non-tail recursive version
def fact2(N):
   if N in (0,1):
     return 1
   else:
     return N * fact2(N-1)
#
# Tail recursive version
def fact3(N):
   def Tfact(N,result):
      if N in (0,1):
        return result
      else:
        return Tfact(N-1, N*result)	
   return Tfact(N,1)
#
