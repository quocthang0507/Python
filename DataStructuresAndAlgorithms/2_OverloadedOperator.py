class Dog:
	def __init__(self, name, month, day, year, speakText):
		self.name = name
		self.month = month
		self.day = day
		self.year = year
		self.speakText = speakText

	def getBark(self):
		return self.speakText

	def getName(self):
		return self.name

	def getBirthday(self):
		return "{}/{}/{}".format(self.month, self.day, self.year)

	def setName(self, name):
		self.name = name
	
	def setBark(self, bark):
		self.speakText = bark

	def toString(self):
		return '{}, borns at {}, barks \'{}\''.format(self.getName(), self.getBirthday(), self.getBark())

	def __add__(self, other):
		return Dog('Puppy of ' + self.name + ' and ' + other.name, self.month, other.day, self.year + 1, self.getBark() + ' ' + other.getBark())

def main():
	boyDog = Dog('Alex', 5, 17, 2019, 'WOOOOF')
	girlDog = Dog('Alisa', 7, 15, 2019, 'Gauuuu')
	print(boyDog.toString())
	print(girlDog.toString())
	puppy = boyDog + girlDog
	puppy.setName = "Puppy"
	print(puppy.toString())

if __name__ == "__main__":
	main()