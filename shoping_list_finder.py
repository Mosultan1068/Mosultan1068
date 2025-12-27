'''
Lap exercise for finding items in the shoping list
'''
from selectors import SelectSelector

#define the items in the list
item1='Milk'
item2='Bananas'
item3='Apple'
item4='Orange'
item5='Bread'

print(''' The Shopping list items are
        ''',
        '1-',item1,''' 
        '''
        '2-',item2,''' 
        '''
        '3-',item3,'''
        '''
        '4-',item4,'''
        '''
        '5-',item5)

milk_available=True
bananas_available=False
apple_available=True
orange_available=True
bread_available=True

#strip() and capitalize() , removes any initial or trailing spces and 1st letter capital
#it ensures the input is cleaned and initial letter is capital
search_item=input("Enter item to search:").strip().capitalize()

#need to ensure the item entered is in the list
#checked using the not in the list
#if the item is not in the list - exit
if search_item not in("Milk","Bananas","Apple","Orange","Bread"):
   print(search_item,"is not a valid shopping item, it does not exits in our list - Exiting")
   print("Good bye")
   exit(1)

#check if the item is part of the shopping list
#using or and a match using if then
if search_item=="Milk" and milk_available:
    print("Great, search item matches the shooping list and" , search_item ," is available")
else:
    print(search_item, "is not available - sorry")
    print(" Thank you for using this program")