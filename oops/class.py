class ShoppingCart(object):

    def __init__(self):
        self.total = 0
        self.items = {}

    def add_items(self,item_name,qty,price):
        self.total += (qty*price)
        self.items.update({item_name:qty})
    
    def remove_item(self,item_name,qty,price):
        self.total -= (qty*price)
        if qty > self.items[item_name] :
            del self.items[item_name]
        self.items[item_name] -= qty
    
    def checkout(self,cash_paid):
        balance = 0 
        if cash_paid < self.total :
            return "You paid {} but cart amount is {}".format(cash_paid,self.total)
        else :
            balance = cash_paid - self.total
            return "Exchange amount {}". format(balance)

#Driver code 
cart = ShoppingCart()
cart.add_items('A', 10, 500)
cart.add_items('B',5,20)
cart.remove_item('B',1,20)
cart_res = cart.checkout(600)

print('Total cart amount :',cart.total)
print('Cart Items:', cart.items)
print(cart_res)