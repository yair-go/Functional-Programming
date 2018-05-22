#
# don't update
# - create the value to be returned
#
# String example
def fullName1(firstName, lastName):
   # imperative style
   Name = ''
   Name += firstName
   Name += ", "
   Name += lastName
   return Name

def fullName2a(firstName, lastName):
   # functional (stateless) style
   return firstName + ", " + lastName

def fullName2b(firstName, lastName):
   # functional (once-only assignment) style
   Name = firstName + ", " + lastName
   return Name
#
# List example
def yearsList(From,To):
   # imperative style
   years = []
   y = From
   while y <= To:
     years.append(y)
     y += 1
   return years

def yearsList2a (From, To):
   # functional (stateless) style
   return list(range(From, To+1))

def yearsList2b (From, To):
   # functional (once-only assignment) style
   years = list(range(From, To+1))
   return years

#
# Dict example
def popAges(names, ages):
   # imperative style
   D = dict([])
   for i in range(len(names)):
      D[names[i]] = ages[i]
   return D

def popAges2a(names, ages):
   # functional (stateless) style
   return dict(zip(names, ages))

def popAges2b(names, ages):
   # functional (once-only assignment) style
   pairsLst = zip(names, ages)
   return dict(pairsLst)

   
   
