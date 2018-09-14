import multiprocessing as mp
import time


class MyProcess(mp.Process):
    def __init__(self, custom_name='No name'):
        self.my_name = custom_name

    def run(self):
        print(f'current process name = {self.my_name} and process_id = {mp.current_process().pid}')
        time.sleep(5)
        print("complete Execution of process :",self.my_name)


if __name__ == '__main__':
    process_1 = MyProcess('Process_1')
    print('This is main process and process_id is : ', mp.current_process().pid)
    process_1.run()
    print('End of main process')