from abc import ABC , abstractmethod

class Parent(ABC):
    def common(self):
        print('In common method of Parent')
    
    @abstractmethod
    def vary(self):
        pass

class Child1(Parent):
    def vary(self):
        print('Child1 vary method')

class Child2(Parent):
    def vary(self):
        print('Child2 vary method')

#obj of child1 class
child1  = Child1()
child1.common()
child1.vary()

#obj of child2 class
child2 =  Child2()
child2.common()
child2.vary()
