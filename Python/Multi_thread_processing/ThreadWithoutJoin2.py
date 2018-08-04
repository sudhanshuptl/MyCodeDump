import threading
import time


def my_wait_func():
    for i in range(10):
        print('I am in loop ',i)
        time.sleep(2)


def main():
    th1 = threading.Thread(target=my_wait_func)
    th1.start()
    return 'Return Main function'

if __name__=='__main__':
    print(main())

    print('ENd of program')

''' result
Return Main function
ENd of program
I am in loop  0
I am in loop  1
I am in loop  2
I am in loop  3
I am in loop  4
I am in loop  5
I am in loop  6
I am in loop  7
I am in loop  8
I am in loop  9
'''