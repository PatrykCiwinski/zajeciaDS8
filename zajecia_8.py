class square:
    def __init__(self,a):
        self.a = a
        self.sides =4

    def area(self):
        print(self.a**2)

    def circuit(self):
        print(self.a*4)

    def show_sides(self):
        print(self.sides)

sq1=square(4)

sq1.area()
sq1.circuit()
print(sq1.sides)

sq2=square(8)

sq2.area()
sq2.circuit()

