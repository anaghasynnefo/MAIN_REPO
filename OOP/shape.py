class shape:
    def area(self):
      return 0
    
class derived_circle(shape):
  def __init__(self,radius):
     self.radius=radius
def area(self):
     return  self.radius**2*3.14


class derived_rectangle(shape):
   def __init__(self,length,width):
      self.length=length
      self.width=width
def area(self):
      return self.length*self.width


circle_obj=derived_circle(2)
rectangle_obj=derived_rectangle(2,3)

circle_area=circle_obj.area()
rectangle_area=rectangle_obj.area()

print("area of circle:   ",circle_area)
print("area of rectangle:    ",rectangle_area)
