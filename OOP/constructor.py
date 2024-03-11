# class vehicle:
#     def __init__(self,color,tyre):
#         self.color=color
#         self.tyre=tyre
#     def show(self):
#         print("color is",self.color,"tyre is",self.tyre)

# car=vehicle("red",4)
# car.show()


# class flower:
#     def __init__(self,color,petals):
#         self.color=color
#         self.petals=petals
#     def show(self):
#         print("color is",self.color,"petals of flower is",self.petals)

# rose=flower("violet",8)
# rose.show()

class animal:
    def __init__(self,legs,mouth,eyes):
        self.legs=legs
        self.mouth=mouth
        self.eyes=eyes
    def show(self):
        print("leg is",self.legs,"num of mouth is",self.mouth,"color of eyes is",self.eyes)

lion=animal(4,1,"brown")
lion.show()