
# Here resides all my functions

# Get the length of pizza list 
def get_total_num_pizz(piz_list):
    total_item = len(piz_list)
    return total_item

# Get value by users selection
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

# Add a new pizza function

def add_new_pizza(name, price, size, topppings, pizza_menu):
    hawaiian_properties =  {
        'name' : name,
        'price': price,
        'size' : size,
         }
    hawaiian_properties.update({'toppings': [topppings]})
    add_pizza =  {name: hawaiian_properties }
    pizza_menu.append(add_pizza)


# def add_new_pizza():
    

# Delete a property 


# Update a property



# Update toppings


'''
Data structure
- Structure of if statements 
- couple of line of code, read through and determine the outcome
- For loops: what they are for what they are used for 
- Couple of question about classes
- One of two questiona bout how to move a block of code to another file and keep it neet 
'''




