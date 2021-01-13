class Hotel:
    def __init__(self,name, place,room_price,lux_room_price, room_mid ={"room1":"free", "room2":"free", "room3": "free"},rooms_lux = {"room1":"free", "room2":"free", "room3": "free"}):
        self.name = name
        self.place = place
        self.room_mid = room_mid
        self.room_price = room_price
        self.rooms_lux = rooms_lux
        self.lux_room_price = lux_room_price
    def Hotel_presentation(self):
        return  F'{self.name} Hotel is located in  fabulous nature of {self.place}. The hotel has two types of rooms middle {self.room_price} and lux {self.lux_room_price} .'
    def booking(self, room_type, room):
        if room_type == "mid":
            if self.room_mid[room] == "free":
                self.room_mid[room] = "bussy"
                print("room_mid: ", self.room_mid)
            else:
                print("The mid room you entered is already bussy, choose another please.")
        if room_type == "lux":
            if self.rooms_lux[room] == "free":
                self.rooms_lux[room] = "bussy"
                print("rooms_lux: ", self.rooms_lux)
            else:
                print("The lux room you entered is already bussy, choose another please.")
    def available_room_check(self,room_type):
        if room_type == "mid":
            b = list(self.room_mid.values())
            free_mid = b.count('free') 
            print(F"The number of free mid rooms is {free_mid}.")
            return free_mid
        if room_type == "lux":
            c = list(self.rooms_lux.values())
            free_lux = c.count('free')
            print(F"The number of free lux rooms is {free_lux}.")
            return free_lux
    def discount(self,room_type,d):
        if room_type == "mid":
            self.room_price -= self.room_price * d /100
            return  self.room_price
        elif room_type == "lux":
            self.lux_room_price -= self.lux_room_price * d /100
            return self.lux_room_price
class Taxi:
	def __init__(self,car_name,car_types,price_for_tour):
		self.car_name = car_name
		self.car_types = car_types
		self.price_for_tour = price_for_tour
	def taxi_presentation(self):
		return F" For trips we provide {self.car_types} mid-sized {self.car_name} which price is {self.price_for_tour}."
	def discount_taxi(self,disc):
		self.price_for_tour -=self.price_for_tour * disc/100
		return "Price after discount",self.price_for_tour
class Tour(Hotel,Taxi):
	def __init__(self,tour_name,name, place,room_price,lux_room_price,car_name,car_types,price_for_tour,price_lux = 0,price_mid =0,room_mid ={"room1":"free", "room2":"free", "room3": "free"},rooms_lux = {"room1":"free", "room2":"free", "room3": "free"}):
		Hotel.__init__(self,name, place,room_price,lux_room_price, room_mid ={"room1":"free", "room2":"free", "room3": "free"},rooms_lux = {"room1":"free", "room2":"free", "room3": "free"})
		Taxi.__init__(self,car_name,car_types,price_for_tour)
		self.tour_name = tour_name
		self.price_lux =self.lux_room_price + self.price_for_tour
		self.price_mid = self.room_price + self.price_for_tour
	def Tour_presentation(self):
		text = "Thank you for choosing us!" + " " + self.Hotel_presentation() + " " + self.taxi_presentation() + F" We  provide two options:\n  1. for one person lux room and taxi will cost {self.price_lux} \n  2. mid room and taxi will cost {self.price_mid} "
		print(text)

tour =Tour("Dilijan_jan","Diligence ", "Dilijan", 10000, 25000,"pickup","Honda Ridgeline",13000)
tour.Tour_presentation()
    
    
        

