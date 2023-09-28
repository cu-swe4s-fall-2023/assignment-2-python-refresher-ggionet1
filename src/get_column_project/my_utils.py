import sys

def get_column(file_name, query_column, query_value, result_column=1):
    """Output a list with a subset of values from the result column
    List is subset to when value in a query column matches the desired value.

    Parameters
    ----------
    file_name: a file with a .csv extension
        File containing a search (query) column and a result column
    query_column: int
        Integer is the column index where search column is located in the file
    query_value: value with same datatype as the datatype of the query column
        Represents the desired value you want to search for in the query_column
    results_column: int
        Integer is the column index where results are held in the file

    Returns
    -------
    fire_list
        A subset list of values from the results column
        Subset to when query_value equals value in query_column for a given row
    """
    fire_list = []
    try:
        f = open(file_name, 'r')
    except FileNotFoundError:
        print('Could not find ' + file_name)
        sys.exit(1)
    try:
        query_column = int(query_column)
    except TypeError:
        print("Value for query_column is not an integer")
        sys.exit(1)
    try:
        result_column = int(result_column)
    except TypeError:
        print("Value for result_column is not an integer")
        sys.exit(1)
    for line in f:
        row = line.rstrip().split(',')
        try:
            selected_column = row[query_column]
        except IndexError:
            print("Index out of range for query_column.")
            sys.exit(1)
        try:
            result = row[result_column]
        except IndexError:
            print("Index out of range for result_column.")
            sys.exit(1)
        if selected_column == query_value:
            fire_list.append(result)
    f.close()
    return fire_list
