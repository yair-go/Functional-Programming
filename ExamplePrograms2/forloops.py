# forloops.py
#
# FUNCTIONS
#
from string import ascii_letters
#
def isNumber(Str):
   idx = Str.find('.')
   if idx == -1:
     return Str.isdigit()
   else:
     return Str[:idx].isdigit() and Str[idx+1:].isdigit()
def isActualStr(Str):
   ascii_letters_set = set(ascii_letters + ' ')
   strSet = set(Str)
   return not (strSet - ascii_letters_set)
def loopByItem(Seq, Msg):
  print (Msg)
  for item in Seq :
    print (item, end=' ')
  print ()
  return
def loopByIndex(Seq, Msg):
  print (Msg)
  for i in range(len(Seq)):
    item = Seq[i]
    print (item, end=' ')
  print ()
  return
def loopUsingIterator(iterator, Msg):
  print (Msg)
  for i, item in iterator:
    print ((i, item), end=' ')
  print ()
  return
#
# MAIN PROGRAM
#
while True:
 inputStr = input("Enter a legal value ('q' for quit): ")
 if inputStr == 'q':
   break
 if isNumber(inputStr):
  if inputStr.find('.') == -1:
    print ("The input string represents the integer number ", int(inputStr))
  else:
    print ("The input string represents the float number ", float(inputStr))
 elif isActualStr(inputStr):
  print ("The input string is printed as it is: ", inputStr)
 else:
  print ("Let's evaluate the input string. ")
  Seq = eval(inputStr)
  print ("Seq = ", Seq)
  loopByItem(Seq, "=== for loop by item ===")
  if isinstance(Seq,(list, tuple)):
    loopByIndex(Seq, "=== for loop by index ===")
  if isinstance(Seq,(list, tuple, set)):
    loopUsingIterator(enumerate(Seq), "=== for loop by index and item, using enumerate() ===")
  elif isinstance(Seq, dict):
    loopUsingIterator(Seq.items(),"=== for loop by key and value, using items() ===")
#  
