#coding=gbk
print('=========================分割线==========================');
class Resturaurant():
    def __init__(self, restaurant_name, cuisine_type):
        """初始化属性restaurant_name,cuisine_type"""
        self.restaurant_name = restaurant_name;
        self.cuisine_type = cuisine_type;
        self.number_served = 0;
        
    def describe_restaurant(self):
        """打印两个属性"""
        print(self.restaurant_name);
        print(self.cuisine_type);   
        
    def open_restaurant(self):
        """正在营业"""
        print('Open for business!');
        
    def set_number_served(self, number_served):
        self.number_served = number_served;
        
    def increment_number_served(self, number_served):
        self.number_served += number_served;
        
rest = Resturaurant('老马烤肉店','烤肉');
print(rest.number_served);
rest.number_served = 2;
print(rest.number_served);
rest.set_number_served(6);
print(rest.number_served);
rest.increment_number_served(300);
print(rest.number_served);

print('=========================分割线==========================');
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
        
user = User('guoying','ma','麦田里的守望者');
user.increment_login_attempts();
user.increment_login_attempts();
user.increment_login_attempts();
print('打印登陆次数：');
print(user.login_attempts);
user.reset_login_attempts();
print('重置后的登录次数：');
print(user.login_attempts);
