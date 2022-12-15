import os
import math
from IPython.display import clear_output

# Takes Input from user
def greeting():
    clear_output()
    print("\n\n*********************** Welcome to Coding Temple Store *****************************")
    print(' ')
    print('  Bathroom Products                                  Cleaning Supplies')
    print('    B1. Shampoo       4.99                             C1. Mops              6.99   ')
    print('    B2. Toothpaste    6.99                             C2. Bleach            2.99')
    print('    B3. Toothbrush    2.99                             C3. Brooms            10.99')
    print('    B4. Handsoap      1.99                             C4. Rubber Gloves     7.99')
    print(' ')
    print('  School Supplies                                    Groceries')
    print('    S1. Note book     3.99                             G1. Tomatoes          1.99')
    print('    S2. Pencils H2    2.99                             G2. Ribeye            18.99')
    print('    S3. Markers       6.99                             G3. OJ                6.99')
    print('    S4. Eraser        1.99                             G4. Milk              5.99')

    print('\n\n')
    user_start = input('Would you like start shopping with us ? "yes"-continue / "no"-quit.  -->  ').strip().lower()
    try:
        if user_start == 'y':
            user_input() 
        elif user_start == 'n':
            exit_program()
        else:
            print('Invalid option! \n\n')
            return greeting()
    except ValueError():
        print('That is not one of our options. Please try again')
        return greeting()

def display_list(**shopping_list):
    print("\n\n*********************** Welcome to Coding Temple Store *****************************")
    print(' ')
    print('  Bathroom Products                                  Cleaning Supplies')
    print('    B1. Shampoo       4.99                             C1. Mops              6.99   ')
    print('    B2. Toothpaste    6.99                             C2. Bleach            2.99')
    print('    B3. Toothbrush    2.99                             C3. Brooms            10.99')
    print('    B4. Handsoap      1.99                             C4. Rubber Gloves     7.99')
    print(' ')
    print('  School Supplies                                    Groceries')
    print('    S1. Note book     3.99                             G1. Tomatoes          1.99')
    print('    S2. Pencils H2    2.99                             G2. Ribeye            18.99')
    print('    S3. Markers       6.99                             G3. OJ                6.99')
    print('    S4. Eraser        1.99                             G4. Milk              5.99')

    continue_shopping(**shopping_list)

# User Input
def user_input(**shopping_list):
    print('\n\n\n')
    
    shopping_list_store = {
        'Shampoo' : 4.99,                                  
        'Toothpaste' : 6.99,   
        'Toothbrush' : 2.99,                     
        'Handsoap' : 1.99,                       
        'Mops' : 6.99,          
        'Bleach' : 2.99,           
        'Brooms' : 10.99,            
        'Rubber Gloves' : 7.99,    
        'Lamps' : 3.99,                                  
        'Tomatoes' : 1.99,
        'Pencils H2' : 2.99,                    
        'Ribeye' : 18.99,
        'Markers' : 6.99,                       
        'OJ' : 6.99,                
        'Eraser' : 1.99,        
        'Milk' : 5.99,              
    }

    item_equalizer = {
        'B1' : 'Shampoo',
        'B2' : 'Toothpaste',
        'B3' : 'Toothbrush',
        'B4' : 'Handsoap',
        'C1' : 'Mops',
        'C2' : 'Bleach',
        'C3' : 'Brooms',
        'C4' : 'Rubber Gloves',
        'K1' : 'Lamps',
        'K2' : 'Pencils H2',
        'K3' : 'Markers',
        'K4' : 'Eraser',
        'G1' : 'Tomatoes',
        'G2' : 'Ribeye',
        'G3' : 'OJ',
        'G4' : 'Milk',
        }


    shopping_list = {}
    
    flag = True 
    while flag:
        print('Please add items by their code # (eg. "B1")')
        print('What Item would you like to add to your cart ? ')
        print('You can also choose "s" - to see items in cart, "q" - to quit, "r" - to check out')
        item = input('---->   ')
     
        if item in item_equalizer.keys():
            x = item_equalizer[item]
            shopping_list[x] = shopping_list_store[x]
            print('\nThis is what you have added so far to your cart : \n', shopping_list)
        elif item == 's':
            clear_output()
            flag = False
            see_items(**shopping_list)
        elif item == 'r':
            clear_output()
            flag = False
            check_out(**shopping_list)
            
        elif item == 'q':
            clear_output()
            flag = False
            exit_program()
        else:
            print('Value non-existent')

