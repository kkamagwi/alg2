import unittest
from alg2.worker import Programist

class Testov(unittest.TestCase):

    def test_name(self):
        oleg = Programist()
        self.assertEqual(oleg.name, 'Oleg')



if __name__=="__main__":
    unittest.main()