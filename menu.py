#define the menu of restuarant 
menu = {
    'Pizza':400,
    'Pasta':250,
    'Burger':120,
    'Salad':180,
    'Cold Coffee':165,
    'Peri Peri Fries':110,
    'Sandwich':80,
}
#Greet
print("Welcome to PYTHON CAFE")
print("Pizza: Rs400\nPasta: Rs250\nBurger: Rs120\nSalad: Rs180\nCold Coffee: Rs165\nPeri Peri Fries: Rs110\nSandwich: Rs80")

order_total=0

item_1 = input("Enter the name of item you want to  order = ")
if item_1 in menu:
    order_total = order_total+menu[item_1]
    print(f"Your item {item_1} has been added to your order")
    
else:
    print(f"Ordered item {item_1} is not available yet")
    
another_order = input("Do you want to add something else  in your order? (Yes/No) ")
if another_order == "Yes":
    item_2 = input("Enter the name of the second item = ")
    if item_2 in menu:
        order_total = order_total + menu[item_2]
        print(f"Item {item_2} has been added to your order") 
    else:
        print(f"Ordered item {item_2} is not available yet!")
        
print(f"The total amount to pay is Rs{order_total} ")
