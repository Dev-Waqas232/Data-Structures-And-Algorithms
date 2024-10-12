class Item:
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


item1 = Item("Phone", -1, 15)
print(item1.calculate_total_price())
