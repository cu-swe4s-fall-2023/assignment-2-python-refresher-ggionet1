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


def mean(input_list):
    """Output the mean of a list of floats or integers.

    Parameters
    -------
    input_list: a list of floats or integers

    Returns
    -------
    The mean of all values within the list

    """
    try:
        sum_list = sum(input_list)
    except TypeError:
        print("Datatype issue. Input should be list of integers or floats.")
        sys.exit(1)
    try:
        lst_avg = sum_list/len(input_list)
    except ZeroDivisionError:
        print("List is empty. Please input values to list.")
        sys.exit(1)
    return lst_avg


def median(input_list):
    """Output the mean of a list of floats or integers.

    Parameters
    ----------
    input_list: a list of floats or integers

    Returns
    -------
    The median of all values within the list
    """
    half = len(input_list)//2
    input_list.sort()
    try:
        type(input_list) == (float, int)
    except TypeError:
        print("Values in input list are not all integers or floats")
        sys.exit(1)
    try:
        if not len(input_list) % 2:
            return (input_list[half - 1] + input_list[half]) / 2
        elif len(input_list) % 2:
            return input_list[half]
    except IndexError:
        print("List is empty. Please input values to list.")
        sys.exit(1)


def std_dev(input_list):
    """Output the mean of a list of floats or integers.

    Parameters
    ----------
    input_list: a list of floats or integers

    Returns
    -------
    The standard deviation from all values within the list
    """
    samp_denom = len(input_list)-1
    try:
        sum_list = sum(input_list)
    except TypeError:
        print("Datatype issue. Input should be list of integers or floats.")
        sys.exit(1)
    try:
        lst_avg = sum_list/len(input_list)
    except ZeroDivisionError:
        print("List is empty. Please input values to list.")
        sys.exit(1)
    sample_min_mean_array = []
    for x in input_list:
        sample_min_mean = ((x-lst_avg)**2)
        sample_min_mean_array.append(sample_min_mean)
    sample_min_mean_sum = sum(sample_min_mean_array)
    std_dev_val = (sample_min_mean_sum/samp_denom)**.5
    return std_dev_val
