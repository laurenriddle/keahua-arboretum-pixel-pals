from animals import Animal
from interfaces import IFreshwater
from interfaces import Identifiable

class RiverDolphin(Animal, IFreshwater, Identifiable):

    def __init__(self):
        Animal.__init__(self, "River dolphin")

        Identifiable.__init__(self)
        self.__prey = { "Trout", "Mackarel", "Salmon", "Sardine" }

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The dolphin ate {prey} for a meal')
            input("Press any button to continue...")
        else:
            print(f'The dolphin rejects the {prey}')


    def __str__(self):
        return f'Dolphin {self.id}. Eeee EeeEEeeeeEE!'
