#coding=gbk
class Resturaurant():
    def __init__(self, restaurant_name, cuisine_type):
        """��ʼ������restaurant_name,cuisine_type"""
        self.restaurant_name = restaurant_name;
        self.cuisine_type = cuisine_type;
    def describe_restaurant(self):
        """��ӡ��������"""
        print(self.restaurant_name);
        print(self.cuisine_type);   
    def open_restaurant(self):
        """����Ӫҵ"""
        print('Open for business!');
print('========================�ָ���=========================');

print('������һ��ʵ��');
rest = Resturaurant('�������','����');
print('ͨ��ʵ�����ʱ�����');
print(rest.restaurant_name);
print(rest.cuisine_type);
print('����describe_restaurant()������');
rest.describe_restaurant();
print('����open_restaurant()������');
rest.open_restaurant();
print('========================�ָ���=========================');

print('��������ʵ��')
rest_01 = Resturaurant('�̲��','�̲�');
rest_02 = Resturaurant('ˮ����','ˮ��');
rest_03 = Resturaurant('�����','����');
rest_01.describe_restaurant();
rest_02.describe_restaurant();
rest_03.describe_restaurant();
print('========================�ָ���=========================');

class User():
    def __init__(self,first_name,last_name,summary):
        self.first_name = first_name;
        self.last_name = last_name;
        self.summary = summary;
    
    def describe_user(self):
        print(self.summary);
    
    def greet_user(self):
        print('Welcome,' + self.first_name.title() + ' ' + self.last_name.title());

user_01 = User('Guoying','Ma','�������������');
user_02 = User('Yuhua','Ma','OB��Ұ');
user_03 = User('zhenghua','ma','����');
user_01.greet_user();
user_01.describe_user();
print();
user_02.greet_user();
user_02.describe_user();
print();
user_03.greet_user();
user_03.describe_user();
