prices = {"apple": 0.50, "bread": 2.50, "milk": 3.00, "eggs": 4.00}
cart = {"apple": 6, "bread": 1, "milk": 2}

def cart_total(cart, prices):
    total = 0
    for key, quantity in cart.items():
        if key in prices:
            total += (quantity * prices[key])

    return total

def apply_discount(prices, item, percent_off):
    new_prices = prices.copy()
    if item in new_prices:
        new_prices[item] = new_prices[item] * (1-(percent_off/100))

    return new_prices

def receipt(cart, prices):
    receipt_list = []
    for key, quantity in cart.items():
        if key in prices:
            receipt_list.append(
                f"{key}: {quantity} x ${prices[key]:.2f} = ${(quantity*prices[key]):.2f}"
                )

    return receipt_list

print(receipt(cart, prices))