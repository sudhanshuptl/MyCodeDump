import threading
from time import sleep

count = 0

def inc(i):
    global count
    print(f"started processing for {i}th thread ")
    count_origional = count
    temp = count
    sleep(0.2)
    temp = temp + 1
    count = temp
    print(f"Count_original: {count_origional} and after increment count = {count}")
    print(f"Completed processing for {i}th thread")


# mythreads = []
# for i in range(20, 0, -1):
#     test = threading.Thread(target=inc, args=(i,))
#     mythreads.append(test)
#     test.start()
#
# # Waiting for completion of each thread before exit
# for th in mythreads:
#     th.join()
#
# print(count)


# Using lock to fix make critical section safe

count = 0


def inc2(i, lock):
    global count
    print(f"started processing for {i}th thread ")
    # taking lock for critical section problem
    lock.acquire()
    count_origional = count
    temp = count
    sleep(0.2)
    temp = temp + 1
    count = temp
    # releasing lock
    lock.release()
    print(f"Count_original: {count_origional} and after increment count = {count}")
    sleep(0.1)
    print(f"Completed processing for {i}th thread")


mythreads = []
lock = threading.Lock()
for i in range(20):
    mythreads.append(threading.Thread(target=inc2, args=(i, lock)))
    mythreads[i].start()

# Waiting for completion of each thread before exit
for th in mythreads:
    th.join()

print(count)
