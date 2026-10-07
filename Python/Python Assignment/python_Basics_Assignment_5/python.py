class ShoppingCart:

    # Part A: Constructor
    def __init__(self, customer_name, items=None):
        self.customer_name = customer_name

        # If no items are provided, use an empty list
        if items is None:
            self.items = []
        else:
            self.items = items

    # Part B: 1. Add Item
    def add_item(self, price):
        if isinstance(price, (int, float)) and price > 0:
            self.items.append(price)
            print(f"{price} added to the cart.")
        else:
            print("Price must be a positive number.")

    # Part B: 2. Remove Item
    def remove_item(self, price):
        if price in self.items:
            self.items.remove(price)
            print(f"{price} removed from the cart.")
        else:
            print(f"{price} is not found in the cart.")

    # Part B: 3. Calculate Total
    def calculate_total(self):
        total = 0

        for price in self.items:
            total += price

        return total

    # Part B: 4. Apply Discount
    def apply_discount(self):
        total = self.calculate_total()

        if total >= 3000:
            discount = total * 0.10
            final_amount = total - discount
        else:
            final_amount = total

        return final_amount

    # Part C: 1. Display Cart
    def display_cart(self):
        total = self.calculate_total()
        final_amount = self.apply_discount()

        print("\n========== Shopping Cart ==========")
        print(f"Customer Name : {self.customer_name}")
        print(f"Items         : {self.items}")
        print(f"Number of Items: {len(self.items)}")
        print(f"Total Amount  : {total:.2f}")
        print(f"Final Amount  : {final_amount:.2f}")
        print("===================================")

    # Part C: 2. Clear Cart
    def clear_cart(self):
        self.items.clear()
        print(f"{self.customer_name}'s cart has been cleared.")

    # Part D: Operator Overloading (+)
    def __add__(self, other):
        combined_name = f"{self.customer_name} & {other.customer_name}"
        combined_items = self.items + other.items

        return ShoppingCart(combined_name, combined_items)


# Create first ShoppingCart object
cart1 = ShoppingCart("Alice")

# Add items
cart1.add_item(1000)
cart1.add_item(1500)
cart1.add_item(1200)

# Remove an item
cart1.remove_item(1500)

# Display first cart
cart1.display_cart()


# Create second ShoppingCart object
cart2 = ShoppingCart("Bob")

# Add items
cart2.add_item(800)
cart2.add_item(2500)
cart2.add_item(1000)

# Remove an item
cart2.remove_item(800)

# Display second cart
cart2.display_cart()


# Combine two carts using + operator
combined_cart = cart1 + cart2

# Display combined cart
print("\n========== Combined Cart ==========")
combined_cart.display_cart()