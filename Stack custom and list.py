stack=[]
stack.append("US")
stack.append("GBB")
stack.append("China")
print(stack)
stack.pop()
print(stack)

class Stack:
    def __init__(self,num):
        self.__list=[]
        self.__capacity=num
    def empty(self):
        return len(self.__list)==0
    def full(self):
        return len(self.__list)==self.__capacity
    def push(self,num):
        if(self.full()):
            raise Exception("No more elements can be pushed")
        self.__list.append(num)
    def pop(self):
        if(self.empty()):
            raise Exception("You can't pop an empty stack")
        return self.__list.pop()
    def items(self):
        return self.__list[::-1]
    def size(self):
        return len(self.__list)
    def top(self):
        if(self.empty()):
            raise Exception("You can't have top element in empty stack")
        return self.__list[-1]
s=Stack(5)
#print(s.pop()) empty stack exception
print(s.empty())
print(s.full())
s.push("USA")
s.push("GBB")
print(s.items())
print(s.size())
print(s.top())
    
