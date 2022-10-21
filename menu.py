menuDict = {
    "Python Pie": 10.50,
    "Variable Veggie Platter": 10.99,
    "Tuple Tapas": 17.99,

    "String Beans": 2.99,
    "Boolean Beets": 2.99,
    "Elif Eggplant": 2.99,

    "Charcolate Cake": 7.99,
    "Int Ice Cream": 3.99,
    "Set Pastry Selection": 6.99
}
mealDict = {}


#EXITS THE PROGRAM
def exit_function():
    print("Goodbye!")


#ALLOWS USERS TO GIVE RESTAURANT FEEDBACK
def feedback_function():
    feedback = input("How can we improve GitBash Restaurant for you? ")
    print("\nThanks for your feedback!")
    decisionf = input("Would you like to Exit or Restart? ").capitalize() 

    if decisionf == "Exit":
        exit_function()
    elif decisionf == "Restart":
        intro_function()
    else:
        print("\nWe cannot understand you")
        print("Let's try this again\n")
        feedback_function()


#SHOWS USER THE RESTAURANT MENU AND PROMTS THEM TO ADD DISHES TO MEAL
def menu_function():
    print("On today's menu we have:")
    for x,y in menuDict.items():
        print(x,y)
    
    print("\n")
    meal = input("What would you like to eat? ")
    
    if meal in menuDict.keys():
        print(meal,"has been added to your order!")
        mealDict[meal] = menuDict[meal]
    else:
        print("We seem to be all out of", meal)
        meal = ""

    def menu_options(meal):
        print("\n")
        print("To add another dish to your meal, type the item name")
        print("To view your meal and pay, type 'Basket'") 
        print("To dine elsewhere, type 'Exit'\n")

        decisionm = input("What will it be? ")

        if decisionm == "Exit":
            exit_function()
        elif decisionm == "Basket":
            basket_function()
        else:
            if decisionm in menuDict.keys():
                print(decisionm,"has been added to your order!")
                mealDict[decisionm] = menuDict[decisionm]
                menu_options(meal)
            else:
                print("We seem to be all out of", decisionm)
                menu_options(meal)
    
    menu_options(meal)
    

#SHOWS USER THE CONTENTS AND PRICE OF THEIR BASKET
def basket_function():
    if len(mealDict.keys()) == 0:
        print("Your basket is empty!")
        print("To add some meals to it, type 'Menu'")
        print("To let us know how we can improve, type 'Feedback'")
        print("To dine elsewhere, type 'Exit'\n")

        decisionb = input("What will it be? ").capitalize()
        print("\n")

        if decisionb == "Menu":
            menu_function()
        elif decisionb == "Feedback":
            feedback_function()
        elif decisionb == "Exit":
            exit_function()
        else:
            print("\nWe cannot understand you")
            print("Let's try this again\n")
            basket_function()
    
    else:
        print("\nYour meal basket contains:")
        price = 0.0
        for x,y in mealDict.items():
            print(x,y)
            price += y
        print("Your total price is:", price)
        decisionb2 = input("Would you like to Pay or Exit? ")

        if decisionb2 == "Exit":
            exit_function()
        elif decisionb2 == "Pay":
            print("\nThank you for your order!")
            exit_function()
        else:
            print("\nWe cannot understand you")
            print("Let's try this again\n")
            basket_function()


#HAPPENS UPON STARTING THE PROGRAM
def intro_function():
    print("\nWelcome to GitBash Restaurant!")
    name = input("What should we call you? ").capitalize()

    print("You look hungry",name,", let's see what we can do about that!\n")
    print("To view everything GB Restaurant has to offer, type 'Menu'")
    print("To view your meal and pay, type 'Basket'")
    print("To let us know how we can improve, type 'Feedback'")
    print("To dine elsewhere, type 'Exit'\n")

    decision = input("What will it be? ").capitalize()
    print("\n")

    if decision == "Exit":
        exit_function()
    elif decision == "Feedback":
        feedback_function()
    elif decision == "Menu":
        menu_function()
    elif decision == "Basket":
        basket_function()
    else:
        print("We cannot understand you",name)
        print("Let's try this again")
        intro_function()


#PROGRAM BEGINS WITH THE BELOW
intro_function()