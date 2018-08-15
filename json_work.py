#coding=gbk
import json

filename = 'json_work.json';
flag = True;
try:
    with open(filename) as f_object:
        number = json.load(f_object);
        if number:
        print('我知道你输入的是：'+str(number));
        flag = False;
except FileNotFoundError:
    print('文件不存在！');
else:
    
if flag:
    number = input("请输入一个数字：");
    try:
        number = int(number);
    except ValueError:
        print('你输入的不是数字！');
    with open(filename,'w') as f_object:
        json.dump(number,f_object);
        
    with open(filename) as f_object:
        number = json.load(f_object);
        print('我知道你输入的是：'+str(number));
