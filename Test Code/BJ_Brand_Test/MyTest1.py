import unittest
import ice_cream as ic # not made yet
class TestStuff(unittest.TestCase):
    def test1(self):
        self.assertEquals((ic.brandSearch("bj"))[0].getName(), "Salted Caramel Core")
if __name__ == '__main__':
    unittest.main()