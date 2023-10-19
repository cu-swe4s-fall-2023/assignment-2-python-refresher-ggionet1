import argparse
import sys
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
sys.path.insert(0, 'src/get_column_project')  # noqa
import my_utils  # noqa


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
    parser.add_argument('--graph_title',
                        help='The title of the graph', type=str, required=True)
    parser.add_argument('--out_graph',
                        help='Name of output graph file with. .png extension',
                        type=str, required=True)
    args = parser.parse_args()
    return args


def main():
    args = get_args()
    file_name = str(args.file_name)
    query_column = int(args.query_column)
    query_value = args.query_value
    result_column = int(args.result_column)
    outgraph = args.out_graph
    x = "Forest Fires"
    y = "Frequency"
    title = str(args.graph_title)
    t = my_utils.get_column(file_name, query_column,
                            query_value, result_column)
    float_list = list(map(float, t))
    sorted_fire_list = sorted(float_list)
    n, bins, patches = plt.hist(sorted_fire_list, bins=5, edgecolor='black')
    plt.xticks(bins)
    plt.xticks(fontsize=8)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(title)
    plt.savefig(outgraph, bbox_inches='tight')


if __name__ == '__main__':
    main()
