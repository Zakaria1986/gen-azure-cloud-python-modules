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
dinner_invites_to_deceased.insert(1,new_guest_name)
print('\n We have one less guest in the list now:',dinner_invites_to_deceased); 


# Inviting 3 more guests, now using promt to add guest names

add_guest_to_invite_list = input('\nIf you wish to invite more guest, please entern guest name: ')
print('\n Guest name you have entered: '+add_guest_to_invite_list)

# Add to the list .append()

dinner_invites_to_deceased.append(add_guest_to_invite_list)
print('\nYour guest name has been added to the invite list: ', dinner_invites_to_deceased)