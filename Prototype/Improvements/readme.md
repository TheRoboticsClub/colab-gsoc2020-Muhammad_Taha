# Spawning Independent Processes Without Copying Memory:

As in multiprocessing processes, the whole process memory is copied into the child process. In this improvement I will try to run independent processes so they are lightweight and don't inherit memory from the parent process.
Running independent command line processes requires string arguments and not objects.
So, I wrote a custom serializer/deserializer which converts all arguments to a string which can then be passed onto command line and then deserialized back to arguments.


# Fixing Memory Leaks:
The POSIX_IPC uses kernel level commands to share memory between processes. The main issue here was that if I kill the Python processes using the parent process, it would cause memory leak because the shared memory is not released. This is written in the POSIX_IPC documentation:

"You must call close_fd() or os.close() explicitly; the file descriptor is not closed automatically when a SharedMemory object is garbage collected."

So I came up with a way to signal every process to safely terminate and release the shared memory.
Each process will regularly check if the parent process is still alive, if it has exited, all processes will know and then they can safely unlink and de-allocate the shared memory preventing any memory leaks.
