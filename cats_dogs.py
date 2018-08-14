#coding=gbk
file_name_cats = 'cats.txt';
file_name_dogs = 'dogs.txt';
try:
    with open(file_name_cats) as cats:
        for line in cats.readlines():
            print(line.rstrip())
except FileNotFoundError:
    print('文件'+ file_name_cats +'不存在');

try:
    with open(file_name_dogs) as dogs:
        for line in dogs.readlines():
            print(line.rstrip())
except FileNotFoundError:
    print('文件'+ file_name_dogs +'不存在');
