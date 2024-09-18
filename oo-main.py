from Computer import Computer
from ResaleShop import ResaleShop

def main():
    store = ResaleShop()
    computer1: Computer = Computer("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5",
                                   1024, 64, "macOS Big Sur", 2013, 1500)

    # Print a little banner
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)
    
    # Add it to the resale store's inventory
    print("Buying", computer1.description)
    print("Adding to inventory...")
    computer_id = store.buy(computer1)
    #buy(computer)
    print("Done.\n")
    
    # Make sure it worked by checking inventory
    print("Checking inventory...")
    store.printInventory()
    print("Done.\n")

    #Change the price
    print("Changing price...")
    store.updatePrice(1, 1000)
    print("Computer now $", computer1.price)
    
    # Now, let's refurbish it
    new_OS = "MacOS Monterey"
    print("Refurbishing Item ID:", computer_id, ", updating OS to", new_OS)
    print("Updating inventory...")
    store.refurbish(computer_id, new_OS)
    print("Done.\n")
    
    # Make sure it worked by checking inventory
    print("Checking inventory...")
    store.printInventory()
    print("Done.\n")
    
    # Now, let's sell it!
    print("Selling Item ID:", computer_id, "for $", computer1.price)
    store.sell(computer_id)

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    store.printInventory()
    print("Done.\n")

# Calls the main() function when this file is run
if __name__ == "__main__": main()

