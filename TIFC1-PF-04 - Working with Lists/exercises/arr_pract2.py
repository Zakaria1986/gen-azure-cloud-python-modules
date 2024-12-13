import random
# Exercise 4: Working with Lists

favorite_pizzas = ["Margherita", "Pepperoni", "BBQ Chicken"]

# 1.
# looking through with the index for loop
for i in range(len(favorite_pizzas)):
    print('I like {} Pizza'.format(favorite_pizzas[i]))
 
 #Add a line at the end of your program, The output should consist of three or more lines about the kinds of pizza you like  
i_love_pizza_string = 'A sentence to expressing my deepest desire for pizza.'
i_love_pizza_string2 = 'Combining both the coding the eating pizza,'
i_love_pizza_string3 = 'I confirm i really Enjoy automating expressing my love for pizza by coding my pizza expressions!'
print ('\n{} {} {}'.format(i_love_pizza_string, i_love_pizza_string2,i_love_pizza_string3))   

# 2.
# List of animals with common characteristics
animals = ["Dolphin", "Elephant", "Chimpanzee"]
#
for pet in animals:
    print(f'\n{pet.title()} would make a great pet.')
    
# what these animals have in common
print('They are all very highly intelligent and social animals.')

# 3.  

# Use a for loop to print the numbers from 1 to 20, inclusive.
num = 20
for i in range(num):
    print('\n1st Num example:',i+1); 

# example 2 of printing numbers one 2 20
for num1 in range(1,21):
    print('\nNum',num1,'\n'); 
    
# 4.  
    # Generating list of number from 1 to 100 randomly
#arr_num_list = [random.randint(1,100) for i in range(1,100)]
arr_num_list = [ ]
for num in (random.randint(1,100) for i in range(1,100)):
    arr_num_list.append(num)
      
# Printig the list    
print(arr_num_list)

# Getting the min and max
min = min(arr_num_list)
max = max(arr_num_list)
print('\nmin num:',min,'Max num:', max)

# 5.
    # 3 from 3 to 30. Use a for loop to print the numbers in your list
arr_three_times_list = []
for num in range(3,100,3):
    #arr_three_times_list.append(num*3)
    if num <= 30:
        arr_three_times_list.append(num)
    
# Printing out the 3 increments   
print('\n',arr_three_times_list)

# 5.

