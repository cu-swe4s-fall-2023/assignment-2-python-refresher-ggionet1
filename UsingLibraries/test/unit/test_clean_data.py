import sys
import unittest
import numpy as np
import matplotlib.pyplot as plt
import random
import os
sys.path.insert(0, '../../src')  # noqa
import collect_data

class Test_clean_data(unittest.TestCase):
    def load_data(self):
        agrofood = pd.read_csv("test/data/agrofood_test_data.csv")
        self.assertIsNotNone(agrofood)

