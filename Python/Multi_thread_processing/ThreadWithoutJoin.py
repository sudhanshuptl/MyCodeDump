import threading
import time


def my_wait_func():
    for i in range(10):
        print('I am in loop ',i)
        time.sleep(2)


th1 = threading.Thread(target=my_wait_func)
th1.start()

print('main_thread Completed')

'''
I am in loop  0
main_thread Completed
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