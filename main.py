print ('Hello World!')
print ('My name is Dasha')
print ('What is yours?')
from random import randint
class Student:
	def __init__(self, name):
		self.name = name
		self.gladness = 0
		self.progress = 0
    self.money += 0
		self.alive = True
	def study(self):
		self.progress += 20
		self.gladness -= 10
    self.money += 10
		print('Study time')
	def chill(self):
		self.gladness += 35
		self.progress -= 8
    self.money += 0
		print('Chill time')
	def sleep(self):
		self.gladness += 4
    self.money += 0
		print('Sleep time')
	def say_hello(self):
		print('Hello!')
	def live(self):
		live_cube = randint(1,4)
		if live_cube == 1:
			self.study()
		elif live_cube == 2:
			self.chill()
		elif live_cube == 3:
			self.sleep()
		elif live_cube == 4:
			self.say_hello()
		self.final()
	def final(self):
		if self.progress == 100:
			print('Amazing! You graduated!')
			self.alive = False
		elif self.progress < -20:
			print('Too bad... You are stupid')
			self.alive = False
		elif self.gladness < -20:
			print('Depression :(')
			self.alive = False

print('Bob\'s life')
obj1 = Student('Bob')
for i in range(365):
	if obj1.alive == False:
		break
	obj1.live()

print('Jane\'s life')
obj2 = Student('Jane')
for i in range(365):
	if obj2.alive == False:
		break
	obj2.live()