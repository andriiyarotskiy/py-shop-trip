import json
from app.shop import Shop
from app.customer import Customer
from app.car import Car


def shop_trip() -> None:
    with open("app/config.json") as f:
        config = json.load(f)

        fuel_price = config["FUEL_PRICE"]

        shops = [Shop(**shop) for shop in config["shops"]]
        customers = [
            Customer(
                name=c["name"],
                product_cart=c["product_cart"],
                location=c["location"],
                money=c["money"],
                car=Car(**c["car"])
            )
            for c in config["customers"]
        ]

        for customer in customers:
            print(f"{customer.name} has {customer.money} dollars")
            for shop in shops:
                cost = customer.trip_cost(shop, fuel_price)

                print(f"{customer.name}'s trip "
                      f"to the {shop.name} costs {cost}")

            cheapest_shop, cheapest_cost = min(
                [(shop, customer.trip_cost(shop, fuel_price))
                 for shop in shops],
                key=lambda x: x[1]
            )

            if customer.money >= cheapest_cost:
                print(f"{customer.name} rides to {cheapest_shop.name}\n")
                customer.location = cheapest_shop.location.copy()
                cheapest_shop.print_receipt(
                    customer.name,
                    customer.product_cart
                )

                # Return home
                print(f"{customer.name} rides home")
                c_customers = config["customers"]
                location = c_customers[customers.index(customer)]["location"]
                customer.location = location

                # Update money
                customer.money -= cheapest_cost
                customer.money = round(customer.money, 2)
                print(f"{customer.name} now has {customer.money} dollars")
                print()
            else:
                print(f"{customer.name} doesn't have enough money "
                      f"to make a purchase in any shop")
