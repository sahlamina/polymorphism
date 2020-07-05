class Boy:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a boy. My name is {self.name}. I am {self.age} years old.")

    def play(self):
        print(self.name, " is playing")


class Girl:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a girl. My name is {self.name}. I am {self.age} years old.")

    def play(self):
        print(self.name, " running")


boy = Boy("Boy1", 6)
girl = Girl("Girl1", 8)

for child in (boy, girl):
    child.play()
    child.info()
    child.play()