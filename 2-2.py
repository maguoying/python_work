names = ["mayh","magy","mazh"];
for name in names:
	print("Dear " + name + ",Mr.Tian invite you to dinner.");
print(names[2] + "cannot come to the dinner.");
print('======================================================');
#del names[2];
#names.insert(2,'cuij');
names[2] = 'cuij';
for name in names:
	print("Dear " + name + ",Mr.Tian invite you to dinner.");
print('======================================================');
print('I find a larger desk!');
print('======================================================');
names.insert(0,'fly');
names.insert(2,'tlh');
names.append('afy');
for name in names:
	print("Dear " + name + ",Mr.Tian invite you to dinner.");
print('======================================================');
print(names);
print('I can only invite 2 friends!');
print('======================================================');
print(names[-1] + ',sorry,you are deleted!');
names.pop();
print(names[-1] + ',sorry,you are deleted!');
names.pop();
print(names[-1] + ',sorry,you are deleted!');
names.pop();
print(names[-1] + ',sorry,you are deleted!');
names.pop();
for name in names:
	print(name + ',you are invited!');
print(names);
print('======================================================');
print('delete 2 left.')
del names[0];
del names[0];
print(names);
