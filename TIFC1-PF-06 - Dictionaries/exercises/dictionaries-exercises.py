

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

pizza_name = ''
for piz in pizza:
   # print('\n',piz)
   
    output = ''
    toppins = ''
    for key, val in piz.items():  
        # output += f'Pizza name: {val['name']},', 'Size {},'.format(val['size']), 'Price: £',val['price'], ',Toppings: {}.'.format(toppins)
        output += f'Pizza name: {val['name']}, \nSize: {val['size']},\nPrice: £{val['price']},\nToppings:'
        pizza_name += f' {val['name']},'
        
        for index, topins in enumerate(val['toppings']):
            toppins += f'\n\t{index} = {topins} '  
    output+=toppins
    print(output)
    
   
# print('\n',pizza_name)
# promt for pizza options
select_option_prompt = input(f'\nPlease select the pizza from the following list:{pizza_name}?...')

## write all the else if statements logics here to only vew whats been selected

            
            

       
           


 





  

