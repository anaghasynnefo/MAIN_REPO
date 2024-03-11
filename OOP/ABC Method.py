from abc import ABC,abstractmethod

class animal(ABC):
    @abstractmethod
    def speak(self):
      pass

class dog(animal):
   def speak(self):
      print ("dog will bark")
      
   
class cat(animal):
   def speak(self):
      print ("cat will make sound MEOW")
   
dog=dog()
dog.speak()
cat=cat()
cat.speak()



   