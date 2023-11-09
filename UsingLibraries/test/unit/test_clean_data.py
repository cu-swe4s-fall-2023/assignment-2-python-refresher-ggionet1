import sys
import unittest
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import os
sys.path.insert(0, '../../src')  # noqa
import collect_data as cd


class Test_clean_data(unittest.TestCase):
    
    @classmethod
    def setUp(self):
        self.agrofood = "../data/agrofood_test_data.csv"
        self.gdp = "../data/gdp_test_data.csv"
        self.empty = "../data/empty_data.csv"
        self.agrofood_incorrect_colnames = "../data/agrofood_test_data_incorrectcol.csv"
        self.pd_agrofood = pd.read_csv("../data/agrofood_test_data.csv")
        self.pd_gdp = pd.read_csv("../data/gdp_test_data.csv")

    def test_load_data(self):
        output_data = cd.clean_dataset(self.agrofood, self.gdp,
                                   country1 = "Austria",
                                   country2 = "Norway",
                                   country3 = "Albania",
                                   country4 = "Belgium")
        self.assertIsNotNone(output_data)
        with self.assertRaises(SystemExit):
            output_data = cd.clean_dataset("doesntexist.csv", self.gdp,
                                       country1 = "Austria",
                                       country2 = "Norway",
                                       country3 = "Albania",
                                       country4 = "Belgium")
        with self.assertRaises(SystemExit):
            output_data = cd.clean_dataset(self.empty, self.gdp,
                                       country1 = "Austria",
                                       country2 = "Norway",
                                       country3 = "Albania",
                                       country4 = "Belgium")
        with self.assertRaises(ValueError):
            output_data = cd.clean_dataset(self.agrofood_incorrect_colnames, self.gdp,
                                       country1 = "Austria",
                                       country2 = "Norway",
                                       country3 = "Albania",
                                       country4 = "Belgium")
    def test_country_input(self):
        with self.assertRaises(ValueError):
            output_data = cd.clean_dataset(self.agrofood, self.gdp,
                                           country1 = random.randrange(1, 100),
                                           country2 = random.randrange(1, 100),
                                           country3 = random.randrange(1, 100),
                                           country4 = random.randrange(1, 100))
        with self.assertRaises(ValueError):
            output_data = cd.clean_dataset(self.agrofood, self.gdp,
                                           country1 = "Austria",
                                           country2 = "Norway",
                                           country3 = "Albania",
                                           country4 = "Afghanistan")
    
    def test_merge_cumsum(self):
        data2_long_subset = pd.melt(self.pd_gdp, id_vars=['Country'],
                                    var_name='Year', value_name='GDP')
        self.assertEqual(len(data2_long_subset), 292)
        data2_long_subset['Year']=data2_long_subset['Year'].astype(int)
        merged_data = pd.merge(pd.read_csv(self.agrofood), data2_long_subset,
                           left_on=['Area','Year'], right_on=['Country','Year'], how="inner")
        self.assertEqual(len(merged_data), 55)
        merged_data['cumulative_emission'] = merged_data.groupby('Area')['total_emission'].cumsum()
        merged_Belgium_subset = merged_data[merged_data['Area'] == 'Belgium']
        cumsum_value = merged_Belgium_subset['cumulative_emission'].iloc[-1]
        Belgium_subset = merged_data[merged_data['Area'] == 'Belgium']
        subset_sum = Belgium_subset['total_emission'].sum()
        self.assertAlmostEqual(cumsum_value, subset_sum)


class Test_plot_data(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.data_notpd = {'Area': ['Country1', 'Country2', 'Country3', 'Country4'],
                'Year': [2020, 2021, 2022, 2023],
                'GDP': [1, 2, 3, 4],
                'Average Temperature °C': [25.5, 26.0, 24.8, 27.0],
                'total_emission': [100, 120, 90, 20],
                'cumulative_emission': [100, 220, 310, 330]}
        self.df = pd.DataFrame(self.data_notpd)
        data_wrongcolname = {'Country': ['Country1', 'Country2', 'Country3', 'Country4'],
                'Time_wrong': [2020, 2021, 2022, 2023],
                'GDP_wrong': [1, 2, 3, 4],
                'Average Temperature_wrong': [25.5, 26.0, 24.8, 27.0],
                'total_emission_wrong': [100, 120, 90, 20],
                'cumulative_emission_wrong': [100, 220, 310, 330]}
        self.df_wrongcolname = pd.DataFrame(data_wrongcolname)
        cd.plot_data(self.df,
                  country1 = "Country1",
                  country2 = "Country2",
                  country3 = "Country3",
                  country4 = "Country4",
                  out_path = "../data/test_png_creation.png")
    
    @classmethod
    def tearDown(self):
        os.remove("../data/test_png_creation.png")

    def test_pd_input(self):
        with self.assertRaises(TypeError):
            output_data = cd.plot_data(self.data_notpd,
                                       country1 = "Country1",
                                       country2 = "Country2",
                                       country3 = "Country3",
                                       country4 = "Country4")
        
    def test_col_names(self):
        with self.assertRaises(ValueError):
            output_data = cd.plot_data(self.df_wrongcolname,
                                       country1 = "Country1",
                                       country2 = "Country2",
                                       country3 = "Country3",
                                       country4 = "Country4")

    def test_country_input(self):
        with self.assertRaises(ValueError):
            output_data = cd.plot_data(self.df,
                                           country1 = random.randrange(1, 100),
                                           country2 = random.randrange(1, 100),
                                           country3 = random.randrange(1, 100),
                                           country4 = random.randrange(1, 100))
    
    def test_out_path(self):
        with self.assertRaises(SystemExit):
            cd.plot_data(self.df,
                         country1 = "Country1",
                         country2 = "Country2",
                         country3 = "Country3",
                         country4 = "Country4",
                         out_path = "../wrongpath/test_png_creation.png")
        with self.assertRaises(ValueError):
            cd.plot_data(self.df,
                         country1 = "Country1",
                         country2 = "Country2",
                         country3 = "Country3",
                         country4 = "Country4",
                         out_path = "../wrongpath/test_png_creation.pdf")

    def test_output_fig(self):
        self.assertTrue(os.path.exists("../data/test_png_creation.png"))




