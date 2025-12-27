
def get_discounted_price(disc1, disc2, disc3, ticket_price, loyalty_card="no"):
    """
    Apply discount based on ticket price and loyalty card status.
    disc1, disc2, disc3 are percentage discounts.
    """
    if loyalty_card.lower() == "yes" or loyalty_card.upper() == "yes":
        if 70 < ticket_price <= 100:
            discount = disc1
        elif 100 < ticket_price <= 200:
            discount = disc2
        else:
            discount = disc3

        new_price = ticket_price - (ticket_price * discount / 100)
        print(f"Discount Applied: {discount}% | New Price: {new_price:.2f}")
        return new_price
    else:
        print("No discount applied. You will need a loyalty card.")
        return ticket_price

# Example usage:
get_discounted_price(10, 20, 30, 120, loyalty_card="YES")



