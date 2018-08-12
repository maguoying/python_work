#coding gbk
card = input('What car do you want?');
print('Let me see if I can find you a Subaru');

peoples = input('How many people here?');
if int(peoples) > 8:
    print('Sorry,there are no desk enough.');
else:
    print('Desk enough.');
    
number = input('Input a number:');
number = int(number);
if number % 10 == 0:
    print('It can be devided by 10.')
else:
    print("It can't be devided by 10.")
