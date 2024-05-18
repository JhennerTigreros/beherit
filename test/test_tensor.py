#!/usr/bin/env python
import unittest

from beherit.tensor import Tensor

class TestTensor(unittest.TestCase):
    def test_zero_dim_init(self):
        x = Tensor(42)
        y = Tensor(1.13)

        self.assertEqual(x.shape, ())
        self.assertEqual(y.shape, ())

    def test_correct_tensor(self):
        x = Tensor([[0, 1], [1, 0]])

        self.assertEqual(x.to_list(), [[0, 1], [1, 0]], "the data is not the same.")


if __name__ == '__main__':
    unittest.main()