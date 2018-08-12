#coding=gbk
def display_message():
    print('I learn function in this part.');
display_message();

def favorite_book(title):
    print('One of my favorite books is ' + title + '.');
favorite_book('Alice in Wonderland');
print('==============================分割线===============');
def make_shirt(size,paint):
    print('The T-shirt size:' + size + ',paint: ' + paint);
make_shirt('small','cat');
make_shirt(paint = 'dog', size='big')

def make_shirt(size,paint = 'I love Python'):
    print('The T-shirt size:' + size + ',paint: ' + paint);
make_shirt('big');
make_shirt('middle');
make_shirt('big', 'Java');
print('==============================分割线===============');
def describe_city(city, country = 'China'):
    print(city + 'is in ' + country);
describe_city('hangzhou');
describe_city('Los','America');
describe_city('mexico','Russia');
