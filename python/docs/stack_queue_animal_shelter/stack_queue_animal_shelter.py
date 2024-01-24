from collections import deque

class Animal:
    def __init__(self, species, name):
        self.species = species
        self.name = name

class AnimalShelter:
    def __init__(self):
        self.dog_queue = deque()
        self.cat_queue = deque()

    def enqueue(self, animal):
        if animal.species == "dog":
            self.dog_queue.append(animal)
        elif animal.species == "cat":
            self.cat_queue.append(animal)

    def dequeue(self, pref=""):
        if pref == "dog":
            return self._dequeue_helper(self.dog_queue)
        elif pref == "cat":
            return self._dequeue_helper(self.cat_queue)
        elif pref == "":
            # If no preference, return the animal that has been waiting the longest
            dog = self._dequeue_helper(self.dog_queue)
            cat = self._dequeue_helper(self.cat_queue)
            return dog if (dog and (not cat or dog.timestamp < cat.timestamp)) else cat
        else:
            return None

    def _dequeue_helper(self, queue):
        if queue:
            return queue.popleft()
        else:
            return None

# Example usage:
dog1 = Animal("dog", "Buddy")
dog2 = Animal("dog", "Max")
cat1 = Animal("cat", "Whiskers")

shelter = AnimalShelter()
shelter.enqueue(dog1)
shelter.enqueue(cat1)
shelter.enqueue(dog2)

print(shelter.dequeue("dog").name)  # Output: Buddy
print(shelter.dequeue("cat").name)  # Output: Whiskers
print(shelter.dequeue())            # Output: Max (oldest animal without preference)
