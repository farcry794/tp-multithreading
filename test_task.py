import unittest

import numpy as np

from task import Task


class TestTask(unittest.TestCase):
    def test_resolution(self):
        task = Task()
        task.work()
        np.testing.assert_allclose(task.a @ task.x, task.b, rtol=1e-5, atol=1e-5)


if __name__ == "__main__":
    unittest.main()
