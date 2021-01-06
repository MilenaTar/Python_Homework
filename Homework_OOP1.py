from math import pi
class Di:
	def __init__(self, a:str, a2:dict):
		self.a = a
		self.a2 = a2
	def dict_func(self): #1
		my_dict = {}
		letters = list(self.a)
		numb = []
		for i in letters:
			my_dict[i] = letters.count(i)
		return my_dict
	def duplic_func(self) : #2
		dict2 ={}
		l = []
		for i, j in self.a2.items():
			if j not in l:
				l.append(j)
				dict2[i] = j
		return dict2
	def maxi_func(self): #3
		list1 = []
		dict3 = {}
		val1 = list(self.a2.values())
		key1 = list(self.a2.keys())
		while len(list1) <3:
			list1.append(max(val1))
			c = val1.index(max(val1))
			dict3[key1[c]] = val1[c]
			val1.remove(max(val1))
		return "Here is a dictionary with 3 max values", dict3

info = Di("Happy",{"a": 155, "v": 10, "e": 24, "m": 10, "s": 10, "p":440, "h": 25})
print(info.dict_func())
print(info.duplic_func())
print(info.maxi_func())

#4
class Circle:
	def __init__(self, radius):
		self.radius = radius 
	def area(self):
		return "Area", pi * self.radius ** 2
	def perimeter(self):
		return "Perimeter", pi * self.radius * 2

sh = Circle(5)
print(sh.area())
print(sh.perimeter())

#5
class Elements:
	def __init__(self,l):
		self.l = l
		target=50
		list3 =self.l.copy()
		for i in self.l:
			c = target - i
			if i == target:
				print(list3.index(i))
				self.l.remove(i)
			elif c in self.l:
				print(list3.index(i) + list3.index(c))
				self.l.remove(i)
				self.l.remove(c)

t = Elements([10,20,10,40,50,60,70])



