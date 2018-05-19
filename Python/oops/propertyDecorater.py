class Employee:
    raise_percentage  = 1.05
    number_of_employee = 0
    '''
    raise is a class variable shared by all instance of class
    '''
    def __init__(self, name, last, sal):
        self.name = name
        self.last = last
        self.sal = sal
        Employee.number_of_employee +=1

    @property
    def email(self):
        return self.name+'@gmail.com'

    def raise_salary(self):
        return self.sal * self.raise_percentage

    def __str__(self):
        return self.fullname + ', Email : ' + self.email + ', ' + str(self.sal) + ', raise = ' \
               + str(self.raise_percentage) + ', new sal = ' + str(self.raise_salary())
    @property
    def fullname(self):
        return self.name+' '+ self.last

    @fullname.setter
    def fullname(self, name):
        self.name, self.last = name.split(' ')

    @fullname.deleter
    def fullname(self):
        print('Delete Name !')
        self.name = ''
        self.last = ''

emp1 = Employee('sudhanshu', 'patel', 44444)
print(emp1)

emp1.name = 'Shaan'
print('changing the name will not change email id'
      'but here we achieve that by using property decorater')
print(emp1)

emp1.fullname = 'Shaan kumar'
print(emp1)

del emp1.fullname
print(emp1)