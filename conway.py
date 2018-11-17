from unittest import TestCase

import numpy as np

class ConwayGOL(TestCase):

    # def test_simple(self):
    #     matrix = np.array([[1, 1, 0],
    #                        [0, 0, 0],
    #                        [0, 1, 0]])
    #     result = np.array([[0, 0, 0],
    #                        [1, 1, 0],
    #                        [0, 0, 0])
    #     self.assertEqual(result, update(matrix))

    def test_same_size(self):
        matrix = np.array([[1, 1, 0],
                           [0, 0, 0],
                           [0, 1, 0]])
        output = update(matrix)
        self.assertEqual(output.shape, matrix.shape)


def update(mat) -> np.ndarray:
    return mat
