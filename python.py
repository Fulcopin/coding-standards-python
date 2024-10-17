"""
Module to demonstrate a shopping cart with discounts, 
tax calculation, environmental fees, input validation, 
and error handling.
"""

class Itemz:
    """
    Represents an item in a shopping cart.
    """
    def __init__(self, name, price, qty, category):
        """
        Initializes Itemz with name, price, quantity, 
        category, and environmental fee.
        """
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Price must be a positive number.")
        if not isinstance(qty, int) or qty <= 0:
            raise ValueError("Quantity must be a positive integer.")
        if not isinstance(category, str):
            raise ValueError("Category must be a string.")

        self.name = name
        self.price = price
        self.qty = qty
        self.category = category
        self.env_fee = 5 if category == "electronics" else 0

    def get_total(self):
        """
        Calculates the total price for the item, 
        including environmental fee.
        """
        return (self.price * self.qty) + self.env_fee

    def __str__(self):  # Added a second public method
        """
        Returns a string representation of the item.
        """
        return (f"{self.name} - Price: ${self.price}, "
                f"Quantity: {self.qty}, Category: {self.category}")


class ShoppingCart:
    """
    Represents a shopping cart with items, discounts, and tax.
    """
    def __init__(self):
        """
        Initializes ShoppingCart with items list, tax rate, 
        discounts, and currency.
        """
        self.items = []
        self.tax_rate = 0.08
        self.member_discount = 0.05
        self.big_spender_discount = 10
        self.coupon_discount = 0.15
        self.currency = "USD"

    def add_item(self, item):
        """
        Adds an item to the shopping cart.
        """
        if not isinstance(item, Itemz):
            raise ValueError("Invalid item type. Must be an instance of Itemz.")
        self.items.append(item)

    def calculate_subtotal(self):
        """
        Calculates the subtotal of all items in the cart.
        """
        subtotal = 0
        for item in self.items:
            subtotal += item.get_total()
        return subtotal

    def apply_discounts(self, subtotal, is_member):
        """
        Applies member and big spender discounts to the subtotal.
        """
        if is_member == "yes":
            subtotal = subtotal - (subtotal * self.member_discount)
        if subtotal > 100:
            subtotal = subtotal - self.big_spender_discount
        return subtotal

    def calculate_total(self, is_member, has_coupon):
        """
        Calculates the total price after discounts and tax.
        """
        subtotal = self.calculate_subtotal()
        subtotal = self.apply_discounts(subtotal, is_member)
        total = subtotal + (subtotal * self.tax_rate)
        if has_coupon == "YES":
            total = total - (total * self.coupon_discount)
        return total

def main():
    """
    Main function to demonstrate shopping cart functionality.
    """
    cart = ShoppingCart()

    try:
        # Example with input validation and error handling
        item1 = Itemz("Apple", 1.5, 10, "fruit")
        item2 = Itemz("Banana", 0.5, 5, "fruit")
        item3 = Itemz("Laptop", 1000, 1, "electronics")
        cart.add_item(item1)
        cart.add_item(item2)
        cart.add_item(item3)
        is_member = True
        has_coupon = "YES"

        total = cart.calculate_total(is_member, has_coupon)

        if total < 0:
            print("Error in calculation!")
        else:
            print("The total price is: $" + str(total))

    except ValueError as e:
        print(f"Error: {e}")
        total = -1
    except TypeError as e:  
        print(f"Type error occurred: {e}")
        total = -1


if __name__ == "__main__":
    main()
