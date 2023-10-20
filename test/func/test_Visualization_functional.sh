test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run basic_add python3 src/workflow/snakemake/fire/Visualization.py --file_name 'test/data/test_viz_sampledataset.txt' --query_column 0 --query_value "Brazil" --result_column 3 --graph_title "Number of Forest Fires in Brazil" --out_graph 'test/func/Brazil_sample.png'
assert_equal $'test/func/Brazil_sample.png' $( ls $'test/func/Brazil_sample.png' )
assert_exit_code 0

run basic_add python3 src/workflow/snakemake/fire/Visualization.py --file_name 'test/data/test_viz_sampledataset.txt' --query_column 0 --query_value "Germany" --result_column 3 --graph_title "Number of Forest Fires in Germany" --out_graph 'test/func/Germany_sample.png'
assert_equal $'test/func/Germany_sample.png' $( ls $'test/func/Germany_sample.png' )
assert_exit_code 0

run basic_add python3 src/workflow/snakemake/fire/Visualization.py --file_name 'test/data/test_viz_sampledataset.txt' --query_column 0 --query_value "Germany" --result_column 41 --graph_title "Number of Forest Fires in Germany" --out_graph 'test/func/Germany_sample.png'
assert_exit_code 1

run basic_add python3 src/workflow/snakemake/fire/Visualization.py --file_name 'test/data/test_viz_sampledataset.txt' --query_column 0 --query_value "Russia" --result_column 3 --graph_title "Number of Forest Fires in Russia" --out_graph 'test/func/Russia_sample.png'
assert_exit_code 1
