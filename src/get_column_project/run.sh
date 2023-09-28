#!/bin/bash

set -e # stop on error
set -u # raise error if variable is unset
set -o pipefail # fail if any prior step failed

python3 print_fires.py --file_name 'Agrofood_co2_emission.csv' --query_column 0 --query_value "United States of America" --result_column 3
set +e
python3 print_fires.py --file_name 'Agrofood_co2_emission_wrong.csv' --query_column 0 --query_value "United States of America" --result_column 3
python3 print_fires.py --file_name 'Agrofood_co2_emission.csv' --query_column 0 --query_value "United States of America" --result_column 41
set -e
