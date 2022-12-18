'''
Write a class definition for a Automobile class.

The Automobile class will have the following attributes:
1.	Make
2.	Model
3.	Mileage
4.	Speed
The class has the accessor (get) methods as well as the mutator (set) methods for each instance variable listed above. 
The class also has the __str__ method redefined
In addition the class has the following two methods:
1.	accelerate():  Every time this method is called, the speed of the automobile increases by 7 miles
2.	brake():  Every time this method is called, the speed of the automobile decreases by 5 miles
'''


class Automobile:

#constructor
	def __init__(self, make, model, mileage, speed):
		self.make = make
		self.model = model
		self.mileage = mileage
		self.speed = speed
 

        
	#redefined __str__ method
	def __str__(self):
		return 'Make: ' + self.make + ', Model: ' + self.model  + ', Mileage '  + str(self.mileage)  + ', current speed: ' + str(self.speed)

	#methods specific to the Automobile class
	def accelerate(self):
		self.speed += 5
        
	def brake(self):
		self.speed -= 5
		