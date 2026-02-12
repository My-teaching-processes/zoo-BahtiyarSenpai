from src.animal import Animal

class Zoo:
    def __init__(self, name, location):
        self._name = name
        self._location = location
        self._animals = []

    @property
    def name(self):
        return self._name

    @property
    def location(self):
        return self._location

    @property
    def animals(self):
        return self._animals[:]

    def add_animal(self, animal):
        self._animals.append(animal)

    def remove_animal(self, animal):
        if animal in self._animals:
            self._animals.remove(animal)
            return True
        return False

    def get_animal_count(self):
        return len(self._animals)

    def find_animal_by_name(self, name):
        for animal in self._animals:
            if animal.name == name:
                return animal
        return None

    def get_species_count(self, species):
        count = 0
        for animal in self._animals:
            if animal.species == species:
                count += 1
        return count

    def get_all_sounds(self):
        return [animal.make_sound() for animal in self._animals]

    def feed_all(self):
        for animal in self._animals:
            animal.eat("Food")

    def exercise_all(self, minutes):
        for animal in self._animals:
            animal.exercise(minutes)

    def display_animals(self):
        print(f"Zoo: {self._name}")
        for animal in self._animals:
            print(animal)