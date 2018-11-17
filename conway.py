from unittest import TestCase

import numpy as np
from scipy.signal import convolve as sconv


GOL_KERNEL = np.array([[1, 1, 1],
                           [1, 0, 1],
                           [1, 1, 1]])
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

    def test_alive_neighbors(self):
        cases = range(9)
        for case in cases:
            next_state = get_next_state(1, case)
            if case<2 or case > 3:
                self.assertEqual(0, next_state)
            else:
                self.assertEqual(1, next_state)
        



def update(mat) -> np.ndarray:
    """
    Convovle over mat with kernel X
    Compare  with cutoffs
    """
    return mat


def get_next_state(current_state, alive_neighbors):
    if current_state==1:
        if alive_neighbors < 2 or alive_neighbors > 3:
            return 0
        else:
            return 1


def convolve(mat, kernel=GOL_KERNEL):
    return sconv(mat, kernel, mode='same')
