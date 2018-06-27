class Animal(object):
  def __init__(self, name, health):
    self.name = name
    self.health = health

  def walk(self):
    self.health -= 1
    print "Health is now: " + str(self.health)
    return self

  def run(self):
    self.health -= 5
    print "Health is now: " + str(self.health)
    return self

  def display_health(self):
    print "Health is: " + str(self.health)
    return self

class Dog(Animal):
  def __init__(self, name, health):
    super(Dog, self).__init__()
  def pet(self):
    self.health += 5
    print "Health after petting: " + self.health

dog_1 = Animal("Buster", 150)
dog_1.walk().walk().walk().run().run().pet().display_health()