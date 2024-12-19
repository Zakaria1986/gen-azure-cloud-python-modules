from dictionary_list import pizza_menu as pizza
from my_classes import PizzaMenuPrompt
from my_classes import UserInputAndValidations
from my_classes import AddNewItemToTheList


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
    
# prompting users to select optons and edit, update and delete item from the lists            
while True:
    user_option = input('Select an option from the list:  "Add new item enter: 0.", "To view menu enter: 1.": ')
    user_choice = user_option.strip()
    
    if user_choice == 'exit': # Exit if user decides to exit the code
        break
    
    elif not user_choice.isdigit() or int(user_choice) > 1: # if the user input is not an intiger or out of select range ask users to select option per instruction
        print("\n\nInvalid input. Please enter a valid option provided.\n\n\t\tOr enter 'exit' to exit the console")
    
    else: # else is where the magic h1appens, checks the users request and gets the data
        if int(user_choice) == 0:
            item_keys=[]
            item_key_str = ''
            userInput_list = []
            userInput_toppings = []
            while True:
                    for index in pizza:
                        for keys, val in index.items():
                            for key, val in val.items():
                                if key not in item_keys:
                                    item_keys.append(key)
                                    item_key_str+=f'"{key}", '
                    print(item_keys)
                    print(item_key_str)
                    
                    userinput = UserInputAndValidations() # instentiating user input and validation class
            
                    for key in item_keys:     
                        if key == 'toppings':
                            while True:
                                choice = userinput.user_in_put(key) # passing on the arugment to offer user menu choices
                                if choice =='exit':
                                    break 
                            # appending
                                userInput_toppings.append(choice) 
                                        
                        else:
                            choice = userinput.user_in_put(key) # passing on the arugment to offer user menu choices
                            userInput_list.append(choice); 
                
                    print(userInput_list)
                    print(userInput_toppings)
                    
                    # Add class, adding new pizza item to the list
                    addToListClass = AddNewItemToTheList(userInput_list[0],userInput_list[1],userInput_list[2], userInput_toppings, pizza)
                    addToListClass.add_new_pizza()

                    if choice =='exit':
                        break 
               
        # User choice 1 to view the menu  
        elif int(user_choice) == 1:
            
            # Get the length of pizza list 
            PizzaMenu = PizzaMenuPrompt(pizza)
            totalPizza = PizzaMenu.get_total_num_pizz() 
            
            while True: # based on users input an infinate loop starts and based on the input code either exits or fetches. 
               
                userinput = UserInputAndValidations() # instentiating user input and validation class
                choice = userinput.user_in_put(pizza_name) # passing on the arugment to offer user menu choices
               
                if choice == 'exit':
                    break
                
                elif not choice.isalpha() or choice not in pizza_name_list:
                    print("\n\nInvalid input. Please enter a valid option from the menu.\n\n\t\tOr enter 'exit' to exit the console")
                else:
                    # Class being called here to get the user request fromt he dictionary
                    pizzaChoice = PizzaMenuPrompt('',choice,pizza)
                    user_choice =pizzaChoice.get_user_selected_pizza()
                    print('\nYou have entered {}'.format(user_choice))
                    print('\nTotal number of pizzas available: ', totalPizza)
                    print('\n\t\tEnter \'exit\' to exit the console')