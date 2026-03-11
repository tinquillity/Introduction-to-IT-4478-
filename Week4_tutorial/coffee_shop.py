print("Welcome to the Python Coffee Shop!")
customer_name = input("What is your name?")
print("Hello," +customer_name+ "! Let's order some coffee.\n")

price_coffee = 3.50
price_latte = 4.00
price_mocha = 5.00

print("Coffee: $" + str(price_coffee))
print("Latte: $" + str(price_latte))
print("Mocha: $" + str(price_mocha))

menu_items=["coffee", "latte", "mocha"]
print("Our menu:", menu_items)


# while loop: initial value, loop condition, update statement
flag = "y"
total = 0
while flag== "y":

    choice = input("what would you like to order? (coffee/latte/mocha):").lower()

    if choice == "coffee":
        cost=price_coffee
    elif choice == "latte":
        cost=price_latte
    elif choice == "mocha":
        cost=price_mocha
    else:
        print("Sorry, we dont have that.")
        cost = 0

                    
    quatity = int(input("How many cups?"))

    total_cost = cost*quatity

    total += total_cost

    flag = input("Do you want to order again (y/n):")

if quatity>1:
                  print("You get a discount of $1")
                  total -=1.00
else:
        print("Sorry, no discount for you")
        
student = input("Are you a student? (yes/no)").lower()
                
if student == "yes":
    total *=0.9

print("Your total is: $" +str(total))
print("Thanks," +customer_name +"!please come again")
