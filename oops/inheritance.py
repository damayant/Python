class Person(object):

    def __init__(self,name) :
        self.name =  name

    def get_name(self):
        return self.name 
    
    def is_employee(self):
        return False
    

class Employee(Person):

    def is_employee(self):
        return True

#driver code
emp = Person('person 1')
print("{} is employee: {}".format(emp.get_name(), emp.is_employee()))

emp = Employee('person 2')
print("{} is employee: {}".format(emp.get_name(), emp.is_employee()))
