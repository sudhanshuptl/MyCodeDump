'''
reegular method passed with instance name as first orgument : self
class method passed with class name as first argument : cls

'''
class Employee:
    raise_percentage  = 1.05
    number_of_employee = 0
    '''
    raise is a class variable shared by all instance of class
    '''
    def __init__(self, name, sal):
        self.name = name
        self.sal = sal
        Employee.number_of_employee +=1

    def raise_salary(self):
        return self.sal * self.raise_percentage

    def __str__(self):
        return self.name + ', ' + str(self.sal) + ', raise = ' + str(self.raise_percentage) + ', new sal = ' + str(self.raise_salary())

    @classmethod #decorator
    def set_raise_amount(cls, percentage):
        '''
        class method has class as first argument
        it can be used to update class variable
        it can be called as class_name,func_name or
        instance_name.func_name and work as same in both case
        '''
        cls.raise_percentage = percentage

    @classmethod
    def from_string(cls, input_string):
        #Alternative Cunstructor
        name, sal = input_string.split('-')
        return cls(name, float(sal))

e1 = Employee('sudhanshu', 5000)
e2 = Employee.from_string('John Doe-10000')

print(e1)
print(e2)

print(e1.__dict__)
print(e2.__dict__)
print('-'*20)
Employee.set_raise_amount(1.09) # it will change class variable value for all instances
print(e1)
print(e2)
print(e1.__dict__)
print(e2.__dict__)

print('Current class variable Value : ', Employee.raise_percentage)
## using class variable to check total number of instance of class created
print('Total Instances ceated till now : ', Employee.number_of_employee)
print('-'*20)
# can be called from instance
e1.set_raise_amount(1.06) # it will change class variable value for all instances
print(e1)
print(e2)
print(e1.__dict__)
print(e2.__dict__)

print('Current class variable Value : ', Employee.raise_percentage)
## using class variable to check total number of instance of class created
print('Total Instances ceated till now : ', Employee.number_of_employee)
