class Node:
    def __init__(self,data) -> None:
        self.data=data 
        self.next=None

class LinkedList:
    def __init__(self) -> None:
        self.head=None

class Graph:
    def __init__(self,vertices) -> None:
        self.vertices=vertices
        self.table=[None ]*self.vertices

    def add_edge(self,src,des):
        node=Node(des)
        node.next=self.table[src]
        self.table[src]=node

        node=Node(src)
        node.next=self.table[des]
        self.table[des]=node
    def print_graph(self):
        for i in range(self.vertices):
            print(f"Adjacency List of {i} vertex is ")
            temp=self.table[i]
            while(temp):
                print(temp.data," --> ",end="")
                temp=temp.next
            print("\n")

        


vertices=5
graph=Graph(5)
graph.add_edge(0, 1)
graph.add_edge(0, 4)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 3)
graph.add_edge(3, 4)
graph.print_graph()
