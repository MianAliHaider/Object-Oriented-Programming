import math
import tkinter as tk
from abc import ABC,abstractmethod 
class Shape:
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def draw(self, canvas):
        pass
class Rectangle(Shape):
    def __init__(self,length,width):
        self.Length = length
        self.Width = width
    
    def area (self):
        return self.Length * self.Width 
    
    def draw(self,canvas):
        canvas.create_rectangle(180, 10, 40 + self.Length, 10 + self.Width, outline="red",fill = "red")
        area_text = (f"Area: {self.area()}")
        canvas.create_text(110 + self.Length / 2,  self.Width /2 , text=area_text, fill="White")
    
class Square(Rectangle):
    def __init__(self,length):
        super().__init__(length,length)
    
    def area(self):
        return self.Length * self.Length
    
    def draw(self,canvas):
        canvas.create_rectangle(10, 10, 10 + self.Length, 10 + self.Length, outline="black",fill = "brown")
        area_text = (f"Area: {self.area()}")
        canvas.create_text(10 + self.Length / 2,  self.Width /2 , text=area_text, fill="White")

class Circle(Shape):
    def __init__(self,radius):
        self.Radius = radius
    
    def area (self):
        return ((self.Radius**2)*math.pi)
    
    def draw(self,canvas):
        canvas.create_oval(500, 500, self.Radius, self.Radius,outline = "green",fill = "green")
        area_text = (f"Area: {self.area()}")
        canvas.create_text(100 + self.Radius ,  100 + self.Radius , text=area_text, fill="Black")

class Oval(Circle):
    def __init__(self, radius_x, radius_y):
        super().__init__(radius_x)
        self.Radius_y = radius_y

    def area(self):
        return math.pi * (self.Radius * self.Radius_y)

    def draw(self, canvas):
        canvas.create_oval(80, 170, self.Radius, self.Radius_y, outline="blue",fill = "blue")
        area_text = (f"Area: {self.area():.0f}")
        canvas.create_text(40 + self.Radius/2,  80 + self.Radius_y /2 , text=area_text, fill="White")
    
def draw_shapes(self):
    root = tk.Tk()
    root.title("Drawing differnt shapes")

    canvas = tk.Canvas(root, width=800, height=800)
    canvas.pack()

    for shape in shapes:
        shape.draw(canvas)

    root.mainloop()


shapes = [Rectangle(220, 300),Square(150),Circle(300),Oval(150,290)]
draw_shapes(shapes)