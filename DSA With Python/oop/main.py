import csv


class Item:
    # class attribute
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: int, quantity: int = 0):
        # Run Validations on the received arguements
        assert price >= 0, f"Price {price} must be greater then 0"
        assert quantity >= 0, f"Quantity {quantity} must be greater then 0"

        # Assigning arguments to self object
        self.__name = name
        self.__price = price
        self.__quantity = quantity

        # Tracking the record of all the objects in a class
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    # Using Class Attribute
    def discount_price(self):
        # hm isko Item.pay_rate se bhi access kr skty hyn lekin agr ksi item ka pay_rate changr krna hoa to wo impossible hoga qk phir wo hr dfa class attribue ki value hi use krega  , lekin is trh se us object ka attribute use hoga jsko hm apne program me manually modify kr skty hyn
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get("name"),
                price=float(item.get("price")),
                quantity=int(item.get("quantity"))
            )

    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity})"


Item.instantiate_from_csv()
print(Item.all)
