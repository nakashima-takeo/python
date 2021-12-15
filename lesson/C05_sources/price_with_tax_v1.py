def price_with_tax(price):
    """Returns the price with 10% tax added"""
    full_price = price + 0.1 * price
    return full_price

# Item prices without tax
price_pen = 5.0
price_eraser = 3.0

# Display prices including tax
print('Price with tax pen:', price_with_tax(price_pen))
print('Price with tax eraser:', price_with_tax(price_eraser))
