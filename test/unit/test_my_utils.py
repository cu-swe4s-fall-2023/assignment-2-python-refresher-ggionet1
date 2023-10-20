import sys
import unittest
import numpy as np
import statistics
import random
import os
sys.path.insert(0, '../../src/get_column_project')  # noqa
import my_utils


#  Test mean, median, and std_dev
class Test_mean(unittest.TestCase):
    def test_mean_randval(self):
        for i in range(100):
            test_list = [random.randint(-50, 50), random.randint(-50, 50),
                         random.randint(-50, 50), random.randint(-50, 50),
                         random.randint(-50, 50)]
            self.assertEqual(my_utils.mean(test_list), np.mean(test_list))

    def test_mean_emptylist(self):
        test_list_2 = []
        with self.assertRaises(SystemExit):
            my_utils.mean(test_list_2)


class Test_median(unittest.TestCase):
    def test_median_randval(self):
        for i in range(100):
            test_list = [random.randint(-50, 50), random.randint(-50, 50),
                         random.randint(-50, 50), random.randint(-50, 50),
                         random.randint(-50, 50)]
            self.assertEqual(my_utils.median(test_list), np.median(test_list))


class Test_std_dev(unittest.TestCase):
    def test_std_dev_randval(self):
        for i in range(100):
            test_list = [random.randint(-50, 50), random.randint(-50, 50),
                         random.randint(-50, 50), random.randint(-50, 50),
                         random.randint(-50, 50)]
            self.assertEqual(round(my_utils.std_dev(test_list), 3),
                             round(statistics.stdev(test_list), 3))


#  Test get_column()
class Test_get_column(unittest.TestCase):
    @classmethod
    def setUp(self):
        country_names = ["USA", "Canada",
                         "UK", "Australia",
                         "Germany", "France", "Japan",
                         "China", "India", "Brazil"]
        self.test_file_name = 'setup_test_file.txt'
        with open(self.test_file_name, 'w') as f:
            for i in range(100):
                random_number = random.randint(1, 1000)
                country_name = random.choice(country_names)
                # Write the data to the file
                f.write(f"{random_number},{country_name}\n")
        f.close()

    @classmethod
    def tearDown(self):
        os.remove(self.test_file_name)

    def test_get_column(self):
        self.assertIsNotNone(
            my_utils.get_column(self.test_file_name, 1, "China", 0))

    def test_get_column(self):
        with self.assertRaises(ValueError):
            my_utils.get_column(self.test_file_name,
                                1, "Country_Not_On_List", 0)


#  Define main
def main():
    unittest.main()


if __name__ == '__main__':
    main()
