#Define the function
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = original_price - (original_price * discount_percent / 100)
        return discounted_price
    else:
        return original_price    

#Get user input
original_price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

#Call the function
final_price = calculate_discount(original_price, discount_percent)

#Print the result
if discount_percent >= 20:
    print("Discount applied.")
    print("The final price is:", final_price)
else:
    print("No discount applied.")
    print("The original price is:", final_price)