shopping_list = []

def add_to_list(item):
    shopping_list.append(item)
    print('{} has been added. You now have {} items on your shopping list...'.format(shopping_list[-1], len(shopping_list)))

def show_help():
    print('What item would you like to add to your shopping list?')
    print('''
    If you need help, type "Help". 
    If you would like to see what is on your list, type "List".
    If you are done, type "Done".
    ''')

def print_list():
    print('=====Shopping List=====')
    for item in shopping_list:
        print('*', item)
    print('=======================')

show_help()
while True: 
    new_item = input('> ').title()

    if new_item == 'Done':
        print_list()
        break
    elif new_item == 'List':
        print_list()
        continue
    elif new_item == 'Help':
        show_help()
        continue

    add_to_list(new_item)
