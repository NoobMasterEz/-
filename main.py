from lib.Graph import BFS
import csv 


if __name__ == '__main__':
   with open('graph.csv') as file:
        reader = csv.reader(file)
        bfs=BFS(data=reader,number = 9 )
        bfs.where("A","H")
        print("[+][ANS]=",bfs.ans)

   