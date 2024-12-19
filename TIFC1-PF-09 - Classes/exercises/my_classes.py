
# Classes


class PizzaMenuPrompt:
    def __init__(self, piz_list ='', input ='', pizza_list=''):
        
        self.piz_list = piz_list
        self.input = input
        self.pizza_list = pizza_list
        
    # Get the length of pizza list 
    def get_total_num_pizz(self):
        self.total_item = len(self.piz_list)
        return self.total_item

    # Get value by users selection
    
    def get_user_selected_pizza(self):
        ## Use it if statement to match the names
        self.output = ''
        
        for self.piz in self.pizza_list:
            for key, self.val in self.piz.items():  
                self.toppins = ''
                if self.val['name'].lower() == self.input:
                    self.output += f'Pizza name: {self.val['name']}, \nSize: {self.val['size']},\nPrice: £{self.val['price']},\nToppings:'
                    for self.index, self.topins in enumerate(self.val['toppings']):
                        self.toppins += f'\n\t{self.index} = {self.topins} ' 
            self.output+=self.toppins
        return self.output;  



# Add a new pizza class
class AddNewItemToTheList:
    def __init__(self, name, price, size, toppings, pizza):
        self.name = name
        self.price = price
        self.size = size
        self.toppings = toppings
        self.pizza = pizza
        
        
    def add_new_pizza(self):
        
        self.addnNewPizza =  {
        'name' : self.name.title(),
        'price': float(self.price),
        'size' : f'{self.size} inch',
        'toppings':  self.toppings
        }
        print(self.addnNewPizza)
        addPizza =  {self.name: self.addnNewPizza}
        self.pizza.append(addPizza)
        print(len(self.pizza))


class UserInputAndValidations:

    def user_in_put(self, pizza_name):
        self.pizza_name = pizza_name
        select_option_prompt = input(f'\nPlease select the pizza from the following list: "{pizza_name}"? ')
        input_entry_to_lower = select_option_prompt.lower()
        choice = input_entry_to_lower.strip()
        return choice


