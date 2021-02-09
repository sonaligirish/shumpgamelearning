shopping_list={}
shopping_list=dict()
shopping_list["soap"]=8
print(shopping_list)
shopping_list["computer"]=3
print(shopping_list)
shopping_list["phone"]=3
print(shopping_list)
shopping_list["headphones"]=1
print(shopping_list)
shopping_list["bookes"]=9
print(shopping_list)
shopping_list["mouse"]=3
print(shopping_list)
shopping_list["pouch"]=1
print(shopping_list)
shopping_list["earphones"]=3
print(shopping_list)
shopping_list["pen"]=5
print(shopping_list)
shopping_list["TV"]=5
print(shopping_list)
earphones=input("enter the number of earphones")
earphones =int(earphones)
shopping_list["earphones"]=earphones
print (shopping_list)
del(shopping_list["TV"])
print(shopping_list)