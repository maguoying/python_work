#coding=gbk
print('==================分割线==========================');
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
        
class IceCreamStand(Resturaurant):
    def __init__(self, restaurant_name, cuisine_type,flavors):
        """初始化方法"""
        super().__init__(restaurant_name,cuisine_type);
        self.flavors = flavors;
        
    def show_flavors(self):
        for flavor in self.flavors:
            print(flavor);
names = ['牛肉','羊肉','鸡肉'];
print(names);
print('>>>>>>>>>>>>>>>>>>>>>>>>调用show_flavors()方法');
iceCream = IceCreamStand('老马烤肉店','烤肉',names);
iceCream.show_flavors();
print('==================分割线==========================');
print('>>>>>>>>>>>>>>>>>>>>>>>>测试Admin子类');
class User():
    def __init__(self,first_name,last_name,summary):
        self.first_name = first_name;
        self.last_name = last_name;
        self.summary = summary;
    
    def describe_user(self):
        print(self.summary);
    
    def greet_user(self):
        print('Welcome,' + self.first_name.title() + ' ' + self.last_name.title());

class Admin(User):
    def __init__(self,first_name,last_name,summary,privileges):
        super().__init__(first_name,last_name,summary);
        self.privileges = privileges;
        
    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege);

privileges = ['can add post','can delete post','can ban user'];
print('>>>>>>>>>>>>>>>>>>>>>>>>打印privileges');
print(privileges);
admin = Admin('guoying','ma','麦田里的守望者',privileges);
print('>>>>>>>>>>>>>>>>>>>>>>>>调用show_privileges()方法');
admin.show_privileges();
