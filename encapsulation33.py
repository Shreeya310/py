class COMP:
    def __init__(self):
        self.__MaxPrice= 999
    def sell(self):
        print("OUR SELLING PRICE={}".format(self.__MaxPrice))
    def setMaxPrice(self,price):
        self.__MaxPrice=price
c=COMP()
c.sell()
c.__MaxPrice=7890
c.sell()      
c.setMaxPrice(7890)
c.sell()


