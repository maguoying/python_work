#coding=gbk
from collections import OrderedDict
from random import randint

class Die():
    def __init__(self,sides = 6):
        self.sides = sides;
        
    def roll_die(self):
        print(randint(1, self.sides));
print('====================�ָ���==================');
print('��6�������10��');
die_01 = Die();
i = 0;
while(i < 10):
    die_01.roll_die();
    i += 1;
print('====================�ָ���==================');
print('��10�������10��');
die_02 = Die(10);
j = 0;
while(j < 10):
    die_02.roll_die();
    j += 1;
print('====================�ָ���==================');
print('��20�������10��');
die_03 = Die(20);
k = 0;
while(k < 10):
    die_03.roll_die();
    k += 1;
