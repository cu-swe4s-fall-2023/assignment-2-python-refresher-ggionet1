#The purpose of this code is to generate an array containing information from the result column when a query column matches a specific value

#I did not specify what the query_value datatype should be so that this code worked for a wider variety of columns

#Columns should be specified by index (order within the file) rather than name

def get_column(file_name, query_column, query_value, result_column=1):
    fire_array = []
    f = open(file_name, 'r')
    for l in f:
        row = l.rstrip().split(',')
        selected_column = row[query_column]
        result = row[result_column]
        if selected_column == query_value:
            fire_array.append(result)

    f.close()
    print(fire_array)