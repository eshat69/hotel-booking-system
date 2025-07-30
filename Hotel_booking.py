class hotel_booking :
    def __init__(self):
        self.room = {
            #single room
            101: {"status": "available", "type": "Single", "price": 3000},
            201: {"status": "available", "type": "Single", "price": 3000},
            301: {"status": "available", "type": "Single", "price": 2500},
            103: {"status": "available", "type": "Single", "price": 3000},
            203: {"status": "available", "type": "Single", "price": 3000},
            303: {"status": "available", "type": "Single", "price": 2500},

            #double room
            102: {"status": "available", "type": "Double", "price": 5000},
            202: {"status": "available", "type": "Double", "price": 5000},
            302: {"status": "available", "type": "Double", "price": 4500},
            104: {"status": "available", "type": "Double", "price": 5000},
            204: {"status": "available", "type": "Double", "price": 5000},
            304: {"status": "available", "type": "Double", "price": 4500},
        }
        self.booking = {}

    def display_abbreviations(self):
        print("\n Welcome to your home away from home ")
        print("1. view available rooms")
        print("2. book a room")
        print("3. cancel booking")
        print("4. view all booking")
        print("5. view room types and prices")
        print("6. exit")

    def view_available(self):
        print("\n view available room")
        for room,status in self.room.items():
            if status == "available" :
                print(f"room {room} : {status} ")

    def book_room(self):
        name=input("\n Enter your name :")
        room_no = int(input("Enter your room no to book :"))
        if room_no in self.room and self.room[room_no] == "available" :
            self.room[room_no] = "booked"
            self.booking[room_no] = name
            print(f"room {room_no} is succesfully booked by {name}")
        else :
            print(f"room {room_no} is not available or already booked by {name}")
        print("-" * 50)

    def cancel_room(self):
        room_no = int(input("\n enter the room no to cancal "))
        if room_no in self.booking :
            name = self.booking.pop(room_no)
            self.room[room_no] = "available"
            print(f"booking for room {room_no} by {name} has been canceled")
        else :
            print(f"no booking found for room {room_no} ")

    def view_room_details(self):
        print("\nRoom Details:")
        print("-" * 40)
        for room_no, info in self.room.items():
            print(f"Room {room_no}: Type = {info['type']}, Price = {info['price']} BDT, Status = {info['status']}")
        print("-" * 50)

    def view_all_booking(self):
        if not self.booking :
            print("\n No boonking found ")
        else :
            print("\n cancel booking")
            for room , name in self.booking.items() :
                print(f"room {room} booked by {name}")

    def rooms(self):
        while True :
            self.display_abbreviations()
            choice = input("enter ur choice between 1 to 6 ")
            if choice == "1" :
                self.view_available()
            elif choice == "2" :
                self.book_room()
            elif choice == "3" :
                self.cancel_room()
            elif choice == "4" :
                self.view_all_booking()
            elif choice == "5":
                self.view_room_details()
            elif choice == "6" :
                print(" Thank uou ! :)")
            else :
                print("invalid choice , Please try again ")
if __name__ == "__main__":
    app = hotel_booking()
    app.rooms()