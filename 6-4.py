#coding=gbk
print('================================�ֵ�ѵ��==============================')
print('��ӡ�������');
courses = {'var':'����','str':'�ַ���','num':'����','list':'�б�','dict':'�ֵ�'};
for key,value in courses.items():
    print(key + ':',end = '');
    print(value);
print('=============================�ָ���===================================');
print('��ӡ������������ĵط�');
rivers = {'nile':'Egypt','amazon':'peru','chang jiang':'chnia'};
for river,place in rivers.items():
    print('The ' + river.title() + ' runs through ' + place.title() + '.');
print('=============================�ָ���===================================');
print('��ӡ����ϲ��������')
favorite_languages = {'mayh':'english','magy':'korean','fengly':'russian','magx':'german','mazh':'japanese'};
names = ['musha','vsky','fengly','magy'];
print('���ܵ������Ա������');
print(names);
for name in names:
    if(name in favorite_languages.keys()):
        print(name + ',thanks for your take part!');
    else:
        print(name + ',please fill in the paper!');
