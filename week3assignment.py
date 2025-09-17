def calculate_discount(price, discount_percent):

    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price


# Main program

price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Call the function
final_price = calculate_discount(price, discount_percent)

# Display result
if discount_percent >= 20:
    print(f"Final price after {discount_percent}% discount: {final_price}")
else:
    print(f"No discount applied. Price remains: {final_price}")
