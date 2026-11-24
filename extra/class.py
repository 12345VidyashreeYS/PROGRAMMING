# class fan:

#     def __init__(self):
#         self.brand="Usha"
#         self.color="black"
#         self.cost=1500

#     def rotate(self):
#         print("Fan is rotating")

#     def on(self):
#         print("Fan is on")

# f1=fan()

# print(f1.brand)
# print(f1.color)
# print(f1.cost)

# f1.rotate()

class Hero:

    def __init__(self):
        self.name="Yash"
        self.age=40

    def work(self):
        print("He is an artist")

h=Hero()

print(h.name)
print(h.age)

h.movie="Ramayana"
print(h.movie)

h.age=41
print(h.age)
h.age=45
print(h.age)

h1=h
print(h1)

print(id(h1))