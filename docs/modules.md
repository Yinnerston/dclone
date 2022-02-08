nsenter: Create namespace, access currently running docker container
cgroups: Create control groups
subprocess: Popen has kwarg preexec_fn which can run callables inside forked process before running the opened process
    - Add process to control group
    - Enter network namespace
    - File handles?
pyroute2: Allows you to treat the network configuration as an object instance
    - Vaddr, routing table, virtual interface
os: Can call Chroot --> Can be called in subprocess preexec_fn
