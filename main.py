import pandas as pd

df = pd.read_csv("hotels.csv")

class Hotel:
    def __init__(self, id):
        self.id = id

    def available(self):
        pass

    def book(self):
        pass


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        pass

    def generate(self):
        pass


print(df)
id = input("Enter the id of the hotel: ")
hotel = Hotel(id)
if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(name, hotel)
    print(reservation_ticket.generate())
else:
    print("Hotel is not free.")