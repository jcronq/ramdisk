# Design Overview

We implement utilities in a library.  fs/utils.py

We make use of iNodes to manage files, and Directories for names.  Root is a singleton which is held in memory.

![./images/ram_disk_uml.png](images/ram_disk_uml.png)

# Move 

Move is implemented in fs/utils/py.  The flow is also illustrated below.


![./images/Move_flow.png](images/Move_flow.png)
