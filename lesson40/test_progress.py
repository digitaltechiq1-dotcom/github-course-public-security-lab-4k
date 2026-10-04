import unittest
from progress import progress, summary

class ProgressTests(unittest.TestCase):
    def test_quarter(self): self.assertEqual(progress(1,4),25)
    def test_rounding(self): self.assertEqual(progress(2,3),67)
    def test_empty(self): self.assertEqual(progress(0,5),0)
    def test_complete(self): self.assertEqual(progress(5,5),100)
    def test_bool(self):
        with self.assertRaises(TypeError): progress(True,5)
    def test_invalid_range(self):
        with self.assertRaises(ValueError): progress(6,5)

class SummaryTests(unittest.TestCase):
    def test_readable_summary(self): self.assertEqual(summary(3,8),"3/8 complete (38%)")
    def test_zero_summary(self): self.assertEqual(summary(0,4),"0/4 complete (0%)")
    def test_invalid_summary(self):
        with self.assertRaises(ValueError): summary(1,0)

if __name__ == "__main__": unittest.main()
