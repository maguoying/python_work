# coding=gbk  
print('ѭ����ӡ1-20');
for value in range(1,21):
	print(str(value) + ',',end = '');
print();
print('======================================');

numbers = [];
#for value in range(1,1000001) :
#	numbers.append(value);
#for number in numbers :
#	print(number,end='');
#print('======================================');
print('1-1000000֮������������С�����ܺͣ�');
numbers = list(range(1,1000001));
print(max(numbers));
print(min(numbers));
print(sum(numbers));
print('======================================');
print('1-20֮���������');
odd_numbers = list(range(1,21,2));
for odd_number in odd_numbers:
	print(str(odd_number) + ',',end = '');
print();
print('======================================');
print('3-30֮�䱻3����������');
number3s = list(range(3,31,3));
for number3 in number3s:
	print(str(number3) + ',',end = '');
print();
print('======================================');
print('��ӡ1-10ʮ�����ֵ�����');
number4s = list(range(1,11));
number4_ends = [];
for number4 in number4s:
	number4_ends.append(number4**3);
print(number4_ends);
print('======================================');
print('Ӧ���б������ӡ3�η��б�');
squares = [value**3 for value in range(1,11)];
print(squares);
