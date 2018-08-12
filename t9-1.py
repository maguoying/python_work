#coding=gbk
class Resturaurant():
    def __init__(self, restaurant_name, cuisine_type):
        """初始化属性restaurant_name,cuisine_type"""
        self.restaurant_name = restaurant_name;
        self.cuisine_type = cuisine_type;
    def describe_restaurant(self):
        """打印两个属性"""
        print(self.restaurant_name);
        print(self.cuisine_type);   
    def open_restaurant(self):
        """正在营业"""
        print('Open for business!');
print('========================分割线=========================');

print('创建第一个实例');
rest = Resturaurant('老马烤肉店','烤肉');
print('通过实例访问变量：');
print(rest.restaurant_name);
print(rest.cuisine_type);
print('调用describe_restaurant()方法：');
rest.describe_restaurant();
print('调用open_restaurant()方法：');
rest.open_restaurant();
print('========================分割线=========================');

print('创建三个实例')
rest_01 = Resturaurant('奶茶店','奶茶');
rest_02 = Resturaurant('水果店','水果');
rest_03 = Resturaurant('拉面馆','拉面');
rest_01.describe_restaurant();
rest_02.describe_restaurant();
rest_03.describe_restaurant();
print('========================分割线=========================');

class User():
    def __init__(self,first_name,last_name,summary):
        self.first_name = first_name;
        self.last_name = last_name;
        self.summary = summary;
    
    def describe_user(self):
        print(self.summary);
    
    def greet_user(self):
        print('Welcome,' + self.first_name.title() + ' ' + self.last_name.title());

user_01 = User('Guoying','Ma','麦田里的守望者');
user_02 = User('Yuhua','Ma','OB打野');
user_03 = User('zhenghua','ma','大阪');
user_01.greet_user();
user_01.describe_user();
print();
user_02.greet_user();
user_02.describe_user();
print();
user_03.greet_user();
user_03.describe_user();
