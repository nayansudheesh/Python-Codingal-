from abc import ABC, abstractmethod
class animal(ABC):
     def move(self):
         pass
class Human(animal):
      def move(self):
         print("I walk on my legs")
class snake(animal):
        def move(self):
             print("I can crawl/slither")
class dog(animal):
        def move(self):
             print("I walk on my 4 legs")
class lion(animal):
        def move(self):
             print("i can walk and run on 4 legs")

h = Human()
h.move()

s = snake()
s.move()

d = dog()
d.move()

l = lion()
l.move()