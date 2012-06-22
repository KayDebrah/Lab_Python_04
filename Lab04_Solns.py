#Question 1
print "1a\n"
groceries=['bananas','strawberries','apples','bread']
groceries.insert(len(groceries)+1,'champagnes')
print groceries


print "1b\n"
groceries.remove('bread')
print groceries
print "1c\n"
grocery_sort={'A':'Apples','C':'Coconut','B':'Bananas'}
grocery_sort=grocery_sort.items()
grocery_sort.sort()

for i in grocery_sort:
    print i

print '.............End of Question 1...................'
min_exp={}

#Question 2
#a
print "2a:\n"

print "The best Data-Structure is the dictionary because it is able eto assign related data"



#b
print "2b:\n"
grocerylist={'Apple':"7.3",'Bananas':5.5,'Bread':1.0,'Carrots':10.0,'Champagne':20.90,'Strawberries':32.6}
print grocerylist

for item in grocerylist:
    print item
#c
print "2c:\n"
grocerylist['Strawberries']=63.43
print grocerylist

#d
print "2d:\n"


print '.............End of Question 2...................'


#Question 3

#a
print "3a:\n"
print "The best data Strucure for this solution is the list"


#b
print "3b:\n"
in_stock={"1":"Fufu","2":"Jollof"}

#c
print "3c:\n"
always_in_stock=("1: Fufu","2: Jollof")
print always_in_stock

#d
print "3d:\n"
for item in always_in_stock:
    print item


#Q4
mylist=[]
min_exp={}
price=float(raw_input("Enter Prices:"))
itemname=raw_input("Enter Item Name:")
newprice=float(raw_input("Enter New Min Price: "))

def binary_insert(new_float,mylist):
    #new_float=price
    mylist.append(new_float)
    print mylist
    return



def min_cost(grocery_list,item_price_list_dict):
    
    min_exp[grocery_list]=item_price_list_dict
    print min_exp
    return

binary_insert(price,mylist)
min_cost(itemname,newprice)



    
#print mylist
    
