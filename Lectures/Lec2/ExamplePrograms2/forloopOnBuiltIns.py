#
# forloopOnBuiltInspy
#
def iterableLooping(iterableObj):
   Lout = []
   for item in iterableObj:
      Lout.append(item)
   return Lout
#
typeSet = set([])
for i in range(5):
   while True:
     Obj = eval(input("Enter the iterable object to loop on : "))
     ObjType = type(Obj)
     if ObjType not in typeSet:
       typeSet.add(ObjType)
       print (iterableLooping(Obj))
       break
     else:
       print ("You already tried this object type")
#
