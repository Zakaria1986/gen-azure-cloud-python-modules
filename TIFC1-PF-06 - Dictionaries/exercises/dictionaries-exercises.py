from dictionary_list import pizza_menu
from functions import get_total_num_pizz
from functions import get_user_selected_pizza

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
pizza_name_list = list();
for piz in pizza:
   # print('\n',piz)
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
     
# print('\n',pizza_name)
# promt for pizza options

print('\n',pizza_name_list)

## Functions saved as variable for later use

# Get the length of pizza list 
totalNum = get_total_num_pizz(pizza)
       
# check for correct entry or otherwise ask for the correct entry
while True:
    select_option_prompt = input(f'\nPlease select the pizza from the following list:"{pizza_name}"?')
    input_entry_to_lower = select_option_prompt.lower()
    choice = input_entry_to_lower.strip()
    
    if choice == 'exit':
        break  
    elif not choice.isalpha() or choice not in pizza_name_list:
        print("\n\nInvalid input. Please enter a valid option from the menu. '\n\n\t\tOr enter \'exit\' to exit the console'")   
  
    else:
        print('\nYou have entered {}'.format(get_user_selected_pizza(choice, pizza_menu)))
        print('\nTotal number of pizza avaiable: ',totalNum)
        print('\n\t\tEnter \'exit\' to exit the console')
    



            
            

       
           


 





  

