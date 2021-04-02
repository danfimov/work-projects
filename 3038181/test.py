import unittest

from task import Vector, EPSILON


class TestVector(unittest.TestCase):
    def test_init(self):
        with self.assertRaises(TypeError):
            Vector("a")
        with self.assertRaises(TypeError):
            Vector(1)
        with self.assertRaises(TypeError):
            Vector([[1]])
        with self.assertRaises(TypeError):
            Vector(["a"])
        Vector([1])
        Vector((1,))

    def test_equal(self):
        self.assertTrue(Vector([1, 2]) == Vector([1, 2]))
        self.assertTrue(Vector([1, 2]) == Vector([2, 1]))

        self.assertTrue(Vector([1, 2]) == Vector([1, 2 + EPSILON / 10]))
        self.assertTrue(Vector([0]) == Vector([EPSILON]))

        self.assertFalse(Vector([1, 3]) == Vector([1, 2]))

        with self.assertRaises(ValueError):
            Vector([1]) == Vector([1, 2])

    def test_greater(self):
        self.assertTrue(Vector([1, 2]) > Vector([1, 1]))

        self.assertTrue(Vector([1, 2]) >= Vector([1, 2 + EPSILON / 10]))
        self.assertTrue(Vector([1, 2 + EPSILON / 10]) >= Vector([1, 2]))
        self.assertTrue(Vector([0]) >= Vector([EPSILON]))
        self.assertTrue(Vector([EPSILON]) >= Vector([0]))

        self.assertFalse(Vector([1, 2]) >= Vector([1, 3]))

        with self.assertRaises(ValueError):
            Vector([1]) >= Vector([1, 2])

    def test_smaller(self):
        self.assertFalse(Vector([1, 2]) < Vector([1, 1]))
        self.assertTrue(Vector([1, 1]) < Vector([1, 2]))

        self.assertTrue(Vector([1, 2]) <= Vector([1, 2 + EPSILON / 10]))
        self.assertTrue(Vector([1, 2 + EPSILON / 10]) <= Vector([1, 2]))
        self.assertTrue(Vector([0]) <= Vector([EPSILON]))
        self.assertTrue(Vector([EPSILON]) <= Vector([0]))

        self.assertFalse(Vector([1, 3]) <= Vector([1, 2]))
        self.assertFalse(Vector([1, 3]) <= Vector([1, 2]))

        with self.assertRaises(ValueError):
            Vector([1]) <= Vector([1, 2])


if __name__ == '__main__':
    unittest.main()