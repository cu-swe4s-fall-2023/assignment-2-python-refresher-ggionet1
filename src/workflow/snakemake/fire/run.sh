#!/bin/bash

set -e # stop on error
set -u # raise error if variable is unset
set -o pipefail # fail if any prior step failed

python3 src/workflow/snakemake/fire/Visualization.py --file_name 'src/workflow/snakemake/fire/Agrofood_co2_emission.csv' --query_column 0 --query_value "Cuba" --result_column 3 --graph_title "Number of Forest Fires in Cuba" --out_graph "doc/Cuba.png"

python3 src/workflow/snakemake/fire/Visualization.py --file_name 'src/workflow/snakemake/fire/Agrofood_co2_emission.csv' --query_column 0 --query_value "Germany" --result_column 3 --graph_title "Number of Forest Fires in Germany" --out_graph "doc/Germany.png"

python3 src/workflow/snakemake/fire/Visualization.py --file_name 'src/workflow/snakemake/fire/Agrofood_co2_emission.csv' --query_column 0 --query_value "Brazil" --result_column 3 --graph_title "Number of Forest Fires in Brazil" --out_graph "doc/Brazil.png"