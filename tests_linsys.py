import unittest

from line import MyDecimal
from linsys import LinearSystem
from plane import Plane
from vector import Vector


class LinearSystemTestCase(unittest.TestCase):
    def test_something(self):
        p0 = Plane(normal_vector=Vector(['1', '1', '1']), constant_term='1')
        p1 = Plane(normal_vector=Vector(['0', '1', '0']), constant_term='2')
        p2 = Plane(normal_vector=Vector(['1', '1', '-1']), constant_term='3')
        p3 = Plane(normal_vector=Vector(['1', '0', '-2']), constant_term='2')

        s = LinearSystem([p0, p1, p2, p3])

        print(s.indices_of_first_nonzero_terms_in_each_row())
        print('{},{},{},{}'.format(s[0], s[1], s[2], s[3]))
        print(len(s))
        print(s)

        s[0] = p1
        print(s)

        print(MyDecimal('1e-9').is_near_zero())
        print(MyDecimal('1e-11').is_near_zero())

    def test_quiz(self):
        p0 = Plane(normal_vector=Vector(['1', '1', '1']), constant_term='1')
        p1 = Plane(normal_vector=Vector(['0', '1', '0']), constant_term='2')
        p2 = Plane(normal_vector=Vector(['1', '1', '-1']), constant_term='3')
        p3 = Plane(normal_vector=Vector(['1', '0', '-2']), constant_term='2')

        s = LinearSystem([p0, p1, p2, p3])
        s.swap_rows(0, 1)
        self.assertTrue(s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3)

        s.swap_rows(1, 3)
        self.assertTrue(s[0] == p1 and s[1] == p3 and s[2] == p2 and s[3] == p0)

        s.swap_rows(3, 1)
        self.assertTrue(s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3)

        s.multiply_coefficient_and_row(1, 0)
        self.assertTrue(s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3)

        s.multiply_coefficient_and_row(-1, 2)
        self.assertTrue(s[0] == p1 and
                        s[1] == p0 and
                        s[2] == Plane(normal_vector=Vector(['-1', '-1', '1']), constant_term='-3') and
                        s[3] == p3)

        s.multiply_coefficient_and_row(10, 1)
        self.assertTrue(s[0] == p1 and
                        s[1] == Plane(normal_vector=Vector(['10', '10', '10']), constant_term='10') and
                        s[2] == Plane(normal_vector=Vector(['-1', '-1', '1']), constant_term='-3') and
                        s[3] == p3)

        s.add_multiple_times_row_to_row(0, 0, 1)
        self.assertTrue(s[0] == p1 and
                        s[1] == Plane(normal_vector=Vector(['10', '10', '10']), constant_term='10') and
                        s[2] == Plane(normal_vector=Vector(['-1', '-1', '1']), constant_term='-3') and
                        s[3] == p3)

        s.add_multiple_times_row_to_row(1, 0, 1)
        self.assertTrue(s[0] == p1 and
                        s[1] == Plane(normal_vector=Vector(['10', '11', '10']), constant_term='12') and
                        s[2] == Plane(normal_vector=Vector(['-1', '-1', '1']), constant_term='-3') and
                        s[3] == p3)

        s.add_multiple_times_row_to_row(-1, 1, 0)
        self.assertTrue(s[0] == Plane(normal_vector=Vector(['-10', '-10', '-10']), constant_term='-10') and
                        s[1] == Plane(normal_vector=Vector(['10', '11', '10']), constant_term='12') and
                        s[2] == Plane(normal_vector=Vector(['-1', '-1', '1']), constant_term='-3') and
                        s[3] == p3)

if __name__ == '__main__':
    unittest.main()
