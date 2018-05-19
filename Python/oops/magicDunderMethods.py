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

    def __repr__(self):
        '''if str is not defiend basicy this function get used
        here try to return object that can be used to recreat object
        '''
        return "Employee('{}', {})".format(self.name, self.sal)

    def __add__(self, other):
        '''
        :param other object of same class:
        :return: sum of salary of this and other object
        '''
        return self.sal + other.sal

    def __len__(self):
        return len(self.name)

# methods started with __ called dunder method they are special
emp = Employee('Sudhanshu', 1000)
emp2 = Employee('Akash', 20000)

print(repr(emp))

print(int.__add__(1, 2))
print(str.__add__('a', 'b'))

print('Sum of salaries of emp and emp2: ', emp.__add__(emp2))

print('len("test") is same as : ', 'test'.__len__())