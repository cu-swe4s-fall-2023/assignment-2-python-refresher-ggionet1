import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import collect_data as cd
import argparse


def get_args():
    parser = argparse.ArgumentParser()
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
    parser.add_argument('--dataset',
                        help='A filepath ending in .csv with merged data',
                        required=True)
    parser.add_argument('--out_path',
                        help='A filepath ending in .png to save the graph',
                        required=True)
    args = parser.parse_args()
    return args


def main():
    args = get_args()
    country1 = args.country1
    country2 = args.country2
    country3 = args.country3
    country4 = args.country4
    data_csv = str(args.dataset)
    out_path_png = str(args.out_path)
    cd.plot_data(data_csv, country1,
                 country2, country3,
                 country4, out_path_png)


if __name__ == '__main__':
    main()
