

#takes name, age and height as inputs
#prints these, adds one to the age and prints that as future age
def main():

    #this is how you get input from the user
    name = input("Please enter your name.")                 #user should enter text in quotes
    age = input("Please enter your age in years.")          #user should enter a whole number
    height = input("Please enter your height in meters.")   #user should enter a decimal number
                                                            #later, we'll learn about how to enforce this

    #this is how you print something
    print("Your name is ",name,". Your age is ",age,"years and your height is ",height,"m.")

    future_age = int(age) + 1                               #we the the int() so program knows age is an integer
    print("In one year you will be ",future_age)

main()

#your turn - write a program that...
# asks the user for
# what item they want to buy,
# how many of it they want to buy
# and how much one of that item costs
# then calculates the total cost
# and prints all the information

#hint: its going to be similar to the program above in terms of structure