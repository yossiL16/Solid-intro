

class Order:
    def __init__(self, items:list, total_price:float):
        self.items = items
        self.total_price  = total_price

class Print:
    @staticmethod
    def print_invoice(items, total_price):
        print(f"tour items: {items}. your total price: {total_price}.")

