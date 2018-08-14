#coding=gbk
file_name = 'guest.txt';
while(1):
    guest_name = input('Input your name:');
    if(guest_name == 'q'):
        break;
    with open(file_name, 'a') as fo:
        fo.write(guest_name + '\n');
print('=======================分割线====================');