def continue_shopping(**shopping_list):
    shopping_list_store = {
        'Shampoo' : 4.99,                                  
        'Toothpaste' : 6.99,   
        'Toothbrush' : 2.99,                     
        'Handsoap' : 1.99,                       
        'Mops' : 6.99,          
        'Bleach' : 2.99,           
        'Brooms' : 10.99,            
        'Rubber Gloves' : 7.99,    
        'Lamps' : 3.99,                                  
        'Tomatoes' : 1.99,
        'Pencils H2' : 2.99,                    
        'Ribeye' : 18.99,
        'Markers' : 6.99,                       
        'OJ' : 6.99,                
        'Eraser' : 1.99,        
        'Milk' : 5.99,              
    }

    item_equalizer = {
        'B1' : 'Shampoo',
        'B2' : 'Toothpaste',
        'B3' : 'Toothbrush',
        'B4' : 'Handsoap',
        'C1' : 'Mops',
        'C2' : 'Bleach',
        'C3' : 'Brooms',
        'C4' : 'Rubber Gloves',
        'K1' : 'Lamps',
        'K2' : 'Pencils H2',
        'K3' : 'Markers',
        'K4' : 'Eraser',
        'G1' : 'Tomatoes',
        'G2' : 'Ribeye',
        'G3' : 'OJ',
        'G4' : 'Milk',
        }
    
    flag = True 
    while flag:
        print('Please add items by their code # (eg. "B1")')
        print('What Item would you like to add to your cart ? ')
        print('You can also choose "s" - to see items in cart, "q" - to quit, "r" - to check out')
        print('\n')
        item = input('---->')
     
        if item in item_equalizer.keys():
            x = item_equalizer[item]
            shopping_list[x] = shopping_list_store[x]
            print(shopping_list)
            clear_output()
        elif item == 's':
            clear_output()
            see_items(**shopping_list)
        elif item == 'r':
            clear_output()
            check_out(**shopping_list)
        elif item == 'q':
            clear_output()
            flag = False
            exit_program()
        else:
            print('Value non-existent')



# User See Items
def see_items(**shopping_list):
    clear_output()
    print(shopping_list)
    print('\n\n')
    print('This is the current list of items in your shopping cart so far :')
    x = 1
    for y, z in shopping_list.items():
        print(x,'.', y, '\t\t',z)
        x += 1
    print('\n')
    print('Sub-Total : {:.2F}'.format(sum(shopping_list.values())))
    print('\n\n')
    print('Would you like to add or delete any items ? ("add" - to add items / "del" - to delete items) - "q" to quit / "r" to check out(register)')
    option = input('--> ')

    if option == 'del':
        delete_items(**shopping_list)
    
    if option == 'add':
        display_list(**shopping_list)

    if option == 'r':
        check_out(**shopping_list)

    if option == 'q':
        exit_program()




def delete_items(**shopping_list):
    print('\n')
    print('  Bathroom Products                                  Cleaning Supplies')
    print('    B1. Shampoo       4.99                             C1. Mops              6.99   ')
    print('    B2. Toothpaste    6.99                             C2. Bleach            2.99')
    print('    B3. Toothbrush    2.99                             C3. Brooms            10.99')
    print('    B4. Handsoap      1.99                             C4. Rubber Gloves     7.99')
    print(' ')
    print('  School Supplies                                    Groceries')
    print('    S1. Note book     3.99                             G1. Tomatoes          1.99')
    print('    S2. Pencils H2    2.99                             G2. Ribeye            18.99')
    print('    S3. Markers       6.99                             G3. OJ                6.99')
    print('    S4. Eraser        1.99                             G4. Milk              5.99')
    print('\n')
    print('These are the items currnetly in your cart :')
    print('\n')
    x = 1
    for y, z in shopping_list.items():
        print(x,'.', y, '\t\t',z)
        x += 1
    print('\n')
    delete = input('Please enter the item you would like to delete from your list (eg. Shampoo) :')
    del shopping_list[delete]
    option = input('Would you like to delete any more items ? --> "y" or "n" / "r" to register or "q" to quit ')    
    if option == 'y':
        delete_items(**shopping_list)
    if option == 'n':
        see_items(**shopping_list)

    if option == 'r':
        check_out(**shopping_list)

    if option == 'q':
        exit_program()

    


# Print all Items as a check out
def check_out(**shopping_list):
    print('\n\n')
    print('\n\n*************************************THANK YOU FOR SHOPPING WITH US *************************************************')
    x = 1
    for y, z in shopping_list.items():
        print(x,'.', y, '\t\t', z)
        x += 1
    print('Your total for today is :')
    print('TOTAL : {:.2F}'.format(sum(shopping_list.values())))
    exit_program()


# Exit Program Befor Shopping
def exit_program():
    clear_output()
    print('\n\nThank you for visiting us. We hope to see you soon!!!')

    print('\n\n\n')
    quit()
    # exit()


greeting()

print('\n\n\n\n')


   