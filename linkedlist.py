class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insertatbeg(self,value):
        newnode=Node(value)
        if self.head==None:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head=newnode
    def insertatend(self,value):
        newnode=Node(value)
        if self.head==None:
            self.head=newnode
        else:
            cur=self.head
            while cur.next!=None:
                cur=cur.next
            cur.next=newnode
    def deleteatbeg(self):
        if self.head==None:
            print("List is empty")
            return 0
        else:
            self.head=self.head.next
    def deleteatend(self):
        if self.head==None:
            print("List is empty")
            return 0
        else:
            cur=self.head
            while cur.next.next!=None:
                cur=cur.next
            cur.next=None
    def middle(self,value):
        if self.count==1:
            self.head.next=newnode
        else:
            i=1
            half=self.count//2
            cur=self.head
            while i!=half:
                cur=cur.next
                i+=1
            newnode.next=cur.next
    def countnode(self):
        cur=self.head
    def printlist(self):
        cur=self.head
        while(cur!=None):
            print(cur.data,end="-->")
            cur=cur.next
        print("null")
l=LinkedList()
l.insertatbeg(4)
l.insertatbeg(3)
l.insertatbeg(2)
l.insertatbeg(1)
l.insertatend(13)
l.deleteatbeg()
l.deleteatend()
l.printlist()