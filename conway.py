from unittest import TestCase

import numpy as np
from scipy.signal import convolve as sconv

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

    def test_convolve(self):
        matrix = np.array([[1, 1, 0],
                           [0, 0, 0],
                           [0, 1, 0]])
        kernel = np.array([[1, 1, 1],
                           [1, 0, 1],
                           [1, 1, 1]])
        result = np.array([[1, 1, 1],
                           [3, 3, 2],
                           [1, 0, 1]])
        output = convolve(matrix, kernel)
        self.assertTrue(np.array_equal(output, result))

def update(mat) -> np.ndarray:
    """
    Convovle over mat with kernel X
    Compare  with cutoffs
    """
    return mat

def convolve(mat, kernel):
    return sconv(mat, kernel, mode='same')
