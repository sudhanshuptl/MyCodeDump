import unittest

from sorted_set import SortedSet


class TestCunstruction(unittest.TestCase):
    def test_empty(self):
        s = SortedSet([])

    def test_from_sequence(self):
        s = SortedSet([7, 3, 1, 11])

    def test_with_duplicates(self):
        s = SortedSet([4, 4, 4])

    def test_from_ierable(self):
        def my_generater():
            yield 3
            yield 6
            yield 3
            yield 7
            yield 1

        g = my_generater()
        s = SortedSet(g)

    def test_default_null(self):
        s = SortedSet()


class TestContainerProtocal(unittest.TestCase):
    def setUp(self):
        self.s = SortedSet([6, 7, 8, 9])

    def test_positive_contained(self):
        self.assertTrue(6 in self.s)

    def test_negative_contained(self):
        self.assertFalse(2 in self.s)

    def test_positive_not_contained(self):
        self.assertTrue(2 not in self.s)

    def test_negative_not_contained(self):
        self.assertFalse(9 not in self.s)


class TestSizeProtocal(unittest.TestCase):
    def test_empty(self):
        s = SortedSet()
        self.assertEqual(len(s), 0)

    def test_one(self):
        s= SortedSet([32])
        self.assertEqual(len(s), 1)

    def test_10(self):
        s = SortedSet(range(10))
        self.assertEqual(len(s), 10)

    def test_duplicate(self):
        s = SortedSet([10, 10, 10])
        self.assertEqual(len(s), 1)

class TestIterable(unittest.TestCase):
    def setUp(self):
        self.s = SortedSet([1,2,3,4])

    def test_iter(self):
        i = iter(self.s)
        self.assertEqual(next(i), 1)
        self.assertEqual(next(i), 2)
        self.assertEqual(next(i), 3)
        self.assertEqual(next(i), 4)
        self.assertRaises(StopIteration, lambda :next(i))

    def test_for_loop(self):
        index=0
        expected = [1,2,3,4]
        for val in iter(self.s):
            self.assertEqual(val,expected[index])
            index +=1


class TestSequenceProtocol(unittest.TestCase):
    def setUp(self):
        self.s = SortedSet([1,4,9,13,15])

    def test_index_zero(self):
        self.assertEqual(self.s[0], 1)

    def test_index_n(self):
        self.assertEqual(self.s[4], 15)

    def test_beyond_index(self):
        self.assertRaises(IndexError, lambda :self.s[10])

    def test_reverse(self):
        self.assertEqual(self.s[-1], 15)

    def test_from_begining(self):
        self.assertEqual(self.s[:3],SortedSet([1,4,9]))

class TestReperMethod(unittest.TestCase):
    def test_repr_empty(self):
        s=SortedSet()
        self.assertEqual(repr(s), 'SortedSet()')

    def test_not_empty(self):
        s = SortedSet([1,2,3])
        self.assertEqual(repr(s),'SortedSet([1, 2, 3])')
if __name__ == '__main__':
    unittest.main()