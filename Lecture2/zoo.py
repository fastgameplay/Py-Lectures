class Animal:
    def eat(self):
        print("ნომ ნომ ნომ")

    def sleep(self):
        print("ხხხხ პშუუუუ")

class Cage:
    def __init__(self):
        self._animals = []

    @property
    def animals(self):
        return self._animals

    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self._animals.append(animal)

class ZooKeeper:
    def feed_animals(self, cage):
        for animal in cage.animals:
            animal.eat()

    def tend_to_animals(self, cage):
        for animal in cage.animals:
            animal.sleep()

    def add_animal(self, cage, animal):
        if isinstance(animal, Animal):
            cage.add_animal(animal)

class PettingZooKeeper(ZooKeeper):
    def pet_animals(self, cage):
        for animal in cage.animals:
            print("პეთ პეთ პეთ ", end=" ")
            animal.eat()

    def add_animal(self, cage, animal):
        raise NotImplementedError("PettingZooKeeper cannot add an animal to a cage")

# მაგალითი:

# lion = Animal()
# elephant = Animal()
# tiger = Animal()

# cage = Cage()
# zookeeper = ZooKeeper()
# petting_zookeeper = PettingZooKeeper()

# cage.add_animal(lion)
# cage.add_animal(elephant)
# cage.add_animal(tiger)

# zookeeper.feed_animals(cage)
# zookeeper.tend_to_animals(cage)

# petting_zookeeper.pet_animals(cage)

# petting_zookeeper.add_animal(cage, Animal())
