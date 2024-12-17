from dictionary_list import pizza_menu
from functions import get_total_num_pizz
from functions import get_user_selected_pizza
from functions import add_new_pizza

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
totalNum = get_total_num_pizz(pizza)   
           
while True:
    user_option = input('Select an option from the list:  "Add new item enter: 0.", "To view menu enter: 1."')
    user_choice = user_option.strip()
    
    if user_choice == 'exit':
        break
    elif not user_choice.isdigit() or int(user_choice) > 1:
        print("\n\nInvalid input. Please enter a valid option provided.\n\n\t\tOr enter 'exit' to exit the console")
    else:
        if int(user_choice) == 0:
            print('You selected option 2')
        elif int(user_choice) == 1:
            while True:
                select_option_prompt = input(f'\nPlease select the pizza from the following list: "{pizza_name}"? ')
                input_entry_to_lower = select_option_prompt.lower()
                choice = input_entry_to_lower.strip()
                
                if choice == 'exit':
                    break
                
                elif not choice.isalpha() or choice not in pizza_name_list:
                    print("\n\nInvalid input. Please enter a valid option from the menu.\n\n\t\tOr enter 'exit' to exit the console")
                else:
                    print('\nYou have entered {}'.format(get_user_selected_pizza(choice, pizza_menu)))
                    print('\nTotal number of pizzas available: ', totalNum)
                    print('\n\t\tEnter \'exit\' to exit the console')