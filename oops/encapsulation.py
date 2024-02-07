class Product : 

    def __init__(self):
        self.__maxprice = 900
        self.minprice = 500

    def sell(self):
        print('Selling price {} '.format(self.__maxprice))
        print('Min selling price {}'.format(self.minprice))
    
    def set_max_price(self,price):
        self.__maxprice = price

    def set_min_price(self,price):
        self.minprice = price


#driver code
product =  Product()
product.sell()

#change price directly
product.__maxprice = 1000
product.minprice = 100
product.sell()

#change price using setter function 
product.set_max_price(1000)
product.sell()
