#pizza project / list

# pizzas = ("4 cheeses", "veggie", "hawaiian", "calzone")

# def display_pizzas():
#     print("----- Pizzas (4): -----")
#     print('4 cheeses')
#     print('veggie')
#     print('hawaiian')
#     print('calzone')
    
# display_pizzas()

#define custom sort function (line 25)
# def custom_sort(e):
#     #return e #sort as default
#     return len(e) #sort based on length
    
#or this better option!

def display_pizzas(collection, n_first_element = -1): #second parameter is optional
    #sort the collection (default alphabetical)
    #collection.sort(reverse=True) #flip order of list
    #custom sorting
    # collection.sort(reserse=True, key=custom_sort)
    #allow function call to slice
    c = collection
    if not n_first_element == -1:
         c = collection[0:n_first_element]#slice to display only those elements
         
    nb_pizzas = len(c)
    
    if nb_pizzas == 0:
        print()
        print("No Pizzas")
        print()
        return
   
        
    print(f"----- Pizzas ({nb_pizzas}): -----")
    for i in c:
        print(i)
    print()
    print("first pizza : " + c[0])
    print( "last pizza : " + c[-1])
    print()
   
#add user pizza

def add_user_pizza(collection):
    p = input("Add your pizza: ")
    #if pizza_exists(p, collection): #check if user input exists
    #so you dont have to creation a fuction
    #use .lower or .upper to remov case sensitivity
    if p.lower() in collection: 
        print("Error: This pizza already exists")
    else:
     collection.append(p) #if it doesnt, add to list
    
#function if pizza already exists
#need new element (e). function tests that e is in collection
# def pizza_exists(e, collection):
#     for i in collection:
#         if e == i:
#             return True
#     return False
    

pizzas = ["4 cheeses", "veggie", "hawaiian", "calzone", "four seasons"]

empty = ()



 
add_user_pizza(pizzas)   
display_pizzas(empty, 3)





