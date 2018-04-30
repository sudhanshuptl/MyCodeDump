'''
static method doens not take any argument by default like class or instance method( self,cls )
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

    #static method
    @staticmethod
    def is_working_day(day):
        if day.weekday() == 3 or  day.weekday() == 4: #sat  or sunday
            return  False
        return True


e1 = Employee('sudhanshu', 5000)
e2 = Employee('John Doe', 10000)

print(e1)
print(e2)

import  datetime
my_date = datetime.date(2018, 4, 5)
print('Is working day : ', Employee.is_working_day(my_date))