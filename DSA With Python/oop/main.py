class Item:
    # class attribute
    pay_rate = 0.8

    def __init__(self, name: str, price: int, quantity: int = 0):
        # Run Validations on the received arguements
        assert price >= 0, f"Price {price} must be greater then 0"
        assert quantity >= 0, f"Quantity {quantity} must be greater then 0"

        # Assigning arguments to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    # Using Class Attribute
    def discount_price(self):
        # hm isko Item.pay_rate se bhi access kr skty hyn lekin agr ksi item ka pay_rate changr krna hoa to wo impossible hoga qk phir wo hr dfa class attribue ki value hi use krega  , lekin is trh se us object ka attribute use hoga jsko hm apne program me manually modify kr skty hyn
        self.price = self.price * self.pay_rate


item1 = Item("Phone", 1000, 15)
item1.pay_rate = 0.7  # yha pr pay_rate ko modify kia he, agr upr function me self. ki bijae Item. use kia hota to yeh changings reflect na hotyn or wo 0.8 hi use krta as a value
item1.discount_price()
print(item1.price)
