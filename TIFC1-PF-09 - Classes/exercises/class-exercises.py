from dictionary_list import pizza_menu
from my_classes import PizzaMenuPrompt

hawaiian_properties =  {
         'name' : "Hawaiian",
          'price': 10,
         'size' : '8 inch',
         }
hawaiian_properties.update({'toppings': [ 'Ham', 'pineapple', 'mozzarella cheese', 'tomato sauce']})
hawaiian =  {'hawaiian': hawaiian_properties }
pizza_menu.append(hawaiian)
 
# add discription seperatly to the list:   "description": "Ham and pineapple with tomato sauce and mozzarella."

pizza = pizza_menu

# String to inlcude inside the input
pizza_name = ''

# Use it if statement to match the names
pizza_name_list = list()
for piz in pizza:
    output = ''
    toppins = ''
    for key, val in piz.items():  
        # output += f'Pizza name: {val['name']},', 'Size {},'.format(val['size']), 'Price: £',val['price'], ',Toppings: {}.'.format(toppins)
        output += f'Pizza name: {val['name']}, \nSize: {val['size']},\nPrice: £{val['price']},\nToppings:'
        pizza_name += f' {val['name']},'
        
        list_name = val['name'].strip().lower()
        pizza_name_list.append(list_name)
        
        for index, topins in enumerate(val['toppings']):
            toppins += f'\n\t{index} = {topins} '  
    output+=toppins
    # print(output)
    
## Functions saved as variable for later use

# Get the length of pizza list 
PizzaMenu = PizzaMenuPrompt(pizza)

totalPizza = PizzaMenu.get_total_num_pizz()   

# prompting users to select optons and edit, update and delete item from the lists            
while True:
    user_option = input('Select an option from the list:  "Add new item enter: 0.", "To view menu enter: 1."')
    user_choice = user_option.strip()
    
    if user_choice == 'exit': # Exit if user decides to exit the code
        break
    elif not user_choice.isdigit() or int(user_choice) > 1: # if the user input is not an intiger or out of select range ask users to select option per instruction
        print("\n\nInvalid input. Please enter a valid option provided.\n\n\t\tOr enter 'exit' to exit the console")
    else: # else is where the magic h1appens, checks the users request and gets the data
        if int(user_choice) == 0:
            print('You selected option 2')
        elif int(user_choice) == 1:
            while True: # based on users input an infinate loop starts and based on the input code either exits or fetches. 
                select_option_prompt = input(f'\nPlease select the pizza from the following list: "{pizza_name}"? ')
                input_entry_to_lower = select_option_prompt.lower()
                choice = input_entry_to_lower.strip()
                
                if choice == 'exit':
                    break
                
                elif not choice.isalpha() or choice not in pizza_name_list:
                    print("\n\nInvalid input. Please enter a valid option from the menu.\n\n\t\tOr enter 'exit' to exit the console")
                else:
                    pizzaChoice = PizzaMenuPrompt('',choice,pizza_menu)
                    user_choice =pizzaChoice.get_user_selected_pizza()
                    print('\nYou have entered {}'.format(user_choice))
                    print('\nTotal number of pizzas available: ', totalPizza)
                    print('\n\t\tEnter \'exit\' to exit the console')