name = str(input('Please enter your name: '))
number = int(input('Please enter a number: '))

word = ''

if number % 3 == 0 and number % 5 == 0:
    word = 'FizzBuzz'
elif number % 3 == 0:
    word = 'Fizz'
elif number % 5 == 0:
    word = 'Buzz'    
else:
    word = 'is neither a fizzy or a buzzy '

print('Wassup ' + name + '!')
print('The number ' + str(number) + '...')
print('is a ' + word + ' number!')