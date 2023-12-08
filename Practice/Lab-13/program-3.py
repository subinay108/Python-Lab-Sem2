# Write a program that creates and uses a Time class to perform various time arithmetic operations
class Time:
    def __init__(self, hour = 0, minute = 0, second = 0):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.normalize()

    def add(self, t):
        self.hour += t.hour
        self.minute += t.minute
        self.second += t.second
        self.normalize()

    def multiply(self, m):
        self.hour *= m
        self.minute *= m
        self.second *= m
        self.normalize()
    
    def display(self):
        print(f'{self.hour} hour {self.minute} minute {self.second} second')

    def normalize(self):
        seconds = self.hour * 3600 + self.minute * 60 + self.second
        self.second = seconds % 60
        self.minute = (seconds // 60) % 60
        self.hour = seconds // 3600

t1 = Time(2, 35, 45)
t2 = Time(1, 42, 35)

t1.display()
t2.display()

# addition
t1.add(t2)
t1.display()

# multiplication
t2.multiply(2)
t2.display()

