class MyDict:
    def __init__(self, name, age):
        self.name = {"name" : name, "age" : age}

    def get(self, value):
        if value in self.name:
            return self.name.get(value)
        else:
            return 0

md1 = MyDict("Phill", 22)
print(md1.get("age"))
print(md1.get("Work"))
