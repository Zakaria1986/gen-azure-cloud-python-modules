

## Dynamically do 'CRUD' to the Dictionary

    # Add new pizza into the pizza list
    
    # Add new property to each of the pizza 

    # Add toppings to the toppings of each pizza or some of the pizza's

## Make this more interactive by adding input for example, let users input the data in console and then added to pizza list
 
 # Check to see if input already exist in the list if not add
 
 # Choose from option which perform CRUD on i.e., add new pizza, add new toppings or add a new property to the pizza's


## Finally print out all the result based on customer option:
 
 # allow list of option from the menue i.e., Pizza's 
 
 # Based on the input show the properties of that Pizza
 
 # if they want to order the pizza calculate and show the total price and end the program. 


# ['Margarita','peperoni','fungi']
pizza_menu = [
                {'Margarita':{
                    'name' : 'Margarita',
                    'price': 5,
                    'size' : '8 inch',
                    'toppings': ['cheese','tomato','basil']
                    }
                },
                
                {'peperoni':{
                    'name' : 'Peperoni',
                    'price' : 6,
                    'size': '8',  
                    'toppings': ['cheese','tomato', 'salami']
                    }
                },
                {'fungi':{
                    'name' : 'Fungi' ,
                    'price' : 7,
                    'size' : '8 inch',
                    'toppings': ['cheese','tomato','mushroom']
                    }
                }
            
         ]

hawaiian_properties =  {
         'name' : "Hawaiian",
          'price': 10,
         'size' : '8 inch',
         }
hawaiian_properties.update({'toppings': [ 'Ham', 'pineapple', 'mozzarella cheese', 'tomato sauce']})
hawaiian =  {'hawaiian': hawaiian_properties }
pizza_menu.append(hawaiian)
 
 #  add discription seperatly to the list:   "description": "Ham and pineapple with tomato sauce and mozzarella."

# being lazing: don't wanna change the names below
pizza = pizza_menu
margherita_properties = len(pizza)
print('total number of pizza in the Dictionary', margherita_properties) 
#print(pizza)

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

def get_user_selected_pizza(input, pizza_list):
    ## Use it if statement to match the names
    output = ''
    
    for piz in pizza_list:
        for key, val in piz.items():  
            toppins = ''
            if val['name'].lower() == input:
                output += f'Pizza name: {val['name']}, \nSize: {val['size']},\nPrice: £{val['price']},\nToppings:'
                for index, topins in enumerate(val['toppings']):
                    toppins += f'\n\t{index} = {topins} ' 
        output+=toppins
    return output; 
        
       
# check for correct entry or otherwise ask for the correct entry
while True:
    select_option_prompt = input(f'\nPlease select the pizza from the following list:"{pizza_name}"?')
    input_entry_to_lower = select_option_prompt.lower()
    choice = input_entry_to_lower.strip()
    
    if choice == 'exit':
        break  
    elif not choice.isalpha() or choice not in pizza_name_list:
        print("\n\n\Invalid input. Please enter a valid option from the menu. '\n\n\t\tOr enter \'exit\' to exit the console'")   
  
    else:
        print('\nYou have entered {}'.format(get_user_selected_pizza(choice, pizza_menu)))
        
        print('\n\t\tEnter \'exit\' to exit the console')
    
    
       
     
    
        
        
        
    

    # if input_op  == "Fungi":
    #     print('correct getting your informaiton')
    # else:
    #     print("Incorrect input, select one from our menu list:")


## write all the else if statements logics here to only vew whats been selected

            
            

       
           


 





  

