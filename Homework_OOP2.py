# #1
class Person:
	def __init__(self,name, gender, height, weight):
		self.name = name
		self.gender = gender
		self.height = height
		self.weight = weight
	def optimal_weight(self):
		if self.gender == "male":
			op_weight = 56.2 + (self.height - 152.4) / 2.54 * 1.36
		elif self.gender == "female":
			op_weight = 53.1 + (self.height - 152.4) / 2.54 * 1.36 
		op_weight = round(op_weight,2)
		print (F"{self.name}'s weight:", self.weight,"optimal weight: ", op_weight, sep ="\n")
		a = op_weight - self.weight
		if a > 0:
			print(F"You need to gain {round(a,2)} kg.")
		elif a < 0:
			print(F"You need to lose {round(a,2)} kg.")
		elif a == 0:
			print("Your weight is normal.")
class Student(Person):
	def __init__(self,name, gender, height, weight, age):
		self.age = age
		Person.__init__(self,name, gender, height, weight)
	def decision(self):
		if self.age > 18:
			print("You can be entered in our sports club without parents signature.\n Dont forget to bring  your passport.")
		else :
			print("We need your parents signature to confirm your membership.")	


Ann = Student("Ann","female",165,56,12)
Ann.optimal_weight()
Ann.decision()

#2
class Country:
	def __init__(self,country_name,continent):
		self.country_name = country_name
		self.continent = continent
	def loc_text(self):
		return F"{self.country_name} is located in {self.continent}."
class Brand:
	def __init__(self,brand_name, start):
		self.brand_name = brand_name
		self.start = start
	def presentation(self):
		return F'{self.brand_name} was founded in {self.start} {self.country_name}.'
class Season:
	def __init__(self,season_name, temperature):
		self.season_name = season_name
		self.temperature = temperature
	def info(self):
		return F"In {self.season_name} average temperature in {self.country_name} is {self.temperature}."

class Product(Country, Brand,Season):
	def __init__(self, country_name,continent,brand_name, start,season_name,temperature,product_name,product_type, price,quantity):
		self.product_name = product_name
		self.product_type = product_type
		self.price = price
		self.quantity = quantity
		Country.__init__(self,country_name,continent)
		Brand.__init__(self,brand_name, start)
		Season.__init__(self,season_name,temperature)
	def product_presentation(self):
		pop = F"The most popular product of {self.brand_name} is {self.product_name} which is {self.product_type}"
		con = F"Highest consumption of {self.product_type} is in {self.season_name}"
		return  self.presentation(),self.loc_text() ,self.info(), pop,con
	def product_discount(self,discount):
		self.price -= self.price *discount/100
		return self.price
	def quantity_increase(self,inc):
		self.quantity +=inc
		return self.quantity

d =Product("Armenia","Asia", "Grand Candy", 2000, "summer", +29,"Sandwich","ice_cream", 120,25)
print(d.product_presentation())
print(d.product_discount(5))
print(d.quantity_increase(10))
