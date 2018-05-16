#
# eratosthenes.py
# The Eratosthenes' algorithm
#
def napa(N):
    lst = [0]*N
    rishoni = [True]*N
    rishoni[0] = False
    for i in range(1,N):
       lst[i] = lst[i-1]+1     #list of number between 1..N
    for i in range(2,N):  #make rishoni to be an array of True values for prime numbers
        if rishoni[i]:
            for mlt in lst[i*2:N:i]:
               rishoni[mlt]=False
    res = []
    for i in range(N):
       if rishoni[i]:
         res.append(lst[i])
    return res
