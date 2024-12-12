import pyautogui as alert
import pygetwindow as gw
import tkinter as tk
from tkinter import messagebox


# List of favorite music artists
names = ["Adele", "Ed Sheeran", "Beyoncé", "Drake", "Taylor Swift"]

print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])

# 2. each message should be personalized with the music artist’s name.
print('\n')
print("Hello",names[0], "you're music is amazing!")
print("Hello",names[1], "you're music is amazing!")
print("Hello",names[2], "you're music is amazing!")
print("Hello",names[3], "you're music is amazing!")
print("Hello",names[4], "you're music is amazing!")

### 3.  favorite book or movie.
favorite_movies = [
    "The Shawshank Redemption",
    "1994",
    "Frank Darabont, based on the novella “Rita Hayworth and Shawshank Redemption” by Stephen King",
    "Drama, Crime",
    "142 minutes", 
    "The narrative of hope, friendship, and redemption resonates deeply with audiences. Andy Dufresne’s journey from despair to triumph is both inspiring and emotionally powerful." 
]

print(f' “\nMy favorite book is {favorite_movies[0]} directed by {favorite_movies[2]} in the year {favorite_movies[1]}' +
      f' based on the genre {favorite_movies[3]} and the length of the movie is {favorite_movies[4]}' +
      f'\n I like that the movie promotes,  {favorite_movies[5]}\n') 


### 4. If you could invite anyone, living or deceased, to dinner, who would you invite?
dinner_invites_to_deceased = [
    "Albert Einstein", 
    "Maya Angelou", 
    "Leonardo da Vinci" 
]

print(
   "People I would invite to dinner: {}".format(dinner_invites_to_deceased[0]), 
   "\nPeople I would invite to dinner: {}".format(dinner_invites_to_deceased[1]),  
   "\nPeople I would invite to dinner: {}".format(dinner_invites_to_deceased[2]),    
)

#Guest 'Maya Angelou cannot make it for the dinner, remove from the list and add a new
dinner_cancelation = dinner_invites_to_deceased.pop(1)
print('\nGuest name',dinner_cancelation,'cannot make it to the dinner. Please invite the next favourte person!'); 

# Print one less guest
print('\n We have one less guest in the list now:',dinner_invites_to_deceased); 

# Inviting next favourite person to the dinner using method insert(1)
new_guest_name = 'Nelson Mandela'
dinner_invites_to_deceased.insert(0,new_guest_name)
middle_index = len(dinner_invites_to_deceased) // 2
dinner_invites_to_deceased.insert(middle_index ,'Name seating in the middle')
print('\n We have one less guest in the list now:',dinner_invites_to_deceased); 

# Found bigger table message
print('\nFound a bigger dinner table, Invite more please')
# def show_alert():
#     root = tk.Tk()
#     root.withdraw()  # Hide the main window
#     messagebox.showinfo("Alert", "Found a bigger dinner table, Invite more please!")
#     root.destroy()
    
# # Call the function to show the alert
# show_alert()

# Inviting 3 more guests, now using promt to add guest names: input() 
add_guest_to_invite_list = input('\nIf you wish to invite more guest, please entern guest name: ')
print('\n Guest name you have entered: '+add_guest_to_invite_list)

# Add to the list .append()
if len(add_guest_to_invite_list) > 0:
    dinner_invites_to_deceased.append(add_guest_to_invite_list)
    
print('\nYour guest name has been added to the invite list: ', dinner_invites_to_deceased)

for name in dinner_invites_to_deceased:
 print("\nPeople I would invite to dinner: {}".format(name))
 
 
# Can only invite 2 people for dinner now
print('\nOpp! I can only invite 2 people for dinner now.')

total_num_of_guest = len(dinner_invites_to_deceased)
print('\nTotal number of guest:', total_num_of_guest)

# popping out the name from the list
for name in dinner_invites_to_deceased:
   if len(dinner_invites_to_deceased) > 2:  
       name_popped = dinner_invites_to_deceased.pop(dinner_invites_to_deceased.index(name))
       print('\nHi, i\'m really sorry, you are not be invited to the dinner:', name_popped)

# still invited
for name in dinner_invites_to_deceased:
    print('\nHi, are still invited:', name) 


for name in dinner_invites_to_deceased:
     # Deleting the last two
    del dinner_invites_to_deceased[dinner_invites_to_deceased.index(name)]
    

# Empty list
print('\nHi, Empty Array:', dinner_invites_to_deceased.clear())
    
    
### 5. Think of at least five places in the world you’d like to visit. Follow the steps to build your program:     
top_five_places = ["Tokyo", "Paris", "New York", "Sydney", "Rio de Janeiro"]
print("\nTop five place for holiday destination",top_five_places); 

# Sorting list in alphabetical order
top_five_places_in_alphabetical_order = sorted(top_five_places) 
print('\nTop five place for holiday destination in alphabedical order: ',top_five_places_in_alphabetical_order)

top_five_places_in_alphabetical_order = sorted(top_five_places_in_alphabetical_order, reverse=True) 
print('\nTop five place for holiday destination in alphabedical order: but reversed: ',top_five_places_in_alphabetical_order)

# Reversing it back into its orginal order
top_five_places_in_alphabetical_order = top_five_places_in_alphabetical_order[::-1];  
print('\nTop five place for holiday destination in alphabedical order in its orginal order: ',top_five_places_in_alphabetical_order)

