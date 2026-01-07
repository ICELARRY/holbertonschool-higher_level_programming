# task_05_dragon.py

# Mixin for swimming behavior
class SwimMixin:
    def swim(self):
        print("The creature swims!")


# Mixin for flying behavior
class FlyMixin:
    def fly(self):
        print("The creature flies!")


# Dragon class inherits behaviors from both mixins
class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")
