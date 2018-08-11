#coding=gbk
print('========================进入字典嵌套训练=====================');
friend_0 = {'first_name':'ma', 'last_name':'Yuhua', 'age':'23', 'city':'广河'};
friend_1 = {'first_name':'ma', 'last_name':'guoying', 'age':'25', 'city':'东乡'};
friend_2 = {'first_name':'feng', 'last_name':'liyuan', 'age':'24', 'city':'临夏'};
peoples = [friend_0,friend_1,friend_2];
for people in peoples:
    for key,value in people.items():
        print(key.title() + ':',end = '');
        print(value.title());
    print();
print('=========================分割线===========================');
favorite_places = {'ma guoying':['兰州','西安'],'feng liyuan':['临夏','杨凌'],'ma yuhua':['广河','三甲集']};
for name,places in favorite_places.items():
    print(name.title() + ':',end='');
    for place in places:
        print(place + ' ',end = '');
    print();
print('=========================分割线===========================');
likeNum = {'Mayh':['2','6'],'azh':['4','2'],'Magy':['8','9'],'Vsky':['5','0'],'fly':['9','3','4']};

for name,nums in likeNum.items():
    print(name + ':', end = '');
    for num in nums:
        print(num + ' ',end = '');
    print();
print('=========================分割线===========================');
cities = {'兰州':{'country':'中国','population':'100','fact':'百合'},'东乡':{'country':'中国','population':'20','fact':'土豆'},'临夏':{'country':'中国','population':'30','fact':'玫瑰'}};
for city,props in cities.items():
    print(city + ':');
    for prop,value in props.items():
        print(prop.title() + ':' + value);
    print();
