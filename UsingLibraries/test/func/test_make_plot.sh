test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run basic_add python3 src/plot_data.py --dataset1 "test/data/agrofood_test_data.csv" --dataset2 "test/data/gdp_test_data.csv" --country1 'Austria' --country2 'Belgium' --country3 'Norway' --country4 'Albania' --out_path_data "test/data/merged_data.csv" --out_path "test/data/Panel_Plot.png"
assert_equal $'test/data/merged_data.csv' $( ls $'test/data/merged_data.csv' )
assert_equal $'test/data/Panel_Plot.png' $( ls $'test/data/Panel_Plot.png' )
assert_exit_code 0

run basic_add python3 src/plot_data.py --dataset1 "doc/doesntexist.csv" --dataset2 "test/data/gdp_test_data.csv" --country1 'Austria' --country2 'Belgium' --country3 'Norway' --country4 'Albania' --out_path_data "test/data/merged_data.csv" --out_path "test/data/Panel_Plot.png"
assert_exit_code 1

run basic_add python3 src/plot_data.py --dataset1 "test/data/agrofood_test_data.csv" --dataset2 "test/data/gdp_test_data.csv" --country1 'Austria' --country2 'Belgium' --country3 'Norway' --country4 'Albania' --country4 'NotInDatasets' --out_path_data "test/data/merged_data.csv" --out_path "test/data/Panel_Plot.png"
assert_exit_code 1

run basic_add python3 src/plot_data.py --dataset1 "test/data/agrofood_test_data.csv" --dataset2 "test/data/gdp_test_data.csv" --country1 'Austria' --country2 'Belgium' --country3 'Norway' --country4 'Afghanistan' --out_path_data "test/data/merged_data.csv" --out_path "test/data/Panel_Plot.png"
assert_exit_code 1

run basic_add python3 src/plot_data.py --dataset1 "test/data/agrofood_test_data_incorrectcol.csv" --dataset2 "test/data/gdp_test_data.csv" --country1 'Austria' --country2 'Belgium' --country3 'Norway' --country4 'Albania' --out_path_data "test/data/merged_data.csv" --out_path "test/data/Panel_Plot.png"
assert_exit_code 1

run basic_add python3 src/plot_data.py --dataset1 "test/data/agrofood_test_data_incorrectcol.csv" --dataset2 "test/data/gdp_test_data.csv" --country1 'Austria' --country2 'Belgium' --country3 'Norway' --country4 'Albania' --out_path_data "test/data/merged_data.wrongextension" --out_path "test/data/Panel_Plot.png"
assert_exit_code 1

run basic_add python3 src/plot_data.py --dataset1 "test/data/agrofood_test_data_incorrectcol.csv" --dataset2 "test/data/gdp_test_data.csv" --country1 'Austria' --country2 'Belgium' --country3 'Norway' --country4 'Albania' --out_path_data "test/data/merged_data.wrongextension" --out_path "test/data/notadirectory/Panel_Plot.png"
assert_exit_code 1
