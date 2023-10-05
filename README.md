# Assignment 3

## Language
This code is writen in python, with an execution file (run.sh) in bash.

## Purpose of the project
The goal was to extract information about the number of fires
in a given country according to our data and output a given summary if requested.
The summaries available are mean, median, and standard deviation (std_dev).

This software can also be used to search through any csv
to output values from a desired column, 
conditionally based on the values from another column in the dataset.

**my_utils.py** 
Creates a function which can extract values from a column conditionally,
based on a condition set for a different column.

Also creates summary functions to find mean, median, or std_dev.

**print_fires.py** 
Calls the get_column function and makes use of the mean, median, or std_dev functions.

**run.sh** 
Is a file where which specifies which file to read
and what data to extract, based on a specified condition, and what summary function to run.

## How to install the software
1. Verify that you have python3. If you do not have python, you can install it using the instructions [here](https://www.python.org/downloads/)

2. Download desired dataset. Our team worked with Agrofood_co2_emissions.csv, which can be found in the course google drive. Place in the source directory.

3. Install software: you will need to clone the repository and open it in your local environment. In your terminal, type:

```
git clone git@github.com:cu-swe4s-fall-2023/assignment-2-python-refresher-ggionet1
cd assignment-2-python-refresher-ggionet1

```

## How to Use
my_utils.py creates the get_column() function and does not need to be changed to extract data from .csv
    It also creates functions to summarize for mean, median, and standard deviation.
print_fires.py calls the get_column() function from my_utils and also does not need to be changed to extract data from .csv

To extract the column you desire, employ the get_column() function in the run.sh file. 

Within the get_column file, specify:
-file_name: this is the name of your file with an extension
-query_column: Provide an integer of the column index for the column you want to conditionally search
-query_value: Provide a value matching the datatype of the query_column, to search for within the query_column
-result_column: Provide an integer of the column index for the column whose values you want to print

As an example in the run.sh file to print the outcomes of the 3rd indexed column if the 0th column is equal to "United States of America" from the Agrofood_co2_emission.csv file":

```
python3 print_fires.py --file_name 'Agrofood_co2_emission.csv' --query_column 0 --query_value "United States of America" --result_column 3
```

After this, run the run.sh file in the terminal like so:
```
bash run.sh
```

To run tests on each individual function, go to the tests folder and unit subfolder. While is folder, in terminal, run this file like so:
```
python3 -m unittest test_my_utils.py
```

To run a test on the overall functionality of this code, go to main directory. 
You can do this by typing in terminal until you get back to the main:
```
cd ..
```

Once there in terminal, run this file like so:
```
bash test/func/test_my_utils_functional.sh
```

## Change Log
-HW2 Files created
-HW3 Files updated to adhere to best practices
-HW4 my_utils.py updated to create summarizing functions. 
    print_fires.py was updated to make use of the summarizing functions within get_column()
    Functional and unit tests created and added into repository.
