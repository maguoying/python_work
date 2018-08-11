#coding=gbk
print('========================代码开始=============================');
print('模拟管理员和普通用户登录情形');
names = ['admin','vsky','magy','mayh','mazh'];
#names = [];
while(True):
    if not names :
        print('We need to find some users!');
        break;
    name = input('Please input your name:');
    if(name == 'q'):
        break;
    if(name not in names):
        print("You havn't registered.");
        continue;
    if(name == 'admin'):
        print('Hello admin,would you like to see a status report?');
    else:
        print('Hello ' + name + ',thank you for logging in again.');
print();
print('================================================================');
print('检查用户名,不区分大小写')
current_users = ['admin','vsky','magy','mayh','mazh'];
new_users = ['Vsky','Magy','Fly','Lzp','Mz'];
for new_user in new_users:
    if(new_user.lower() in (current_user.lower() for current_user in current_users)):
        print('Name' + new_user + 'is used,please choose another one.');
    else:
        print('You can use the name ' + new_user);
print('================================================================');
print('打印1-9的序数');
numbers = [1,2,3,4,5,6,7,8,9];
for number in numbers:
    if(number == 1):
        print('1st');
    elif(number == 2):
        print('2nd');
    elif(number == 3):
        print('3rd');
    else:
        print(str(number)+'th');
