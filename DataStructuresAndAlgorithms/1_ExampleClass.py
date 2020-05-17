class Dog:
    def __init__(self, name, month, day, year, speakText):
        self.name = name
        self.month = month
        self.day = day
        self.year = year
        self.speakText = speakText

    def bark(self):
        return self.speakText

    def getName(self):
        return self.name

    def getBirthday(self):
        return self.month + "/" + self.day + "/" + self.year

    def setName(self, name):
        self.name = name


if __name__ == "__main__":
    Lulu = Dog('Lulu', 1, 1, 2020, 'Gau gau')
    print(Lulu.bark())
