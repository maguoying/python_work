#coding=gbk

while(True):
    number_01 = input('������һ�����֣�');
    if(number_01 == 'q'):
            break;
    try:
        number_01 = int(number_01);
    except ValueError:
        print('�޷�ʶ���ַ���������һ������');
        continue;
        
    number_02 = input('��������һ�����֣�');
    if(number_02 == 'q'):
            break;
    try:
        number_02 = int(number_02);
    except ValueError:
        print('�޷�ʶ���ַ���������һ������');
        continue;
    print('����1+����2=' + str(number_01 + number_02));
