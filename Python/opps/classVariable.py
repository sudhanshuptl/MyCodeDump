
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

e1 = Employee('sudhanshu', 5000)
e2 = Employee('John Doe', 10000)

print(e1)
print(e2)

print(e1.__dict__)
print(e2.__dict__)

e1.raise_percentage = 1.07
# Here e1 instance change the value of raise_percentage but it does not change value for class variable
# value of Employee.raise_percentage will be same for all class,
# but if any instance change the value because raise_percentage created as instance variable look at dict print
# than e1.raise_percentage (self. raise_percentage )can have different value or updated value of class variable

print(e1)
print(e2)
print(e1.__dict__)
print(e2.__dict__)

print('Current class variable Value : ', Employee.raise_percentage)

## using class variable to check total number of instance of class created
print('Total Instances ceated till now : ', Employee.number_of_employee)