# Main Program (Single User Input)
original_price = float(input("Enter the original price in dollars: $"))  # Get user input

# Lambda function to apply discount based on price range
apply_discount = lambda price: price * 0.90 if price > 100 else price * 0.95

# Non-parametric function for tax calculation
def calculate_tax(price):
    tax_rate = 0.07 if price > 100 else 0.05  # 7% tax for prices above $100, 5% otherwise
    tax_amount = price * tax_rate  # Calculate tax amount
    final_price = price + tax_amount  # Add tax to price
    return final_price, tax_amount

# Parametric function for final price adjustment
def final_price(price):
    discounted_price = apply_discount(price)  # Apply discount based on price range
    adjusted_price, tax_amount = calculate_tax(discounted_price)  # Apply tax
    return discounted_price, adjusted_price, tax_amount

# Perform all calculations
discounted, final_adjusted, tax_deducted = final_price(original_price)

# Display results
discount_applied = "10%" if original_price > 100 else "5%"  # Identify discount applied
print(f"\nOriginal Price: ${original_price:.2f}")
print(f"Discount Applied: {discount_applied}")
print(f"Price after discount: ${discounted:.2f}")
print(f"Tax deducted: ${tax_deducted:.2f}")
print(f"Final adjusted price after tax: ${final_adjusted:.2f}")
