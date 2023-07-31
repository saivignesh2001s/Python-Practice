'''
repr and str methodss\
'''
class Competition:
     def __init__(self,name,prize,country):
         self.__name=name
         self.__prize=prize
         self.__country=country
     def get_name_country(self):
         return "({},{})".format(self.__name,self.__country)
     def __repr__(self):
        return "(name:'{}',prize:{},country:{})".format(self.__name,self.__prize,self.__country)
     def __str__(self):
        return "({},{})".format(self.get_name_country(),self.__prize)

ro=Competition("rowing",7600,"America")
print(repr(ro))
print(str(ro))#first go for __str__() then __repr__
print(ro.__repr__())
print(ro.__str__())

print(int.__add__(1,2))
print(str.__add__('a','3'))

#add special method
class Savings:
      def __init__(self,amount):
          self.__amount=amount
      def __add__(self,other):
          return self.__amount+other.__amount
      def __sub__(self,other):
          return self.__amount-other.__amount
      def __mul__(self,other):
          if(type(other)==int or type(other)==float):
              return self.__amount*other
          else:
              raise ValueError("Can only multiply by int or float")
s1=Savings(1000)
s2=Savings(2000)
print(s1*3)
print(s1+s2)
print(s1.__add__(s2))
#sub,mul,div,mod also possible
print(s1.__sub__(s2))#Now you have * implementation under sub method,sub method invokes mul
print(s1-s2)
#float.__mul__(1,2.1) needs float only

#special methods for other operations
class Floordiv:
    def __init__(self,number):
        self.__number=number
    def __floordiv__(self,other):
        return self.__number//other.__number
    def __mod__(self,other):
        return self.__number%other.__number
    def __pow__(self,other):
        return self.__number**other.__number
f=Floordiv(100)
f1=Floordiv(5)
print(f//f1)
print(f%f1)
print(f**f1)
print(f1**f)

class Participate:
    def __init__(self):
        self.__participants=[]
        self.__index=0
    def add_participants(self,name):
        self.__participants.append(name)
    def __len__(self):
        return len(self.__participants)
    def __iter__(self):
        self.__index=0
        return self
    def __next__(self):
        if(self.__index==len(self.__participants)):
           raise StopIteration
        p=self.__participants[self.__index]
        self.__index=self.__index+1
        return p
s1=Participate()
s1.add_participants("Rama")
print(len(s1))
s1.add_participants("Charu")
for p in s1:
    print(p)
print(len(s1))
print(iter(s1))
print(next(s1))
print(next(s1))
#print(next(s1))
print(list.__dict__)

class wrestler:
    def __init__(self):
        self.__name=''
    def set_name(self,value):
        self.__name=value
    def get_name(self):
        return self.__name
    def del_name(self):
        del self.__name
    name=property(get_name,set_name,del_name)#(fgwt,fset,fdel,doc)
d=wrestler()
d.set_name("Sai")
print(d.get_name())
print(d.name)
#del d.name delete the property
print(d.name)
#d.name d.__name error unless explicit property

#Defining properties using decorators
class wrestler1:
      def __init__(self,name):
          self.__name=name
      @property
      def name(self):
          return self.__name
      @name.setter
      def name(self,value):
          self.__name=value
      @name.deleter
      def name(self):
          del self.__name

w=wrestler1("admin")
print(w.name)
w.name="John"
print(w.name)
del w.name
#print(w.name) throw error if you try to access after deleting it

#Class Methods
'''
Class methods associated with a class
can be accessed with both instance and class methods
'''
class Cop:
    __raise_amount=1.04
    def __init__(self,name,prize):
        self.__name=name
        self.__prize=prize
    def raise_prize(self):
        self.__prize=self.__prize*self.__raise_amount
    def print_details(self):
        print("Name:{} prize:{}".format(self.__name,self.__prize))
    @classmethod
    def get_raise_amount(cls):
        return cls.__raise_amount
    @classmethod
    def set_raise_amount(cls,amount):
        cls.__raise_amount=amount
    @classmethod
    def from_str(cls,compet_str):
        name,prize=compet_str.split('-')
        return cls(name,prize)
d=Cop("swimming",2000)
d.print_details()
d.set_raise_amount(2)
print(d.get_raise_amount())
print(Cop.get_raise_amount())
cp="Swimming-7000"
swim=Cop.from_str(cp)
swim.print_details()

'''
Static methods no reference to class nothing but utility methods
cannot access state associated with class and instance as well
'''
class rect:
    def area(x,y):
        return x*y
    @staticmethod
    def peri(x,y):
        return 2*x + 2*y ;
rect.area=staticmethod(rect.area)
print(rect.area(5,6))
print(rect.peri(5,6))

'''
Abstract base classes
you can't instance 
'''
from abc import ABC,abstractmethod
class Hominidae(ABC):
    @abstractmethod
    def dict(self):
        pass
    @abstractmethod
    def walk(self):
        pass
    def behaviour(self):
        print("they have social manners")
class chim(Hominidae):
    pass
class Human(Hominidae):
    def dict(self):
        print("omnivorous")
    def walk(self):
        print("can walk")
    def behaviour(self):
        print("they have social manners")
Homini=Human()
#can't instantiate the class which have abstract methods

'''
repr,str,add,mul,div,mod and many

class methods =>can access class methods @classmethod
static methods =>should not access both class and instance variables @staticmethod
'''
class Employee:
    def __init__(self,id1):
        self.__id=id1
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,value):
        self.__id=value
    @id.deleter
    def id(self):
        del self.__id
c1=Employee(1001)
print(c1.id)
c1.id=1002
print(c1.id)
del c1.id
print(c1.id)
