#
# Tree Recursion
#
# The first N Fibonacci Numbers
#
# Using a sequential loop
#
def  fib1(N):
	a=0; b=1
	for i in range(N):
		a, b = b, a+b
	return a
#
# Using Non-Tail (Tree) Recursion
#      
def fib2(N):
   if (N == 0):
     return 0
   elif (N == 1):
     return 1
   else:
     return fib2(N-1) + fib2(N-2)
#
# Using Tail Recursion
#
def fib3(n):
  def fibIter(a, b, count):
     if (count == 0):
       return  b
     else:
       return fibIter(a+b, a, count-1)
  return fibIter(1, 0, n)
#
def fib1aSeq(N):
   if N == 0:
     return [fib1(N)]
   return fib1aSeq(N-1)+[fib1(N)]
#
##
## Nested List Recursion (which is a Tree Recursion too)
##
def hasAllnumberp(L):
   """ boolean function that checks if all the elements of L,
at the top level, arte numbers"""
   if L == []:
     return True
   elif isinstance(L[0], (int, float)):
     return hasAllnumberp(L[1:])
   else:
     return False
#
def nestedHasnumberp(L):
   """ boolean function that checks if all the elements of L,
at its all nested levels, arte numbers"""
   if L == []:
     return True
   elif isinstance(L[0], list):
     return nestedHasnumberp(L[0]) and nestedHasnumberp(L[1:])
   elif isinstance(L[0], (int,float)):
     return nestedHasnumberp(L[1:])
   else:
     return False
##
def keepNonumbers(L):
   if not L:
     return []
   elif hasnumberp(L[0]):
     return keepNonumbers(L[1:])
   else:
     return [L[0]] + keepNonumbers(L[1:])
