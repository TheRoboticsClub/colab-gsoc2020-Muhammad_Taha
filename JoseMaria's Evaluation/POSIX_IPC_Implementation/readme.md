### Why use POSIX_IPC implementation?

## Problem with Python shared_memory module:
Python 3.8 introduced the multiprocessing.shared_memory library, which is the first step to implementing IPC tools for communication of unrelated processes. This article was just conceived as a demonstration case of this library usage. However, everything went wrong. As of November 29, 2019, the implementation of shared memory in this library is incorrect – the shared memory object is deleted even if the process just wants to stop using the object without the intention of deleting it. Despite the presence of two calls close () and unlink (), regardless of their call or non-call, the object is deleted when any of the processes using the object terminates.


## Benefits:
The transfer and sharing of objects between processes through shared memory are much more efficient than serialization and deserialization, as it is practically free, therefore it fits great for implementing a low-latency high-bandwidth data exchange between processes within a single node. Unfortunately, if it is required to exchange data between compute nodes, the traditional approaches based on the transmission of messages must be used.



