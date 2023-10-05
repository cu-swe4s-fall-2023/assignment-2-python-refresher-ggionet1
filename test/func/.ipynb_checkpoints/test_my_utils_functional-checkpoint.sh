test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run basic_add python3 src/get_column_project/print_fires.py --file_name 'test/data/test_func_sampledataset.txt' --query_column 0 --query_value "China" --result_column 3 --summary "mean"
assert_stdout
assert_exit_code 0

run basic_add python3 src/get_column_project/print_fires.py --file_name 'test/data/test_func_sampledataset.txt' --query_column 0 --query_value "China" --result_column 41 --summary "mean" 
assert_exit_code 1

run basic_add python3 src/get_column_project/print_fires.py --file_name 'test/data/test_func_sampledataset.txt' --query_column 0 --query_value "China" --result_column 3 --summary "median" 
assert_stdout
assert_exit_code 0

run basic_add python3 src/get_column_project/print_fires.py --file_name 'test/data/test_func_sampledataset.txt' --query_column "Not_correct_value" --query_value "China" --result_column 3 --summary "median" 
assert_exit_code 1

run basic_add python3 src/get_column_project/print_fires.py --file_name 'test/data/test_func_sampledataset.txt' --query_column 0 --query_value "China" --result_column 3 --summary "std_dev" 
assert_stdout
assert_exit_code 0

run basic_add python3 src/get_column_project/print_fires.py --file_name 'test/data/test_func_sampledataset.txt' --query_column 0 --query_value "China" --result_column 0 --summary "median" 
assert_exit_code 1

