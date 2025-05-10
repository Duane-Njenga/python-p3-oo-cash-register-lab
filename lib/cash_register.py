#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.last_transaction = 0 

  def add_item(self, title, price, quantity = 1):
    self.total += price * quantity
    self.title = title
    self.last_transaction = price * quantity
    for _ in range(quantity):
      self.items.append(self.title)
    return self.items


  
  def apply_discount(self):
    self.total -= (self.total*self.discount/100)
    if self.discount == 0:
      print("There is no discount to apply.")
    else:
      print(f"After the discount, the total comes to ${int(self.total)}.")
  

  def void_last_transaction(self):
    self.total -= self.last_transaction

    


test = CashRegister(20).apply_discount()
print(test)