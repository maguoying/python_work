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
