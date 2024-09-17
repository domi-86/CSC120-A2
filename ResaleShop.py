from Computer import Computer
from typing import Dict, Optional

class ResaleShop:

    # What attributes will it need?

    # inventory consisting of computer objects (how to have them listed but not change index number if removing a computer from the list?)
    # computer "ID" / index

    # How will you set up your constructor?
    def __init__(self):
        self.itemID: int = 0
        self.inventory : Dict[int, Computer] = {}
        pass # You'll remove this when you fill out your constructor

    # What methods will you need?

    # buying a computer

    """
Takes in a Dict containing all the information about a computer,
adds it to the inventory, returns the assigned item_id
"""


    def buy(self, computer: Computer):
        self.itemID += 1
        #print("Trying to add", computer.description, "to inventory.")
        self.inventory[self.itemID] = computer
        #print("Success!")
        return self.itemID

    # selling a computer

    #def sell(computer: Computer):

    """
    Takes in an item_id, removes the associated computer if it is the inventory, 
    prints error message otherwise
    """
    def sell(self, itemID: int):
        if itemID in self.inventory:
            del self.inventory[itemID]
            print("Item", itemID, "sold!")
        else: 
            print("Item", itemID, "not found. Please select another item to sell.")


    #updating price
    def updatePrice(self, itemID: int, newPrice: float):
        if itemID in self.inventory:
            self.inventory[itemID].price = newPrice
        else:
            print("Item", itemID, "not found. Cannot update price.")


    #refurbish a computer (update price based on age, optional change OS)
    def refurbish(self, itemID: int, newOS: Optional[str] = None):
        if itemID in self.inventory:
            computer = self.inventory[itemID] # locate the computer
            if int(computer.year_made) < 2000:
                computer.price = 0 # too old to sell, donation only
            elif int(computer.year_made) < 2012:
                computer.price = 250 # heavily-discounted price on machines 10+ years old
            elif int(computer.year_made) < 2018:
                computer.price = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer.price = 1000 # recent stuff

            if newOS is not None:
                computer.operating_system = newOS # update details after installing new OS
        else:
            print("Item", itemID, "not found. Please select another item to refurbish.")



    def printInventory(self):
         #If the inventory is not empty
        if self.inventory:
            # For each item
            for itemID in self.inventory:
                # Print its details
                print(f'Item ID: {itemID} : {self.inventory[itemID].description}')
        else:
            print("No inventory to display.")


