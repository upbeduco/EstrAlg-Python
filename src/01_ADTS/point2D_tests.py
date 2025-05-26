import math
from .point2DCartesian import Point2DCartesian
from .point2DPolar import Point2DPolar

import unittest

class TestPoint2D(unittest.TestCase):
    def setUp(self):
        self.p1 = Point2DCartesian(0,0)
        self.p2 = Point2DPolar(1, math.pi/4)
        self.p3 = Point2DCartesian(self.p2.getX(), self.p2.getY())

    def test_equality(self):
        self.assertNotEqual(self.p1, self.p2)
        self.assertEqual(self.p2, self.p3)
        self.assertNotEqual(self.p1, self.p3)

    def test_components(self):
        self.assertAlmostEqual(self.p2.getX(), math.sqrt(2)/2, places=8)
        self.assertAlmostEqual(self.p2.getY(), math.sqrt(2)/2, places=8)

    def test_norm(self):
        self.assertEquals(abs(self.p2), 1.0)
        self.assertEquals(abs(self.p3), 1.0)



if __name__ == "__main__":
    unittest.main()



    