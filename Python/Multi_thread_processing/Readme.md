# [Global Interpreter lock](https://realpython.com/python-gil/)

The Python Global Interpreter Lock or GIL, in simple words, is a mutex (or a lock) that allows only one thread to hold the control of the Python interpreter.

This means that only one thread can be in a state of execution at any point in time. The impact of the GIL isn’t visible to developers who execute single-threaded programs, but it can be a performance bottleneck in CPU-bound and multi-threaded code.

Why GIL exist if it cause bottleneck :  for memory management python keep track of reference count so
this reference count variable needed protection from race conditions where two threads increase or decrease its value simultaneously

This reference count variable can be kept safe by adding locks to all data structures that are shared across threads so that they are not modified inconsistently.But adding a lock to each object or groups of objects means multiple locks will exist which can cause another problem—Deadlocks

The GIL is a single lock on the interpreter itself which adds a rule that execution of any Python bytecode requires acquiring the interpreter lock. This prevents deadlocks (as there is only one lock) and doesn’t introduce much performance overhead. But it effectively makes any CPU-bound Python program single-threaded.

## Benefits of GIL
* Solved above problem
* A lot of extensions were being written for the existing C libraries whose features were needed in Python. To prevent inconsistent changes, these C extensions required a thread-safe memory management which the GIL provided.
* The GIL is simple to implement and was easily added to Python. It provides a performance increase to single-threaded programs as only one lock needs to be managed.
* C libraries that were not thread-safe became easier to integrate. And these C extensions became one of the reasons why Python was readily adopted by different communities.

```The impact on multi-threaded Python programs
CPU-bound programs are those that are pushing the CPU to its limit.
 I/O-bound programs are the ones that spend time waiting for Input/Output which can come from a user, file, database, network, etc.
 ```

For any CPU bound job threading may cause bottleneck as we know only one thread can run at a time. And there is context overhead for switching thread.
That cause threaded program in python take more time then normal program.
[EX_link:](https://realpython.com/python-gil/)

```The GIL does not have much impact on the performance of I/O-bound multi-threaded programs as the lock is shared between threads while they are waiting for I/O.```

##### what about the programs where some threads are I/O-bound and some are CPU-bound?
In such programs, Python’s GIL was known to starve the I/O-bound threads by not giving them a chance to acquire the GIL from CPU-bound threads.
This was because of a mechanism built into Python that forced threads to release the GIL after a fixed interval of continuous use and if nobody else acquired the GIL, the same thread could continue its use.

## How to deal with Python’s GIL
If the GIL is causing you problems, here a few approaches you can try:
Multi-processing vs multi-threading: The most popular way is to use a multi-processing approach where you use multiple processes instead of threads. Each Python process gets its own Python interpreter and memory
