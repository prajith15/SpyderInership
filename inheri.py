# Single Inheritance
class Balachander():
    def car(self):
        print("Dad 1 car")
    
    def food(self):
        print("Parotta in Dads house")
    
    def property(self):
        print("Dads property and money")

class Deva(Balachander):
    
      def bike(self):
          print('Deva bike')
      def dress(self):
          print("Deva dress")

    
obj=Deva()
obj.bike()
obj.car()
obj.fake_car()

# Multilevel Inheritance
class Balachander():
    def car(self):
        print("Dad 1 car")
    
    def food(self):
        print("Parotta in Dads house")
    
    def property(self):
        print("Dads property and money")

class Deva(Balachander):
    
      def bike(self):
          print('Deva bike')
      def dress(self):
          print("Deva dress")

class Devasri(Deva):

     def toy(self):
         print('Devasri toys')
    
# Hierarchical Inheritance

class Balachander():
    def car(self):
        print("Dad 1 car")
    
    def food(self):
        print("Parotta in Dads house")
    
    def property(self):
        print("Dads property and money")

class Deva(Balachander):
    
      def bike(self):
          print('Deva bike')
      def dress(self):
          print("Deva dress")

class Devasri(Balachander):

     def toy(self):
         print('Devasri toys')
    
obj=Deva()
obj.toy()
obj.bike()
obj.car()
obj.fake_car()
    
# multiple inheritance
class Balachander():
    def car(self):
        print("Dad 1 car")
    
    def food(self):
        print("Parotta in Dads house")
    
    def property(self):
        print("Dads property and money")

class fake_dad():
    def fake_car(self):
      print('Fake dads car 2')

class Deva(Balachander,fake_dad):
    
      def bike(self):
          print('Deva bike')
      def dress(self):
          print("Deva dress")
