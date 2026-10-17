import math
import unittest
from probability import probability,binomial_probability,expected_points
class ProbabilityTests(unittest.TestCase):
    def test_conditional_counts(self):
        self.assertAlmostEqual(probability(329,786),.4185750636)
        self.assertAlmostEqual(expected_points(374,648,2),1.15432098765)
    def test_binomial_distribution_normalizes(self):
        self.assertAlmostEqual(sum(binomial_probability(k,12,.41) for k in range(13)),1.)
    def test_degenerate_distribution(self):
        self.assertEqual(binomial_probability(0,4,0),1)
        self.assertEqual(binomial_probability(4,4,1),1)
        self.assertEqual(binomial_probability(2,4,1),0)
    def test_invalid_counts(self):
        for a,b in [(1,0),(-1,5),(6,5),(True,2)]:
            with self.assertRaises(ValueError):probability(a,b)
    def test_invalid_probability(self):
        for p in [-1,2,float('nan')]:
            with self.assertRaises(ValueError):binomial_probability(1,3,p)
if __name__=='__main__':unittest.main()
