import unittest

class TestAnimalShelter(unittest.TestCase):
    def setUp(self):
        self.shelter = AnimalShelter()

    def test_enqueue_and_dequeue_dog(self):
        dog1 = Animal("dog", "Buddy")
        dog2 = Animal("dog", "Max")

        self.shelter.enqueue(dog1)
        self.shelter.enqueue(dog2)

        self.assertEqual(self.shelter.dequeue("dog").name, "Buddy")
        self.assertEqual(self.shelter.dequeue("dog").name, "Max")

    def test_enqueue_and_dequeue_cat(self):
        cat1 = Animal("cat", "Whiskers")
        cat2 = Animal("cat", "Mittens")

        self.shelter.enqueue(cat1)
        self.shelter.enqueue(cat2)

        self.assertEqual(self.shelter.dequeue("cat").name, "Whiskers")
        self.assertEqual(self.shelter.dequeue("cat").name, "Mittens")

    def test_enqueue_and_dequeue_without_pref(self):
        dog1 = Animal("dog", "Buddy")
        cat1 = Animal("cat", "Whiskers")

        self.shelter.enqueue(dog1)
        self.shelter.enqueue(cat1)

        # Without preference, the oldest animal (Buddy) should be dequeued first
        self.assertEqual(self.shelter.dequeue().name, "Buddy")

    def test_dequeue_with_invalid_pref(self):
        dog1 = Animal("dog", "Buddy")

        self.shelter.enqueue(dog1)

        # Invalid preference should return None
        self.assertIsNone(self.shelter.dequeue("bird"))

    def test_dequeue_empty_shelter(self):
        # Dequeue from an empty shelter should return None
        self.assertIsNone(self.shelter.dequeue("dog"))
        self.assertIsNone(self.shelter.dequeue("cat"))
        self.assertIsNone(self.shelter.dequeue())

if __name__ == '__main__':
    unittest.main()
