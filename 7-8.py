#coding=gbk
sandwich_orders = ['tuna','meat','pastrami','tomato','pastrami','pastrami'];
finished_sandwiches = [];
while sandwich_orders:
    sandwich_order = sandwich_orders.pop();
    print('I made your ' + sandwich_order);
    finished_sandwiches.append(sandwich_order);
print();
for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche + ' has finished.');
print('======================�ָ���===================');
print('Pastrami�Ѿ�������');
print('Pastrami has been used all.');
sandwich_orders = ['tuna','meat','pastrami','tomato','pastrami','pastrami'];
print(sandwich_orders);
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami');
print('�Ƴ����')
for sandwich in sandwich_orders:
    print(sandwich);
print('======================�ָ���===================');
print('����Ķȼ�ʤ��');
places = [];
while (1):
    message = 'If you could visit one place in the world,where would you go?';
    place = input(message);
    if(place == 'q'):
        break;
    places.append(place);
print(places);
