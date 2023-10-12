import my_utils
import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file_name', type=str,
                        help='Name of the file', required=True)
    parser.add_argument('--query_column',
                        help='The index of column to search', required=True)
    parser.add_argument('--query_value',
                        help='The value to search for in query_column',
                        required=True)
    parser.add_argument('--result_column',
                        help='The index of column containing desired results',
                        required=True)
    parser.add_argument('--summary',
                        help='The summary function (mean, median, std_dev)',
                        required=False, default=None)
    args = parser.parse_args()
    return args


def main():
    args = get_args()
    file_name = str(args.file_name)
    query_column = int(args.query_column)
    query_value = args.query_value
    result_column = int(args.result_column)
    t = my_utils.get_column(file_name, query_column,
                            query_value, result_column)
    d = []
    for i in t:
        d.append(float(i))
    summary_request = str(args.summary)
    if args.summary is None:
        return d
    elif summary_request == "mean":
        d_mean = my_utils.mean(d)
        print(d_mean)
    elif summary_request == "median":
        d_median = my_utils.median(d)
        print(d_median)
    elif summary_request == "std_dev":
        d_std_dev = my_utils.std_dev(d)
        print(d_std_dev)
    else:
        print("Please specify summary function as mean, median, or std_dev")
        sys.exit(1)


if __name__ == '__main__':
    main()
