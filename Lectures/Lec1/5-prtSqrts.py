import math
def printSqrts(fr,to):
    for i in range(fr,to):
        shoresh=pow(i,0.5)
        p2=pow(i,2)
        print(" {0:10}  {1:5.3f}  {2:5.3f}".format(i,shoresh,p2))
