#coding=gbk
def show_magicians(magicians):
    for magician in magicians:
        print(magician.title());
magicians = ['magy','mayh','mazh'];
show_magicians(magicians)
print('======================分割线========================');
def make_great(magicians):
    end_list = [];
    for magician in magicians:
        endmagician = 'the Great ' + magician;
        end_list.append(endmagician);
    return end_list;
make_magicians = make_great(magicians[:]);
print('原列表：');
show_magicians(magicians);
print('修改后列表：');
show_magicians(make_magicians);
print('======================分割线========================');
def get_toppings(*toppings):
    for topping in toppings:
        print(topping + ' ',end = '');
    print();
get_toppings('a','b','c','d');
get_toppings('d','e');
get_toppings('f','g');
print('======================分割线========================');
def restor_car(name,ver,color='',tow_package=''):
    if color and color:
        car_info = {'name':name,'ver':ver,'color':color,'tow_package':tow_package};
    elif color:
        car_info = {'name':name,'ver':ver,'color':color};
    elif tow_package:
        car_info = {'name':name,'ver':ver,'tow_package':tow_package};
    else:
        car_info = {'name':name,'ver':ver};
    return car_info;
car_info = restor_car('subaru','outback',color = 'blue',tow_package=True);
print(car_info);
print(restor_car('a','sv'))
