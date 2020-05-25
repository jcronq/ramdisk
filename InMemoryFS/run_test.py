from fs.utils import ls, mkdir, move, write, read

print("Test that ls and mkdir work")
print('$ ls /')
print(ls('/'))
print('$ mkdir /home')
mkdir('/home')
print('$ ls /')
print(ls('/'))

print("Test that mv works")
print('$ mv /home /opt')
move('/home', '/opt')
print('$ ls /')
print(ls('/'))

print("Test that text documents work.")
print('$ mkdir /opt/test_data')
mkdir('/opt/test_data')
print('$ ls /')
print(ls('/'))
print('$ ls /opt')
print(ls('/opt'))
print('$ write /opt/test_data/document.txt "Lorem ipsum dolor sit"')
write('/opt/test_data/document.txt', "Lorem ipsum dolor sit")
print('$ ls /opt/test_data')
print(ls('/opt/test_data'))
print('$ cat /opt/test_data/document.txt')
print(read('/opt/test_data/document.txt'))
