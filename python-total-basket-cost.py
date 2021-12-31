"""
    This project creates a program that calculates the total
    cost of a customers shopping basket, including shipping.

    - If a customer spends over $100, they get free shipping
    - If a customer spends < $100, the shipping cost is $1.20 per kg of the baskets weight


"""

shipping_cost_per_kg = 1.20
customer_basket_cost = 101
customer_basket_weight = 44

if(customer_basket_cost >= 100):
  print('Free shipping!')
else:
  shipping_cost = customer_basket_weight * shipping_cost_per_kg
  customer_basket_cost = shipping_cost + customer_basket_cost

print("Total basket cost including shipping is " + str(customer_basket_cost))

