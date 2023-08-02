'''
Singly linked list =>have a pointer to the next node
Doubly linked list=>Have a pointer to both previous and next nodes
'''
class Node:
    def __init__(self,dataval=None,nextval=None):
        self.data=dataval
        self.next=nextval
    def __repr__(self):
        return repr(self.data)
class Linkedlist:
    def __init__(self):
        self.__head=None
    def __repr__(self):
        nodes=[]
        curr=self.__head
        while curr:
            nodes.append(repr(curr))
            curr=curr.next
        return '['+'->'.join(nodes)+']'
    def prepend(self,dataval):#O(1) appending data at the head
        self.__head=Node(dataval=dataval,nextval=self.__head)
    def append(self,dataval):#pappending the data at the end
        if not self.__head:
            self.__head=Node(dataval=dataval)
            return
        curr=self.__head
        while curr.next:
            curr=curr.next
        curr.next=Node(dataval=dataval)
    def  add_after(self,middle_dataval,dataval):#appending the data after the element
        if(middle_dataval is None):
            print("Data to insert after not specified")
        curr=self.__head
        while curr and curr.data!=middle_dataval:
            curr=curr.next
        new_node=Node(dataval=dataval)
        new_node.next=curr.next
        curr.next=new_node
    def find(self,dataval):#find the particular value is present
       curr=self.__head
       '''
        while curr and curr.__dataval!=dataval:
            curr=curr.__next
        return curr
        '''
       while curr:
           if(curr.data==dataval):
               print("found")
               break
           curr=curr.next
    def remove(self,data):#remove value from the data
        curr=self.__head
        prev=None
        while curr and curr.data!=data:
            prev=curr
            curr=curr.next
        if prev is None:
            self.__head=curr.next
        elif curr:
            prev.next=curr.next
            curr.next=None
    def reverse(self):#reverse the list
        curr=self.__head
        prev=None
        next1=None
        while curr:
             nextval=curr.next
             curr.next=prev
             prev=curr
             curr=nextval
        self.__head=prev
    def recursreverse(self):#reverse using recursion
        def recurs(curr,prev):
            if not curr:
                return prev
            nextval=curr.next
            curr.next=prev
            prev=curr
            curr=nextval
            return recurs(curr,prev)
        self.__head=recurs(curr=self.__head,prev=None)
    def countnodes(self):#count the number of nodes
        if self.__head is None:
            return 0
        else:
            count=0
            curr=self.__head
            while curr:
                count+=1
                curr=curr.next
            return count
    def middleval(self):#finding middle value
        if(self.__head is None):
            return
        curr=self.__head
        prev=None
        while curr and curr.next:
            prev=curr
            curr=curr.next.next
        return prev.data
#iterating
num=Linkedlist()
num.append(1)
num.append(2)
print(num)
num.prepend(3)
print(num)
num.add_after(1,6)
print(num)

num.add_after(6,7)
print(num.middleval())
print(num)
print(num.countnodes())
num.find(6)
num.remove(1)
print(num)
num.reverse()
print(num)
num.recursreverse()
print(num)

