class person:
    def __init__(self, name="", age=0, hight=0, weight=0):
        self.name = name
        self.age = age
        self.hight = hight
        self.weight = weight

    def __str__(self):
        return self.name + "," + str(self.age) + "," + str(self.hight) + "/" + str(self.weight)

a = person(name="Masahiro", hight=169, weight=70)
print(a)
print(a.name)
print(a.age)
print(a.hight)
print(a.weight)

b = person()
print(b)
print(b.name)
print(b.age)
print(b.hight)
print(b.weight)
