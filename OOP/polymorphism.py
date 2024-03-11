# """METHOD OVERLOADING"""

# class A:
#     def add(self,a,b,c=0):
#         return a+b+c
#     def add(self,a,b,c=0):
#         return a+b+c
# ob=A()
# print(ob.add(5,3,4))

# """METHOD OVERRIDING"""

# class animal:
#     def sound(self):
#         print("animals will make sound")


# class dog(animal):
#     def sound(self):
#         print("dogs are barking")
# d=animal()
# d=dog()
# d.sound()

# class A:
#     def add(self,a,b,c=0):
#         return a+b+c
#     def add(self,a,b,c=0):
#         return a+b+c
# ob=A()
# print(ob.add(5,5,5))





class pathanamthitta:
    def place(self):
        print("chuttipara")
class konni(pathanamthitta):
    def place(self):
        print("adavi")
class seethathodu(pathanamthitta):
    def place(self):
        print("gavi")
a=pathanamthitta()
b=konni()
c=seethathodu()

a.place()
b.place()
c.place()


