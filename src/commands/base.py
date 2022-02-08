from asyncio import subprocess
import os
from subprocess import check_call, Popen

from click import Command

class BaseCommand():
    """Base for all other dclone commands.
    """
    def __init__(self, image_name, image_dir, container_dir, command) -> None:
        self.run(image_name, image_dir, container_dir, command)

    def __mount_proc__(self, new_root: str):
        """ Call the mount syscall using the subprocess module

        Args:
            new_root (str): Root directory of the container
        """
        source = 'proc'
        target = os.path.expanduser(os.path.join(new_root, 'proc'))
        fs_type = 'proc'
        mount_flags = 0
        data = ''
        check_call(['mount', source, target, fs_type, mount_flags, data])

    def new_root_directory(self):
        """ Create a new root directory
        
        https://wiki.archlinux.org/title/Chroot#Using_chroot
        """
        pass
        # create root directory for the container by extrating an image into a new directory

        # chroot into new root directory

        # mount temporary API filesystems
        
        # ...


    def run(self, image_name, image_dir, container_dir, command, *args, **kwargs):
        # Get root path
        # 
        Popen(command)