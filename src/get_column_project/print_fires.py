from my_utils import get_column
import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file_name', type=str,
                        help='Name of the file', required=True)
    parser.add_argument('--query_column', type=int,
                        help='The index of column to search', required=True)
    parser.add_argument('--query_value',
                        help='The value to search for in query_column',
                        required=True)
    parser.add_argument('--result_column', type=int,
                        help='The index of column containing desired results',
                        required=True)
    args = parser.parse_args()
    return args


def main():
    args = get_args()
    file_name = str(args.file_name)
    query_column = int(args.query_column)
    query_value = args.query_value
    result_column = int(args.result_column)
    d = get_column(file_name, query_column, query_value, result_column)
    print(d)


if __name__ == '__main__':
    main()
