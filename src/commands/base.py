from asyncio import subprocess
import os
from subprocess import check_call, Popen

from click import Command
import uuid
import os

from ..utils.libc import LibcWrapper

class BaseCommand():
    """Base for all other dclone commands.
    """

    def __init__(self, image_name, image_dir, container_dir, command) -> None:
        self.run(image_name, image_dir, container_dir, command)


    def new_root_directory(self):
        """ Create a new root directory
        
        https://wiki.archlinux.org/title/Chroot#Using_chroot
        """
        # placeholder
        return "/mnt/c/Users/natha/COMP/dclone/containers/tmp"
        # create root directory for the container by extrating an image into a new directory

        # chroot into new root directory

        # mount temporary API filesystems
        
        # ...

    def _create_mounts(self, new_root: str):
        """Create container mounts

        Args:
            new_root ([type]): [description]
        """
        # Create mounts (/proc, /sys, /dev) under new_root
        PROC_FLAGS = 0
        SYSFS_FLAGS = 0
        TMPFS_FLAGS = 0
        print(os.path.join(new_root, 'proc'))
        # TODO: Use LibcWrapper.mount() https://stackoverflow.com/questions/1667257/how-do-i-mount-a-filesystem-using-python
        # check_call(['mount', '-t', 'proc' '/proc', os.path.join(new_root, 'proc'), str(PROC_FLAGS), ''])
        # check_call(['mount', '/sysfs', os.path.join(new_root, 'sysfs'), 'sysfs', str(SYSFS_FLAGS), ''])
        # check_call(['mount', '/tmpfs', os.path.join(new_root, 'tmpfs'), 'tmpfs', str(TMPFS_FLAGS), 'mode=755'])
        # Add devices
        pass

    def run(self, image_name, image_dir, container_dir, command, *args, **kwargs):
        """Run the command.

        Args:
            image_name ([type]): [description]
            image_dir ([type]): [description]
            container_dir ([type]): [description]
            command ([type]): [description]
        """
        # Generate id for container
        container_id = str(uuid.uuid4())
        new_root = self.new_root_directory()


        print("BEFORE" , str(os.getpid()))
        # Get root path
        def in_cgroup():
            """Preexec functuion for adding child to cgroup
            """
            try:
                print("PREEXEC_FN" , str(os.getpid()))
                # check_call(['export', "TMP_HOSTNAME=" + container_id])
                
                # create mounts
                self._create_mounts(new_root)
                # TODO: Set uid to root=0 --> does this fix chroot permission?
                # os.setuid(os.geteuid())

                # Chroot
                os.chroot(new_root) # TODO: MAke permissions work? How --> Look into changing uid/gid owner to cgroup?
                # https://github.com/francisbouvier/cgroups/blob/762b8015380e002937b4bfb564e00f97d9a7c539/cgroups/user.py#L62 
                
                # chdir "/"
                os.chdir('/')
                # 
            except Exception as e:
                print(e)
                import traceback
                traceback.print_exc()

        # flags to clone with
            # CLONE_NEWUTS
            # CLONE_NEWPID
        print(command)
        process = Popen(command, preexec_fn=in_cgroup, shell=True)
        process.wait()
        print("AFTER WAIT" , str(os.getpid()))
        