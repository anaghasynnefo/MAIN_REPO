# class vehicle:
#     wheel=4
#     door=4

#     def start(self):
#         print("engine start")

#         car=vehicle()
#         car.start()

# class vehicle:
#     wheel=4
#     door=4

#     def start(self,a,b):
#         print("a*b")

#         car=vehicle()
#         car.start(5,3)

# class vehicle:
#     wheel=4
#     door=4

#     def start(self,type):
#         print("type,engine start")

#         car=vehicle()
#         car.start("engine stop")


# class vehicle:
#     color="red"
#     def show(self):
#         print("color is",self.color)
# car=vehicle()
# car.show()

# class vehicle:
#     def setcolor(self,color):
#         self.color=color
#     def show(self):
#         print("color is",self.color)
# car=vehicle() 
# car.setcolor("meroon")       
# car.show()


class vehicle:
    def setcolor(self,seat):
        self.seat=seat
    def show(self):
        print("number of seat  is",self.seat)
car=vehicle() 
car.setcolor("5")       
car.show()