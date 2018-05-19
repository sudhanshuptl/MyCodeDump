
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


class Developer(Employee):
    pass
    '''
    It will have all the property od Employee class 
    '''


dev1 = Developer('Sudhanshu', 5000)
dev2 = Developer('Akash', 10000)
emp = Employee('Dummy',2000)

print(dev1)
print(dev2)
print(emp)

print('\n Updating class variable for developer , it should not effect class variable of employee object')
Developer.raise_percentage = 1.7

print(dev1)
print(dev2)
print(emp)

# It uses method resolution if not defiend in developer it look up
print(help(Developer))