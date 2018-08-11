#coding=gbk
print('================================字典训练==============================')
print('打印编程术语');
courses = {'var':'变量','str':'字符串','num':'数字','list':'列表','dict':'字典'};
for key,value in courses.items():
    print(key + ':',end = '');
    print(value);
print('=============================分割线===================================');
print('打印三大河流流经的地方');
rivers = {'nile':'Egypt','amazon':'peru','chang jiang':'chnia'};
for river,place in rivers.items():
    print('The ' + river.title() + ' runs through ' + place.title() + '.');
print('=============================分割线===================================');
print('打印人物喜欢的语言')
favorite_languages = {'mayh':'english','magy':'korean','fengly':'russian','magx':'german','mazh':'japanese'};
names = ['musha','vsky','fengly','magy'];
print('接受调查的人员名单：');
print(names);
for name in names:
    if(name in favorite_languages.keys()):
        print(name + ',thanks for your take part!');
    else:
        print(name + ',please fill in the paper!');
