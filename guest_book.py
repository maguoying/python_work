#coding=gbk
file_name = 'guest_book.txt';
while(1):
    guest_book_name = input('Input your name:');
    if(guest_book_name == 'q'):
        break;
    print("You are welcome," + guest_book_name);
    with open(file_name, 'a') as fo:
        fo.write(guest_book_name + ' comes here!' + '\n');
