#coding=gbk
import json

filename = 'json_work.json';
flag = True;
try:
    with open(filename) as f_object:
        number = json.load(f_object);
        if number:
        print('��֪����������ǣ�'+str(number));
        flag = False;
except FileNotFoundError:
    print('�ļ������ڣ�');
else:
    
if flag:
    number = input("������һ�����֣�");
    try:
        number = int(number);
    except ValueError:
        print('������Ĳ������֣�');
    with open(filename,'w') as f_object:
        json.dump(number,f_object);
        
    with open(filename) as f_object:
        number = json.load(f_object);
        print('��֪����������ǣ�'+str(number));
