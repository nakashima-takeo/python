def price_with_tax(price):
    """Returns the price 
    with 5% tax added if less or equal to 4.0
    with 10% tax if larger than 4.0
    """
    if price <= 4.0:
        return price + 0.05 * price
    else:
        return price + 0.1 * price
    
# Item prices without tax
price_pen = 5.0
price_eraser = 3.0

# Display prices including tax
print('Price with tax pen:', price_with_tax(price_pen))
print('Price with tax eraser:', price_with_tax(price_eraser))