#
# quadratic.py
#
import math

def CalculateDiscriminant(x,y,z):
   desc = y**2 - 4*x*z 
   return desc
 
def CalculateRoots(a,b,desc):
  result = []
  term = -b / (2*a)
  if desc == 0:
    result.append(term)
  elif desc > 0:
    root1 = term + math.sqrt(desc) / (2*a)
    root2 = term - math.sqrt(desc) / (2*a)
    result.extend([root1, root2]) 
  else:
    pass
  return result

def PrintSolution(RootsList):
  if (len(RootsList) == 0):
    print ('no real solutions')
  elif (len(RootsList) == 1):
    print ('the only one solution is ',)
    print (RootsList[0])
  else:
    print ('the two real solutions are: ',)
    print (RootsList)

a = float(input('Enter the value of a: '))
b = float(input('Enter the value of b: '))
c = float(input('Enter the value of c: '))
Desc = CalculateDiscriminant(a,b,c)
# Solution is a list
Solution = CalculateRoots(a,b,Desc)
PrintSolution(Solution)
