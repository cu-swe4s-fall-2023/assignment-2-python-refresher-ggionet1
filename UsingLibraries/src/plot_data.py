import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import collect_data as cd
import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset1', type=str,
                        help='Name of a .csv file in long format',
                        required=True)
    parser.add_argument('--dataset2',
                        help='Name of a .csv file in wide format',
                        required=True)
    parser.add_argument('--country1',
                        help='The first value to search for column "Area"',
                        required=True)
    parser.add_argument('--country2',
                        help='The first value to search for column "Area"',
                        required=True)
    parser.add_argument('--country3',
                        help='The first value to search for column "Area"',
                        required=True)
    parser.add_argument('--country4',
                        help='The first value to search for column "Area"',
                        required=True)
    parser.add_argument('--out_path',
                        help='A filepath ending in .png to save the graph',
                        required=True)
    args = parser.parse_args()
    return args


def main():
    args = get_args()
    dataset1_fires = args.dataset1
    dataset2_gdp = args.dataset2
    country1 = args.country1
    country2 = args.country2
    country3 = args.country3
    country4 = args.country4
    out_path_png = str(args.out_path)
    data_for_plot = cd.clean_dataset(dataset1_fires,
                                     dataset2_gdp, country1,
                                     country2, country3,
                                     country4)
    cd.plot_data(data_for_plot, country1,
                 country2, country3,
                 country4, out_path_png)


if __name__ == '__main__':
    main()