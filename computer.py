# realization: I was getting multiple errors that didn't make sense to me (like indentation when I knew it was right), 
# it turns out the problem was that I didn't declare the attributes or include pass in the constructor. Once I did that everything worked.









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


def main():
    newComputer: Computer = Computer("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64, "macOS Big Sur", 2013, 1500)
    print(newComputer.description)


if __name__ == "__main__": 
    main()
