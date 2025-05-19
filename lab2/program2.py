#now we are going to learn about methods

def main():
    item = input("What item do you wish to buy?")
    price = input("What is the dollar cost of one of these items?")
    amount = input("How many of these would you like to buy?")

    #call method calculate_total_price
    total_price = calculate_total_price(amount, price)

    #call print_summary method
    print_summary(item,amount,price,total_price)

    #1. why does line 9 have total_price = and line 12 not have something like that?
    #2. what is the stuff in the brackets?
    #see answers at bottom

def calculate_total_price(amount,price):
    return int(amount) * float(price)

#takes item, amount, price and total_price as inputs
#and prints a string summarizing that information
def print_summary(item,amount,price,total_price):
    print("you have purchased ",amount," items at a rate of ",price," each for the total cost of ",total_price," dollars.")


main()


#answers:
#
#1
#calculate_total_price RETURNS something - the thing that is returned is put inside total_price
#print_summary prints something but does not return anything
#
#2
#the stuff in the brackets is parameters - they are PASSED to the method definition
#and used inside the method to do something
#this lets the methods be used with different inputs

