#Write a Python program to calculate the surface volume and area of a sphere.
import os
path = 'e:\\testpath\\p.txt'
fd = os.open(path, os.O_RDWR)
info = os.fstat(fd)
print (f"ID of device containing file: {info.st_dev}")
print (f"Inode number: {info.st_ino}")
print (f"Protection: {info.st_mode}")
print (f"Number of hard links: {info.st_nlink}")
print (f"User ID of owner: {info.st_uid}")
print (f"Group ID of owner: {info.st_gid}")
print (f"Total size, in bytes: {info.st_size}")
print (f"Time of last access: {info.st_atime}")
print (f"Time of last modification: {info.st_mtime }")
print (f"Time of last status change: {info.st_ctime }")
os.close(fd)




#Write a Python program to run an operating system command using the OS module.
import os
if os.name == "nt":
    command = "dir"
else:
    command = "ls-l"
os.system(command)




#Write a Python program to get the size, permissions, owner, device, created, last modified and last accessed date and time of a specified path.
import os
import sys
import time
path = 'g:\\testpath\\'
print('Path Name({}):'.format(path))
print('Size:', stat_info.st_size)
print('Permissions:', oct(stat_info.st_mode))
print('Owner:', stat_info.st_uid)
print('Device:', stat_info.st_dev)
print('Created     :', time.ctime(stat_info.st_ctime))
print('Last modified:', time.ctime(stat_info.st_mtime))
print('Last accessed:', time.ctime(stat_info.st_atime))
