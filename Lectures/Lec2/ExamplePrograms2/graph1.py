# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Graph:
    def __init__(self,V,E):
        self.V=V
        self.VertexList={}
        for vertex in V:
            self.VertexList[vertex]=[]
        for edge in E:
            self.VertexList[edge[0]].append(edge[1])

    def printGraph(self):
        for i in self.V:
            str=i + ': '
            for edge in self.VertexList[i]:
                str = str + "({},{})".format(i,edge[0])
            print(str)
        
    def DFSrec(self,u):
        for v in self.VertexList[u]:
            if not(v in self.VertexDict):
                print ('Edge ({},{}) is a Tree-edge'.format(u,v))
                self.timer = self.timer + 1
                self.VertexDict[v]=(u, self.timer, 'gray')
                self.DFSrec(v)
            else:
                if (self.VertexDict[v][2] == 'gray'):
                    print ('A circle found. Edge ({},{}) is a backword edge'.format(u,v))
                else:
                    if (self.VertexDict[u][1] < self.VertexDict[v][1]):
                        print ('Edge ({},{}) is a forward edge'.format(u,v))
                    else:
                        print ('Edge ({},{}) is a cross edge'.format(u,v))
        self.timer = self.timer + 1
        parentOfU=self.VertexDict[u][0]
        self.VertexDict[u]=(parentOfU,self.timer, 'black')
    
    def DFS(self):
        self.VertexDict={}
        self.timer=0
        returnedVal = False
        for u in self.V:
            if (not (u in self.VertexDict)):
                self.timer = self.timer + 1
                self.VertexDict[u]=("",self.timer, "gray")
                self.DFSrec(u)
                
g=Graph(['a','b','c','d'],[('a','b'),('b','c'),('c','a'),('c','d')])
g.DFS()