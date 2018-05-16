#
# elseforloop.py
#
import sys
import collections
#
def average(L):
   return sum(L) / len(L)
#
def prtError(Msg):
   print (Msg)
   print ('Program is aborted')
   return
#
L = eval(input('Enter a sequence of numbers: '))
if isinstance(L, collections.Iterable):
  print ('OK - the input ', L, ' is a sequence.')
else:
  prtError('ERROR - the input is not a sequence!')
  sys.exit()
#
for item in L:
   if not isinstance(item, (int, float)):
     prtError('ERROR - the item in position ' + str(L.index(item)) + ' is not a number')
     sys.exit()
else :
    print ('OK - all the items in the sequence are numbers')
    print ('The minimum of all of them is: ', min(L))
    print ('The maximum of all of them is: ', max(L))
    print ('The sum of all of them is: ', sum(L))
    print ('The average of all of them is: ', average(L))
    
