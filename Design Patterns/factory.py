from abc import ABC, abstractmethod
'''
1. Abstract Classes:

The code defines an abstract base class named Shape using ABC from the abc module. This class represents the general concept of a shape and has an abstract method draw() that subclasses must implement.
2. Concrete Shape Classes:

Two concrete classes, Square and Circle, inherit from the Shape class. These classes implement the draw() method specific to each shape (printing "Drawing a Square" or "Drawing a Circle").
3. Factory Interface:

An abstract class named ShapeFactory is also defined using ABC. This class serves as the factory interface and has an abstract method create_shape() that concrete factory subclasses must implement.
4. Concrete Factory Classes:

Two concrete factory classes, SquareFactory and CircleFactory, inherit from ShapeFactory. Each factory class implements the create_shape() method to return the appropriate concrete shape object (Square or Circle).
5. Main Function:

The main() function demonstrates how to use the factory pattern.

It creates instances of the concrete factory classes (SquareFactory and CircleFactory).
It calls the create_shape() method on each factory to get the corresponding shape object.
Finally, it calls the draw() method on the shape objects to print their specific output.
'''


class Shape(ABC):
  @abstractmethod
  def draw(self):
    pass

class Square(Shape):
  def draw(self):
    print("Drawing a Square")

class Circle(Shape):
  def draw(self):
    print("Drawing a Circle")

class ShapeFactory(ABC):
  @abstractmethod
  def create_shape(self) -> Shape:
    pass

class SquareFactory(ShapeFactory):
  def create_shape(self) -> Shape:
    return Square()

class CircleFactory(ShapeFactory):
  def create_shape(self) -> Shape:
    return Circle()

def main():
  # Use the factory to create different shapes
  square_factory = SquareFactory()
  square = square_factory.create_shape()
  square.draw()

  circle_factory = CircleFactory()
  circle = circle_factory.create_shape()
  circle.draw()

if __name__ == "__main__":
  main()
