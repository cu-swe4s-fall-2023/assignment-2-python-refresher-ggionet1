# Assignment 6

## Scientific Presentation

### Introduction

For this assignment, we were curious about the distribution of fires among countries of different land mass. We hypothesized that number of forest fires would correlate to the land mass within a given country, but that the overall distribution of forest fires by country would be the same.

We generated three plots, from a small, medium-sized, and large country to visualize the distribution of the number of yearly forest fires since 1992.

### Methods

Using a document containing fire data from countries around the world, we selected data from a given country using the get_column() function. In the Visualization.py file, we called this function and used this data to create a histogram for a given country. We ran a snakefile to create a histogram of one small country, one medium-sized country, and one large country.

### Results

![Cuba_fires](doc/Cuba.png?raw=true "Cuba Fires")
![Germany_fires](doc/Germany.png?raw=true "Germany Fires")
![Brazil_fires](doc/Brazil.png?raw=true "Brazil Fires")

We found that the distributions were not the same for all countries. Indeed, Germany, a medium-sized country, had much less forest fires than the other two countries.
We conclude that there are factors other than landmass (such as humidity or area of protected forest) which contribute to the number of forest fires per year.

## Language
This code is writen in python, with an execution file (run.sh) in bash.

## Purpose of the project
The goal was to extract information about the number of fires
in a given country according to our data and output a given summary if requested.
The summaries available are mean, median, and standard deviation (std_dev).

This software can also be used to search through any csv
to output values from a desired column, 
conditionally based on the values from another column in the dataset.

**src/get_column_project/my_utils.py** 
Creates a function which can extract values from a column conditionally,
based on a condition set for a different column.

Also creates summary functions to find mean, median, or std_dev.

**src/get_column_project/print_fires.py** 
Calls the get_column function and makes use of the mean, median, or std_dev functions.

**src/get_column_project/run.sh** 
Is a file where which specifies which file to read
and what data to extract, based on a specified condition, and what summary function to run.

**.github/workflows/test.yml***
Is a file specifying when to run continuous integration functional and unit testing.

**src/workflow/snakemake/fire/snakefile***
Is a snakefile which will generate histograms of fires for Brazil, Germany, and Cuba.

## How to install the software
1. Verify that you have python3. If you do not have python, you can install it using the instructions [here](https://www.python.org/downloads/)

2. Download desired dataset. Our team worked with Agrofood_co2_emissions.csv, which can be found in the course google drive. Place in the source directory.

3. Install software: you will need to clone the repository and open it in your local environment. In your terminal, type:

```
git clone git@github.com:cu-swe4s-fall-2023/assignment-2-python-refresher-ggionet1
cd assignment-2-python-refresher-ggionet1

```
4. To run the current code, unit tests, and functional tests using continuous integration, you will merely need to push any branch (```git push origin *branchname*```) or make a pull request (```git pull```) from the main.

5. a) To run the snakemake file, simply download snakemake:
```
mamba install -c bioconda snakemake
```


## How to Use
The code will automatically run whenever a branch is pushed with the following code 

```
git push origin *branchname*
```
or a pull request is made from the main:
```
git pull
``` 

Unit tests, functional tests, and python formatting will be tested if these events occur.

To personalize the code further, please read below:

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
If you would like to generate histograms, you will simply need to run the snakefile located in the src folder. You can run the snakefile with the following code:

```
snakemake --snakefile src/workflow/snakemake/fire/snakefile -c -1
```


To run tests on each individual function, in terminal, run this file like so:
```
python3 -m unittest test/unit/test_my_utils.py
```

To run a test on the overall functionality of this code, go to main directory. 
You can do this by typing in terminal until you get back to the main:
```
cd ..
```

Once there in terminal, run this file like so:
```
bash test/func/test_my_utils_functional.sh
bash test/func/test_Visualization_functional.sh

```


## Change Log
-HW2 Files created

-HW3 Files updated to adhere to best practices

-HW4 my_utils.py updated to create summarizing functions. 
    print_fires.py was updated to make use of the summarizing functions within get_column()
    Functional and unit tests created and added into repository.

-HW5 Added continuous integration file and workflow folder (Version 4).

-HW6 Added snakemake file and created histograms of forest fires.
