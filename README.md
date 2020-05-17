# In-Memory Filesystem
## Objective

Design and implement an in-memory file system. This file-system consists of 4
types of entities: Drives, Folders, Text files, Zip files.

## The Easy Way (Optimal Solution)
Filesystems are hard.  One should not attempt to reinvent the wheel whenever possible, especialy so when that wheel is something that has taken decades to get right.  I cannot recommended enough using available tools to satisfy a requirement whenever possible.

**REQUIREMENTS:** Access to a linux machine with root permissions (need to be able to call mount/umount).

###Implementation
Use the linux 'tmpfs' mount.  Use type 'ramfs' if you don't want to bound your memory usage.

To run locally you will need a linux machine (virtual machine OK).

```bash
# root access required.  If not super-user add sudo when calling ./local_validate.sh

git clone https://github.com/jcronq/ramdisk.git
cd ramdisk/easy_way && ./local_validate.sh
```

Run in a docker instance you will need a linux machine with docker installed (virtual machine OK).
```bash
# root access required.  If not super-user add sudo when calling ./local_validate.sh
#
# Assumption here is you didn't just download and run the local version. 

https://github.com/jcronq/ramdisk.git
cd ramdisk/easy_way && ./docker_validate.sh
```

## How it might be created in code
It's assumed that the reason for this request is to test coding skills.  So now I'll demonstrate how this system would be designed assuming no ram-disk tools are available for one reason or another. 

Pending...

- Design
- Sketch of "move" flow
- Implement size function
