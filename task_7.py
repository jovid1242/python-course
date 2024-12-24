class Product:
    def __init__(self, name, price, discount):
        self.name = name
        self.price = price
        self.discount = discount

    @property
    def price_with_discount(self): 
        return self.price * (1 - self.discount / 100)

    @property
    def price(self): 
        return self._price

    @price.setter
    def price(self, value): 
        if value < 0:
            raise ValueError("Цена не может быть отрицательной.")
        self._price = value

    @property
    def discount(self): 
        return self._discount

    @discount.setter
    def discount(self, value): 
        if not (0 <= value <= 100):
            raise ValueError("Скидка должна быть в пределах от 0% до 100%.")
        self._discount = value

  

product = Product("Айфон", 1500, 30) 
print(product.price_with_discount) 
 
 
try:
    product.price = -100  
except ValueError as e:
    print(e)

try:
    product.discount = 150   
except ValueError as e:
    print(e)
