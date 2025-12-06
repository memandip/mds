# Q29: Create a class Time with three instance variables hours, minutes, and seconds.
# Add instance methods display() to display the time in hh:mm:ss format and add() to add two time objects.
# Use this class to add and display two different time objects.

class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def display(self):
        print(f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}")

    def add(self, other):
        total_seconds = self.seconds + other.seconds
        total_minutes = self.minutes + other.minutes + total_seconds // 60
        total_hours = self.hours + other.hours + total_minutes // 60
        seconds = total_seconds % 60
        minutes = total_minutes % 60
        hours = total_hours % 24
        return Time(hours, minutes, seconds)

print("Enter first time:")
h1 = int(input("Hours: "))
m1 = int(input("Minutes: "))
s1 = int(input("Seconds: "))
t1 = Time(h1, m1, s1)

print("Enter second time:")
h2 = int(input("Hours: "))
m2 = int(input("Minutes: "))
s2 = int(input("Seconds: "))
t2 = Time(h2, m2, s2)

t3 = t1.add(t2)
print("Sum of times:")
t3.display()
