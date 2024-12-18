
# Classes



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

class AddNewItemToTheList:
    def __init__(self, name, price, size, toppings, pizza_menu):
        def add_new_pizza(name, price, size, topppings, pizza_menu):
            hawaiian_properties =  {
                'name' : name,
                'price': price,
                'size' : size,
                }
            hawaiian_properties.update({'toppings': [topppings]})
            add_pizza =  {name: hawaiian_properties }
            pizza_menu.append(add_pizza)

