class Computer:

 # What attributes will it need?
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int


    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self,
                    des: str,
                    pro_typ: str,
                    hdd_cap: int,
                    mem: int,
                    os: str,
                    year: int,
                    amt: int):
        
        self.description = des
        self.processor_typ = pro_typ
        self.hard_drive_capacity = hdd_cap
        self.memory = mem
        self.operating_system = os
        self.year_made = year
        self.price = amt
     # You'll remove this when you fill out your constructor

    # What methods will you need?
   