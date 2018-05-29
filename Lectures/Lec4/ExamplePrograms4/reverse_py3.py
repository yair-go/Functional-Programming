#
# top level reverse
#
def myReverse(L):
   retval = []
   for item in L:
      retval = [item] + retval
   return retval

def recReverse(L):
   if L == []:
     return L
   return ([L[-1]] + recReverse(L[:-1]))

def tailReverse(L, resL = []):
   if L == []:
     return resL
   return tailReverse(L[:-1], resL + [L[-1]])
#
# nested reverse
#
def deepReverse(L):
   if L == []:
     return L
   if isinstance(L[-1],list):
     return [deepReverse(L[-1])]+deepReverse(L[:-1])
   else:
     return ([L[-1]]+deepReverse(L[:-1]))

#------------------
##L = [1,2,3,4,5]
##print( myReverse( L ) )
##
##print( recReverse(L) )
##print( tailReverse(L) )
##
##L = [1,[2,3,[4,5]],6]
##print( deepReverse(L) )
