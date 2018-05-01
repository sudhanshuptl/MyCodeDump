
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
    '''
    It will have all the property od Employee class
    '''
    def __init__(self, name, sal, prog_lang):
        super().__init__(name, sal)
        self.prog_lang = prog_lang

    def __str__(self):
        return super().__str__() + ', programming lang : '+self.prog_lang


class Manager(Employee):
    def __init__(self, name, sal, employee = None):
        super().__init__(name, sal)
        if employee is None:
            self.employee = []
        else:
            self.employee = employee

    def add_employee(self, emp):
        if emp not in self.employee:
            self.employee.append(emp)

    def remove_employee(self, emp):
        if emp in self.employee:
            self.employee.remove(emp)

    def print_employee(self):
        for emp in self.employee:
            print('--->', emp)
        print('\n\n')

dev1 = Developer('Sudhanshu', 5000, 'python')
dev2 = Developer('Akash', 10000,'C++')
mng = Manager('Roshani', 15000, [dev2])

mng.print_employee()

print('Add new Employee to manager')
mng.add_employee(dev1)
mng.print_employee()

print('Remove a employee from manager')
mng.remove_employee(dev2)
mng.print_employee()

print('Check if object is instance of given class ')
print('mng is instance of Manager class :', isinstance(mng, Manager))
print('dev2 is instance of Manager class:', isinstance(dev2, Manager))

print('\n\nCheck if class is subclass of given class ')
print('is developer is subclass of emplyee : ', issubclass(Developer, Employee))