# realization: I was getting multiple errors that didn't make sense to me (like indentation when I knew it was right), 
# it turns out the problem was that I didn't declare the attributes or include pass in the constructor. Once I did that everything worked
# I had to do "from Computer import Computer" to get the class to work, I tried "import Computer" first, but then it took in a module
# forgot to include "self" in methids
# "self.inventory[itemID].description" instead of "self.inventory[itemID]", which just lead to the object location

class Computer:

    # Attributes
    description: str = ""
    processor_type: str = ""
    hard_drive_capacity: int = 0
    memory: int = 0
    operating_system: str = ""
    year_made: int = 0
    price: int = 0

    # Constructor
    def __init__(self, description: str, processor_type: str, hard_drive_capacity: int, memory: int, operating_system: str, year_made: int, price: int) -> None:
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price
        pass



    # update price

    # update OS


# def main():
#     newComputer: Computer = Computer("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64, "macOS Big Sur", 2013, 1500)
#     print(newComputer.description)


# if __name__ == "__main__": 
#     main()
