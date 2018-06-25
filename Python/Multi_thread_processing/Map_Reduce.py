from multiprocessing import Pool
import time

def simple_sum(n):
    sum_ = 0
    for i in range(n):
        sum_ +=i
    return sum_

t1 = time.time()
result = []
for i in range(10000):
    result.append(simple_sum(i))

print('Time Elapse for normal excution :,', (time.time() - t1)*1000,'Mili seconds' )


t1 = time.time()
P = Pool()
result = P.map(simple_sum,list(range(10000)))
P.close()
P.join()
print('Time Elapse usaing POOL,', (time.time() - t1)*1000,'Mili seconds' )