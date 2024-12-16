#1 

for ask in range (1,6):
    user_in_put = input('Please enter  your test result to measure overall grade: ')
    user_in_put = int(user_in_put)
    if user_in_put < 40:
       print('You just need little more improvement.')
    elif user_in_put >= 40 and user_in_put < 60:
        print('You passed.')
    elif user_in_put >= 60 and user_in_put < 70:
        print('Your passing mark is merit, you did really good.')
    elif user_in_put >= 70 and user_in_put <=100:
        print('Excellent work, you did great. Your passing mark is distinction')
    else:
        print('Only enter numbers between 1 to 100')


