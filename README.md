# In-Memory Filesystem
## Objective

Design and implement an in-memory file system. This file-system consists of 4
types of entities: Drives, Folders, Text files, Zip files.

## The Easy Way
Create a full featured file system in-memory.

Use the linux mount type 'tmpfs'.  Use type 'ramfs' if you don't want to bound your memory usage.

To run locally you will need a linux machine (virtual machine OK).

```bash
cd easy_way && ./local_validate.sh
```

Run in a docker instance you will need a linux machine with docker installed.
```bash
cd easy_way && ./docker_validate.sh
```

## How it might be created in code
TBD

