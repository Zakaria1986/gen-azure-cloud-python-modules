

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
for piz in pizza:
   # print('\n',piz)
    for key, val in piz.items():
        print(f'Pizza name: {key},', 'Size {},'.format(val['size']), 'Price: £',val['price'], ',Toopings {}.'.format(val['toppings']),)

# keys = pizza.keys()
# values = pizza.values()

# print('Keys', keys)

# for key, val in pizza.items():
#     if key == str('Margarita'):
#         print('Pizza name: {}'.format( val['name']))
    

