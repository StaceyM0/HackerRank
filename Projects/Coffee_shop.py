#We are going to build a coffee shop using Pythong Programming concepts. Let's build a robot Barista

print("Hello, welcome to my coffee shop!!")

name = input("What is your name?\n") #Now you will type your name

print("Hello " + name + ", thank you so much for coming in today.\n\n")

# love this dialog so much'



menu = "Black Coffee, Espresso, Latte, Cappucino"

print(name + ", what would you like from our menu today? Here is what we are serving.\n" + menu)

order = input()

price = 8

quantity = input("How many coffees would you like?\n")

total = price * int(quantity) 

print("Thank you. Your total is: $" + str (total))

print("Sounds good " + name + ", we'll have your " + quantity + " "+ order + " ready for you shortly.")
