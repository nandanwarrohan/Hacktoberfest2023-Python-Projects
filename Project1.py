# INHERITANCE IN OPPS ==>>
"""
   Type of inheritance :
         1. Single Inheritance.
         2. Multi-Level Inheritance.
         3. Hierarchical Inheritance.
         4. multi Inheritance.
         5. Hybrid Inheritance.
         6. Cyclic Inheritance.
"""

class vehicle:
    def general_usage(self):
        print("general use : Transportation")


class car(vehicle):
    def __init__(self):
        print("I am a car")
        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):
        print("specification use : commute to work , vacation with family\n")


def specific_usage():
    print("Specific use : road trip, racing")


class motorcycle(vehicle):
    def __init__(self):
        print("\nI am a motor cycle")
        self.wheel = 2
        self.has_roof = True


Tata = car()
Tata.general_usage()
Tata.specific_usage()

tesla = car()
tesla.general_usage()
tesla.specific_usage()

maruti_suzuki = motorcycle()
maruti_suzuki.general_usage()
specific_usage()
