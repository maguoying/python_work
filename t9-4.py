#coding=gbk
print('=========================�ָ���==========================');
class Resturaurant():
    def __init__(self, restaurant_name, cuisine_type):
        """��ʼ������restaurant_name,cuisine_type"""
        self.restaurant_name = restaurant_name;
        self.cuisine_type = cuisine_type;
        self.number_served = 0;
        
    def describe_restaurant(self):
        """��ӡ��������"""
        print(self.restaurant_name);
        print(self.cuisine_type);   
        
    def open_restaurant(self):
        """����Ӫҵ"""
        print('Open for business!');
        
    def set_number_served(self, number_served):
        self.number_served = number_served;
        
    def increment_number_served(self, number_served):
        self.number_served += number_served;
        
rest = Resturaurant('�������','����');
print(rest.number_served);
rest.number_served = 2;
print(rest.number_served);
rest.set_number_served(6);
print(rest.number_served);
rest.increment_number_served(300);
print(rest.number_served);

print('=========================�ָ���==========================');
class User():
    def __init__(self,first_name,last_name,summary):
        self.first_name = first_name;
        self.last_name = last_name;
        self.summary = summary;
        self.login_attempts = 0;
    
    def describe_user(self):
        print(self.summary);
    
    def greet_user(self):
        print('Welcome,' + self.first_name.title() + ' ' + self.last_name.title());

    def increment_login_attempts(self):
        self.login_attempts += 1;
        
    def reset_login_attempts(self):
        self.login_attempts = 0;
        
user = User('guoying','ma','�������������');
user.increment_login_attempts();
user.increment_login_attempts();
user.increment_login_attempts();
print('��ӡ��½������');
print(user.login_attempts);
user.reset_login_attempts();
print('���ú�ĵ�¼������');
print(user.login_attempts);
