name = input('What\'s your name?\n')

print('Hello, '+name+'.')
answer = input('Do you understand Python while loops? Type "Yes" or "No". ')

while answer == "No":
    print('The while loop is used to repeat a section of code an unknown number of times until a specific condition is met.')

    answer = input('Do you understand Python while loops? Type "Yes" or "No". ')
print("Great! Let's move on " + name + "!")    