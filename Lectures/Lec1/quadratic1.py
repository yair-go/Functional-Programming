#
# quadratic1.py
#
import math

def CalculateDiscriminant(x,y,z):
   desc = y**2 - 4*x*z 
   return desc
 
def CalculateRoots(a,b,desc):
  term = -b / (2*a)
  if desc == 0:
    result = term
  elif desc > 0:
    root1 = term + math.sqrt(desc) / (2*a)
    root2 = term - math.sqrt(desc) / (2*a)
    result = root1, root2
  else:
    result = None
  return result

def PrintSolution(Roots):
  if (Roots == None):
    print ('no real solutions')
  elif isinstance(Roots, (int, float)):
    print ('the only one solution is ',)
    print (Roots)
  else:
    print ('the two real solutions are: ',)
    print (Roots)

a = float(input('Enter the value of a: '))
b = float(input('Enter the value of b: '))
c = float(input('Enter the value of c: '))
Desc = CalculateDiscriminant(a,b,c)
# Solution is a pair of values or only one
Solution = CalculateRoots(a,b,Desc)
PrintSolution(Solution)
