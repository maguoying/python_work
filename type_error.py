#coding=gbk

while(True):
    number_01 = input('请输入一个数字：');
    if(number_01 == 'q'):
            break;
    try:
        number_01 = int(number_01);
    except ValueError:
        print('无法识别字符，请输入一个数字');
        continue;
        
    number_02 = input('请再输入一个数字：');
    if(number_02 == 'q'):
            break;
    try:
        number_02 = int(number_02);
    except ValueError:
        print('无法识别字符，请输入一个数字');
        continue;
    print('数字1+数字2=' + str(number_01 + number_02));
