from typing import List, Optional, Dict
from src.animal import Animal

class Zoo:
    """Класс для управления зоопарком и коллекцией животных.
        _name (str)
        _location (str)
        _animals (List[Animal]).
    """

    def __init__(self, name: str, location: str):
        self._name = name
        self._location = location
        self._animals: List[Animal] = []

    @property
    def name(self) -> str:
        return self._name

    @property
    def location(self) -> str:
        return self._location

    @property
    def animals(self) -> List[Animal]:
        return self._animals
    
    def add_animal(self, animal: Animal) -> None:
            self._animals.append(animal)
            print(f"{animal.name} был добавлен в {self._name}.")

    def remove_animal(self, animal: Animal) -> None:

        self._animals.remove(animal)
        print(f"{animal.name} покинул {self._name}.")

    def feed_all(self) -> None:
        print("\n Пора есть")
        for animal in self._animals:
            animal.eat("стандартный рацион")

    def exercise_all(self) -> None:
        print("\n Время тренировки")
        for animal in self._animals:
            print(f"{animal.name} активно двигается!")
            animal.make_sound()

    def get_animal_by_name(self, name: str) -> Optional[Animal]:
        for animal in self._animals:
            if animal.name == name:
                return animal
        return None

    def get_count_by_species(self, species_name: str) -> int:
        count = 0
        for animal in self._animals:
            if type(animal).__name__ == species_name or getattr(animal, 'species', '') == species_name:
                count += 1
        return count

    def display_animals(self) -> None:
        print(f"\nЖивотные в {self._name} ({self._location}):")
        for animal in self._animals:
                print(f"- {animal.name} ({type(animal).__name__})")