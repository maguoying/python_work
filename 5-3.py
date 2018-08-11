# coding=gbk  
alien_color = 'green';
if(alien_color =='green'):
    print('You shoot it,get 5 points');
elif(alien_color != 'green'):
    print('You get 10 points!');
print('===============================');

alien_color = 'yellow';
if(alien_color =='green'):
    print('You shoot it,get 5 points');
elif(alien_color != 'green'):
    print('You get 10 points!');
print('===============================');

alien_color = 'red';
if(alien_color =='green'):
    print('You get 5 points!');
elif(alien_color == 'yellow'):
    print('You get 10 points!');
elif(alien_color == 'red'):
    print('You get 15 points!')
print('===================================');
while(True):
    age = input('Please input the age:');
    if(age == 'q'):
        print('You choose exist.');
        break;
    age = int(age);
    if(age < 2):
        print('婴儿.');
    elif(age < 4 ):
        print('蹒跚学步');
    elif(age < 13):
        print('儿童');
    elif(age < 20):
        print('青少年');
    elif(age < 65):
        print('成年人');
    elif(age >= 65):
        print('老年人');
print('===================================');
favorite_fruits = ['apple','banana','pear'];
print('favorite_fruits:');
print(favorite_fruits);
if('banana' in favorite_fruits):
    print('You really like bananas.');
if('peach' not in favorite_fruits):
    print("You not like peach.");
