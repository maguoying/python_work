pizzas = ['New York','chicago','Pan','Thick','Cracker'];
message = 'The first three items in the list are:';
print(message);
print(pizzas[:3]);
print('Three items from the middle of the list are:');
print(pizzas[1:4]);
print('The last three items in the list are:');
print(pizzas[-3:]);
friend_pizzas = [];
pizzas.append('ice');
friend_pizzas.append('naiyou');
print('My favorite pizzas are:');
for pizza in pizzas:
	print(pizza);
print("My friend's favorite pizzas are:");
for friend_pizza in friend_pizzas:
	print(friend_pizza);
print('=========================================================');
my_foods = ['pizza','falafel','carrot cake'];
for my_food in my_foods:
	print(my_food);
