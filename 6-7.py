#coding=gbk
print('========================�����ֵ�Ƕ��ѵ��=====================');
friend_0 = {'first_name':'ma', 'last_name':'Yuhua', 'age':'23', 'city':'���'};
friend_1 = {'first_name':'ma', 'last_name':'guoying', 'age':'25', 'city':'����'};
friend_2 = {'first_name':'feng', 'last_name':'liyuan', 'age':'24', 'city':'����'};
peoples = [friend_0,friend_1,friend_2];
for people in peoples:
    for key,value in people.items():
        print(key.title() + ':',end = '');
        print(value.title());
    print();
print('=========================�ָ���===========================');
favorite_places = {'ma guoying':['����','����'],'feng liyuan':['����','����'],'ma yuhua':['���','���׼�']};
for name,places in favorite_places.items():
    print(name.title() + ':',end='');
    for place in places:
        print(place + ' ',end = '');
    print();
print('=========================�ָ���===========================');
likeNum = {'Mayh':['2','6'],'azh':['4','2'],'Magy':['8','9'],'Vsky':['5','0'],'fly':['9','3','4']};

for name,nums in likeNum.items():
    print(name + ':', end = '');
    for num in nums:
        print(num + ' ',end = '');
    print();
print('=========================�ָ���===========================');
cities = {'����':{'country':'�й�','population':'100','fact':'�ٺ�'},'����':{'country':'�й�','population':'20','fact':'����'},'����':{'country':'�й�','population':'30','fact':'õ��'}};
for city,props in cities.items():
    print(city + ':');
    for prop,value in props.items():
        print(prop.title() + ':' + value);
    print();
