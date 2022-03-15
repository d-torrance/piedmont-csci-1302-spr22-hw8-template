import unittest
import hw8
import math

class Homework8Tests(unittest.TestCase):
    def test_number_format1(self):
        self.assertEqual(hw8.number_format(math.pi, 2), "3.14")

    def test_number_format2(self):
        self.assertEqual(hw8.number_format(1/3, 5), "0.33333")

    def test_number_format3(self):
        self.assertEqual(hw8.number_format(10000, 0, True), "1e+04")

    def test_number_format4(self):
        self.assertEqual(hw8.number_format(1/math.sqrt(2), 3, True),
                         "7.071e-01")

    def test_is_mac_address1(self):
        self.assertTrue(hw8.is_mac_address("3D:F2:C9:A6:B3:4F"))

    def test_is_mac_address2(self):
        self.assertTrue(hw8.is_mac_address("3D-F2-C9-A6-B3-4F"))

    def test_is_mac_address3(self):
        self.assertFalse(hw8.is_mac_address("A1:B2-C3:D4-E5:F6"))

    def test_is_mac_address4(self):
        self.assertFalse(hw8.is_mac_address("foo3D:F2:C9:A6:B3:4Fbar"))

    def test_factorial1(self):
        fact = hw8.FactorialIterator()
        self.assertEqual(iter(fact), fact)

    def test_factorial2(self):
        fact = hw8.FactorialIterator()
        self.assertEqual(next(fact), 1)

    def test_factorial3(self):
        fact = hw8.FactorialIterator()
        next(fact)
        self.assertEqual(next(fact), 1)

    def test_factorial4(self):
        fact = hw8.FactorialIterator()
        for i in range(10):
            next(fact)
        self.assertEqual(next(fact), 3628800)

    def test_odd_iterator1(self):
        i = hw8.OddIterator([1, 2, 3])
        self.assertEqual(iter(i), i)

    def test_odd_iterator2(self):
        i = hw8.OddIterator([1, 2, 3])
        next(i)
        self.assertRaises(StopIteration, lambda : next(i))

    def test_odd_iterator3(self):
        i = hw8.OddIterator("Hello, world!")
        self.assertEqual(list(i), ['e', 'l', ',', 'w', 'r', 'd'])

    def test_odd_iterator4(self):
        i = hw8.OddIterator(range(10))
        self.assertEqual(list(i), list(range(1, 10, 2)))

    def test_linked_list1(self):
        L = hw8.LinkedList()
        i = iter(L)
        self.assertRaises(StopIteration, lambda : next(i))

    def test_linked_list2(self):
        L = hw8.LinkedList()
        i =iter(L)
        self.assertEqual(i, iter(i))

    def test_linked_list3(self):
        L = hw8.LinkedList()
        L.append(1)
        i = iter(L)
        self.assertEqual(next(i), 1)

    def test_linked_list4(self):
        L = hw8.LinkedList()
        for i in range(10):
            L.append(i)
        self.assertEqual(list(L), list(range(10)))
