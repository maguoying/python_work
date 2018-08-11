# coding=gbk  
print('循环打印1-20');
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
print('1-1000000之间的最大数，最小数和总和：');
numbers = list(range(1,1000001));
print(max(numbers));
print(min(numbers));
print(sum(numbers));
print('======================================');
print('1-20之间的奇数：');
odd_numbers = list(range(1,21,2));
for odd_number in odd_numbers:
	print(str(odd_number) + ',',end = '');
print();
print('======================================');
print('3-30之间被3整除的数：');
number3s = list(range(3,31,3));
for number3 in number3s:
	print(str(number3) + ',',end = '');
print();
print('======================================');
print('打印1-10十个数字的立方');
number4s = list(range(1,11));
number4_ends = [];
for number4 in number4s:
	number4_ends.append(number4**3);
print(number4_ends);
print('======================================');
print('应用列表解析打印3次方列表');
squares = [value**3 for value in range(1,11)];
print(squares);
