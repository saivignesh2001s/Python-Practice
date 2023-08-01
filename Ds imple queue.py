from queue import Queue
olympics=Queue(5)
print(olympics)
olympics.put("United states")#enqueue
olympics.put("Great britain")
print(olympics.empty())
print(olympics.full())
print(olympics.qsize())
olympics.put("China")
olympics.put("Russia")
olympics.put("Germany")
print(olympics.get())
print(olympics.qsize())
print(Queue.__dict__)
help(Queue)

#Custom
class MyQueue:
    def __init__(self,num):
        self.__list=[]
        self.__size=num
    def empty(self):
        if(len(self.__list)>0):
            return False
        else:
            return True
    def full(self):
        if(len(self.__list)==self.__size):
            return True
        else:
            return False
    def enqueue(self,num):
        if self.full():
            raise Exception("You can't enqueue any more elements")
        self.__list.append(num)
    def size(self):
        return len(self.__list)
    def dequeue(self):
        if self.empty():
            raise Exception("No elements present to dequeue")
        p=self.__list[0]
        return self.__list.pop(0)
    def items(self):
        return self.__list
    def peek(self):
        if self.empty()!=True:
            return self.__list[0]
        else:
            raise ValueError("queue is empty")
        
g=MyQueue(5)
#g.dequeue() queue empty so you can't dequeue any elements
print(g.empty())
print(g.full())
#g.peek() queue empty so you can't have any elements at the front
g.enqueue("United states")
g.enqueue("Great britain")
print(g.size())

print(g.empty())
print(g.full())
print(g.size())
g.enqueue("China")
g.enqueue("Russia")
g.enqueue("Germany")
#g.enqueue("France") queue full exception
print(g.empty())
print(g.full())
print(g.size())
print(g.dequeue())
print(g.peek())
print(g.items())
