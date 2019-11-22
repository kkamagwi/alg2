import unittest
from alg2.worker import Programist

class Testov(unittest.TestCase):

    def test_name(self):
        oleg = Programist()
        self.assertEqual(oleg.name, 'Oleg')

    def test_age(self):
        cat = favorite_pet()
        self.assertEqual(cat.favorite_pet, 'cat')



if __name__=="__main__":
    unittest.main()