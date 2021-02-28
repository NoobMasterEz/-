from collections import defaultdict

class BFS(object):
    Queue=[] 
    ANS=0
    def __init__(self,**kwarge):

        self.data=kwarge["data"]
        self.number=kwarge["number"]
        self.graph =  defaultdict(list)

    def __addEdge(self,u,v,w):
        if w == 1 :
            self.graph[ord(u)-65].append(ord(v)-65)
        else:
        
            self.graph[ord(u)-65].append(self.number)
            self.graph[self.number].append(ord(v)-65)
            self.number = self.number +1 


    def __path(self,parent,s):
        Path_len = 1

        if parent[s] == -1  and s < self.number:
            print(chr(s+65),)
            return 0
        l= self.__path(parent,parent[s])
        Path_len = l + Path_len 
        
        if s < self.number:
            if Path_len % 2 == 0 :
                print(chr(s+65))
        return Path_len 

    def __bfs(self):
        visited = [False ] * (self.number+1 )
        parent = [-1] * (self.number+1)
        self.Queue.append(ord(self.source)-65)
        visited[ord(self.source)-65]= True
        print("graph -- > ",self.graph)
        while len(self.Queue) >0 :
            print("parent-->",parent)
            print("visited-->",visited)
            s= self.Queue.pop(0)

            if s == ord(self.dest)-65 : 
                return self.__path(parent,s)
            for i in self.graph[s]: 
                if visited[i] == False:
                    self.Queue.append(i) 
                    visited[i]= True
                    parent[i]=s
                

    def where(self,source,dest):
        self.source=source
        self.dest=dest
        for (u,v,w) in self.data:
            self.__addEdge(u,v,w)

        self.ANS= self.__bfs()

    @property
    def ans(self):
        return self.ANS      

    def __str__(self):
        for i in self.data :
            print(i) 