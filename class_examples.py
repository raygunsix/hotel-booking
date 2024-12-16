# import Abstract Base Class module methods
from abc import ABC, abstractmethod
import pandas

df = pandas.read_csv("hotels.csv", dtype={"id": str})


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """Book a hotel by changing its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """Check if the hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False
        
    # Examples

    # Class method
    # applies to all instances
    #
    # >>> import pandas
    # >>> df = pandas.read_csv("hotels.csv", dtype={"id": str})
    # >>> hotel1.get_hotel_count(df)
    # 3
    # >>> hotel2.get_hotel_count(df)
    # 3
    @classmethod
    def get_hotel_count(cls, data):
        return len(data)

    # "Magic" method
    # override default behaviour
    #
    # >>> hotel1 = Hotel(hotel_id="188")
    # >>> hotel2 = Hotel(hotel_id="188")
    # >>> hotel1 == hotel2
    # True
    def __eq__(self, other):
        if self.hotel_id == other.hotel_id:
            return True
        else:
            return False

# Create abstract ("base" ) class  
# Abstract classes cannot be instantiated, only used for defining structure    
class Ticket(ABC):

    # Require child classes to define a generate method
    @abstractmethod
    def generate(self):
        pass


class ReservationTicket(Ticket):
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are you booking data:
        Name: {self.customer_name}
        Hotel name: {self.hotel.name}
        """
        return content

    # Examples

    # Property
    # behaves like a variable
    #
    # >>> ticket = ReservationTicket(customer_name="bob ", hotel_object=hotel1)
    # >>> ticket.the_customer_name
    # 'Bob'
    @property
    def the_customer_name(self):
        name = self.customer_name.strip()
        name = name.title()
        return name

    # Static method
    # "Utility" or helper functionality
    #
    # >>> ReservationTicket.convert(10)
    # 12.0
    @staticmethod
    def convert(amount):
        return amount * 1.2

class DigitalTicket(Ticket):

    # Required by abstract class Ticket
    def generate(self):
        pass