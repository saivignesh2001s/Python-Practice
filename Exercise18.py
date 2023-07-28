class A:
    def f(self):
        return self.g()
    def g(self):
        print("A's code here")
class B(A):
    def g(self):
        print("B's code here")
a=A()
b=B()
a.f()
b.f()
a.g()
b.g()
