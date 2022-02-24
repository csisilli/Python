class Rectangle():
    def __init__(self,length,width):
        self.length =int(length)
        self.width= int(width)
    def rectangle_area(self):
        return self.width*self.length
    def display(self):
        print("Length: ", self.length)
        print("Width: ",self.width)
        print("Area: ",self.rectangle_area())
newRectangle = Rectangle(12, 10)
newRectangle.display()
