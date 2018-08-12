import print_models
names = ['magy','mayh','mazh'];
print_models.print_model(names);

print('=============================');
from print_models import print_model as mn
mn(names);

print('=============================');
from print_models import print_model as mn
mn(names);

print('=============================');
import print_models as pm
pm.print_model(names);

print('=============================');
from print_models import *
print_models.print_model(names);
