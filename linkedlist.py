class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class linkedlist:
    
    def __init__(self):
        self.head=None
    
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    
    def pushend(self,prev_node,new_data):
        if prev_node is None:
            pirnt("error")
        new_node=Node(new_data)
        new_node.next=prev_node.next
        prev_node.next=new_node
        
    
    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
            
l=linkedlist()
for i in range(5):
    i=input()
    l.push(i)
l.pushend(l.head.next,7)
l.printlist()
