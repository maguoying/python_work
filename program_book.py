#coding=gbk
file_name = 'program_book.txt';
while(True):
    name = input('Input your name:');
    if(name == 'q'):
        break;
    program_language = input('Input your program language:');
    with open(file_name,'a') as fo:
        fo.write(name + ' use ' + program_language + ' program language.\n');
        
