#!/data/data/com.termux/files/usr/bin/python3

class Bicycle:
    """
    Bicycle is a class which describes a bicycle.
    """
    wheel = 'wheel'
    def __init__(self, frame, fork, wheels):
        self.frame = frame
        self.fork = fork
        self.wheels = wheels
    def describe(self):
        return f"A vehicle with a {self.frame} frame and a {self.fork} fork."
    def wheeled(self):
        return f"A vehicle with {self.wheels} wheels."
    @classmethod
    def tricycle(cls, wheels=None):
        if not wheels:
            wheels = [cls.wheel, cls.wheel, cls.wheel]
            return cls(None, None, wheels)

giant = Bicycle('Giant', 'RockShox', ['WTB', 'WTB'])
print(giant.describe())
print(f"Giant has a {giant.fork} fork.")
giant.lights = ['front', 'rear']
print(f"Giant has {giant.lights} lights.")
del giant.lights

thrice = Bicycle.tricycle()
print(f"Tricycle 1 has {thrice.wheels}.")

class Tricycle(Bicycle):
    wheel = 'wheel'
    def __init__(self, wheels=None):
        if not wheels:
            wheels = [self.wheel, self.wheel, self.wheel]
        self.wheels = wheels
    def wheeled(self):
        initial = super().wheeled()
        return f"{initial}"

trike = Tricycle()
print(f"Tricycle 2 has {trike.wheels}.")
print(trike.wheeled())

