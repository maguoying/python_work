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
