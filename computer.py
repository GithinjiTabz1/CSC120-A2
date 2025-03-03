class Computer:
    """
    A class representing a computer with various specifications.
    Stores details such as processor type, memory, OS, and price.
    """

    # Attributes
    description: str  # Brief description of the computer
    processor_type: str  # Type of processor used
    hard_drive_capacity: int  # Storage capacity in GB
    memory: int  # RAM size in GB
    operating_system: str  # Installed OS
    year_made: int  # Year the computer was manufactured
    price: int  # Price of the computer

    # Constructor
    def __init__(self,
                 des: str,
                 pro_typ: str,
                 hdd_cap: int,
                 mem: int,
                 os: str,
                 year: int,
                 amt: int):
        """
        Initializes a Computer object with given specifications.
        """
        self.description = des
        self.processor_type = pro_typ
        self.hard_drive_capacity = hdd_cap
        self.memory = mem
        self.operating_system = os
        self.year_made = year
        self.price = amt
