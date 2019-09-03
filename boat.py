
# Define a class called Boat
# Give it a method that allows the boat to move that prints the speed it's moving
# Define a Class called Kayak
# Make it a derived class of Boat
# Give it a method called `paddle` that uses its inherited `move` method

# Make a Kayak instance and 'paddle' it


class Boat:
  def __init__(self, type, propulsion):
    self.type = type
    self.propulsion = propulsion

  def move(self, speed):
      return f"the boat is moving at {speed} knots."


class Kayak(Boat):
  def __init__(self, passengers = 1):
    # super init is how you gain access to inherited methods from parent a parent or sibling class
    super().__init__("kayak", "paddle") # paddle = type paddle = propulsion
    self.passengers = passengers

  def paddle(self, move):
      print(f'I like to go out in my kayak and {move}')


kayak22 = Kayak(1)
kayak22.paddle(23)
kayak22.paddle(3)



