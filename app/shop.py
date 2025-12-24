from dataclasses import dataclass
import datetime


@dataclass
class Shop:
    name: str
    location: list[int]
    products: dict

    def cart_cost(self, cart: dict) -> float:
        total = 0
        for key, value in cart.items():
            total += value * self.products[key]
        return round(total, 2)

    def print_receipt(self, customer_name: str, cart: dict):
        current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {current_time}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")

        for product, quantity in cart.items():
            cost = quantity * self.products[product]
            cost = round(cost, 2)
            if isinstance(cost, float) and cost.is_integer():
                cost = int(cost)

            print(f"{quantity} {product}s for {cost} dollars")

        total = self.cart_cost(cart)
        if isinstance(total, float) and total.is_integer():
            total = int(total)

        print(f"Total cost is {total} dollars")
        print("See you again!\n")
