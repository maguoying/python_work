#coding=gbk
print('==================�ָ���==========================');
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
        
class IceCreamStand(Resturaurant):
    def __init__(self, restaurant_name, cuisine_type,flavors):
        """��ʼ������"""
        super().__init__(restaurant_name,cuisine_type);
        self.flavors = flavors;
        
    def show_flavors(self):
        for flavor in self.flavors:
            print(flavor);
names = ['ţ��','����','����'];
print(names);
print('>>>>>>>>>>>>>>>>>>>>>>>>����show_flavors()����');
iceCream = IceCreamStand('�������','����',names);
iceCream.show_flavors();
print('==================�ָ���==========================');
print('>>>>>>>>>>>>>>>>>>>>>>>>����Admin����');
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
print('>>>>>>>>>>>>>>>>>>>>>>>>��ӡprivileges');
print(privileges);
admin = Admin('guoying','ma','�������������',privileges);
print('>>>>>>>>>>>>>>>>>>>>>>>>����show_privileges()����');
admin.show_privileges();
