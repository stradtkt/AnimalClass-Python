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
  def __init__(self, name, health=150):
    super(Dog, self).__init__(name, health)
  def pet(self):
    self.health += 5
    print "Health after petting: " + str(self.health)
    return self

dog_1 = Dog("Buster")
dog_1.walk().walk().walk().run().run().pet().display_health()

class Dragon(Animal):
  def __init__(self,name,health=170):
    super(Dragon, self).__init__(name, health)
  
  def fly(self):
    self.health -= 10
    return self

  def display_health(self):
    super(Dragon, self).display_health()
    print "I am a Dragon"
dragon_1 = Dragon("Optimus")
dragon_1.fly().fly().display_health()

# Below will produce an error
# animal_1 = Animal("Buddy", 100)
# animal_1.pet().fly()
