# Tasks
* A task executes a coroutine in an even loop
* at Each Step the coroutine either
    * Awaits(Yeild) a future
    * awaits (yeild) another coroutine
    * return a result

# Select Module
* Select is an OS function to wait for I/O
* It tells you which, IF any I/O channels are ready
* I/O channels can be files, Sockets or pipes
* It can wait a fixed length of time indefinitely

# Asyncio Transport
* Transport are communication channels
* Responsible for performing I?O & buffering
* There are Several types
    * TCP, UDP,SSL,Pipes

## Other Type of transport
* Subprocess
    * The API includes methods such as 
        * get_pid, get_pipe_transport, terminate,kill
    * Datagram Transport
        * API includes: sendto, abort
* We don't create transport directly
* instead the event loop supplies methods
* for example
    * create_connection
    * create_server
    * subprocess_exec
* each takes `protocol` factory as its first argument

# Protocols
* Asyncio protocols process received data
    * and ask the transport to send the data
* Again there a several type
    * Streaming , Datagram, subprocess

* Your Application will create a subclass of one