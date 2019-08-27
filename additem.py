#! Python3

# This file contains the initial list of commands, defined as functions
# TODO: CLI accessibility


# Adding an item
# call pydo add
print('Item to add to list: ')
item = input()

n = open('todo.txt','a+')
n.write('\n' + item)
n.close()

r = open('todo.txt','r')
print('Todo: ')
print(r.read())