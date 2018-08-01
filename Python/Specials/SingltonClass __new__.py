

class DemoSinglton(object):
    _instance_count = 0

    def __init__(self, name):
        print('I am in __init__()')
        self.name = name

    def __new__(cls, *args, **kwargs):
        print('I am in __new__')
        if cls._instance_count <1:
            cls._instance_count += 1
            # object is super class
            instance = object.__new__(cls)
            return instance
        else:
            raise TypeError('It is singlton class so only one instace allowed')

    def __del__(self):
        DemoSinglton._instance_count -=1

if __name__ == '__main__':
    obj1 = DemoSinglton(name='sudhanshu')
    print(obj1.name)
    print('Try to create another instance')
    # del obj1
    try:
        obj2 = DemoSinglton('Shaan')
        print(obj2.name)
    except Exception as e:
        print('Error in object creation :',e)