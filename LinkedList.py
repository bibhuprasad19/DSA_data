class Node:
    def __init__(self,data=None,next=None) -> None:
        self.data=data
        self.next=next
    
class LinkedList:
    def __init__(self) -> None:
        self.head=None

    def insert_at_end(self,data):
        if(self.head is None):
            self.head=Node(data,None)
            return
        itr=self.head
        
        while(itr.next):
            itr=itr.next
        itr.next=Node(data,None)


    def print(self):
        string=""
        if(self.head is None ):
            print(" the linkedList is empty")
            return
        itr=self.head
        while(itr):
            string+=str(itr.data)+" -- " if itr.next else str(itr.data)
            itr =itr.next
        print(string)

    def insert_at_begin(self,data):
        
        node=Node(data,self.head)
        self.head=node

    def get_length(self):
        itr=self.head
        count=0
        while(itr):
            count+=1
            itr=itr.next
        print(count)

    def insert_values(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_at_end(data)
    def insert_at(self,index,data):
        if(index<0 or index>self.get_length()):
            raise Exception("invalid index value")
        if(index==0):
            self.insert_at_begin(data)
            return 
        
print("hello world")

llist=LinkedList()
print(llist)

llist.insert_at_end("apple")
llist.insert_at_end("oranges")
llist.print()
llist.insert_at_begin("grape")
llist.print()
llist.get_length()
llist.insert_values(["apple","orange","banana","grape"])
llist.print()