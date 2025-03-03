from computer import Computer
from typing import Dict, Optional

class ResaleShop:
    """
    A class to manage a resale shop's computer inventory.
    Allows buying, selling, refurbishing, and updating prices.
    """

    # Attributes 
    inventory: list  # Stores the list of computers in inventory
    item_id: int  # Tracks the current item ID

    # Constructor
    def __init__(self, inv: list, item_ID: int):
        """
        Initializes the resale shop with an inventory and item ID counter.
        """
        self.inventory = inv
        self.item_id = item_ID

    # Methods
    def buy(self, computer: Computer):
        """
        Adds a computer to the inventory and returns its assigned item ID.
        """
        self.inventory.append(computer)
        return self.inventory.index(computer)
    
    def update_price(self, item_id: int, new_price: int):
        """
        Updates the price of a computer if it exists in the inventory.
        """
        if self.inventory[item_id] is not None:
            self.inventory[item_id]["price"] = new_price
        else:
            print("Item", item_id, "not found. Cannot update price.")

    def sell(self, item_id: int):
        """
        Removes a computer from inventory if it exists, indicating it has been sold.
        """
        if item_id in self.inventory:
            self.inventory.pop(item_id)
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")

    def print_inventory(self):
        """
        Displays all items in inventory with their item IDs and details.
        """
        if self.inventory:
            for item in self.inventory:
                print(f'Item ID: {self.inventory.index(item)} : {item}')
        else:
            print("No inventory to display.")

    def refurbish(self, item_id: int, new_os: Optional[str] = None):
        """
        Updates a computer's price based on its age and installs a new OS if provided.
        """
        if item_id in self.inventory:
            computer = self.inventory[item_id]

            if int(computer["year_made"]) < 2000:
                computer["price"] = 0  # Too old to sell, donation only
            elif int(computer["year_made"]) < 2012:
                computer["price"] = 250  # Heavily discounted price
            elif int(computer["year_made"]) < 2018:
                computer["price"] = 550  # Discounted price
            else:
                computer["price"] = 1000  # Recent stuff

            if new_os is not None:
                computer["operating_system"] = new_os  # Update OS if provided
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")
