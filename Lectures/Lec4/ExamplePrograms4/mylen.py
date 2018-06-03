#
# mylen.py
#
# Iterative (non-Functional) version
#
def mylen1(L):
   length = 0
   for item in L:
      length += 1
   return length
#
#
# Functional versions
#
# Non-tail recursive version
def mylen2(L):
   if L == []:
     return 0
   else:
     return 1 + mylen2(L[1:])
#
# Tail recursive version
def nyLen3(L):
   def Tlen(L,length):
      if L == []:
        return length
      else:
        return Tlen(L[1:], 1 + length)	
   return Tlen(L,0)
#
def evenLen(L):
   if L == []:
     return 0
   elif L[0] % 2 == 0:
     return 1 + evenLen(L[1:])
   else:
     return evenLen(L[1:])
