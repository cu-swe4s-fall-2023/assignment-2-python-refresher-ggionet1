# Assignment 9
Pandas and MatPlotLib


## Scientific Presentation

### Introduction

This code is dedicated to my dear Uncle John. Uncle John, I know we've had our disagreements before, so I thought I'd compile the following data for you to demonstrate the effects of climate change. Since you live in North America, all of my data is relevant to North American countries (United States, Canada, Guatemala, and Mexico). 

I prepared the following graphs:
1. A plot of year vs. average temperature
2. A scatter plot of total emissions by year
3. A plot of GDP vs total emissions, colored by year, with data from North American countries
4. A plot of the cumulative emissions in Mexico by average yearly temperature


### Methods

Our functions were developed using the pandas and matplotlib libraries.

We used a function, clean_data() to extract the information we needed in the following steps:
1. Using a document containing emissions data from countries around the world, we selected data from 4 separate countries. 
2. We then extracted gdp data from the countries in question
3. We merged the gdp and emissions data 
4. We output a .csv file containing the merged dataset

Then, we used a function called make_plot() to create a 4-panel plot from the prepared .csv file.
A snakefile was prepared to make our pipeline reproducible.

### Results

![Panel Plot](doc/Panel_Plot.png?raw=true "Climate Change Plots for Uncle John")

1. A plot of year vs. average temperature
    In this plot, you can see a general trend that the average temperature is increasing over time. This directly demonstrates climate change, as we are seeing an increase over time in average temperature across several different countries.
    You will notice that the trend is much more dramatic and unstable in Canada. This represents how the poles are experiencing climate change earlier than countries closer to the equator.

2. A scatter plot of total emissions by year
    The total emissions per year flunctuates, but since 1990 has overall increased. This plot demonstrates the importance that the United States plays on the global stage when it comes to curbing emissions; it emits the most compared to any other country in North America. In fact, it is hard to even distinguish the change in Guatemala's emissions when plotted on the same axis as the United States' emissions, because the United States emits so much. This indicates the importance of pro-climate change policy in the United States specifically, and how stopping global climate change is part of our responsibility as individuals living in the U.S.

3. A plot of GDP vs total emissions
    This plot demonstrates that, over time, GDP has increased and so have total emissions. However, high GDPs have been obtained in the past with low emissions, demonstrating that it is possible to have economic success while also emitting lower amounts of CO2. We shouldn't think of climate change as being against the economy, but rather that fighting emissions and supporting the economy can be two tasks that go hand-in-hand.
    
4. A plot of the cumulative emissions in Mexico by average yearly temperature
    This plot of Mexico demonstrates a strong positive correlation between cumulative emissions and average yearly temperature. Although it doesn't prove causation, this plot shows that there is a strong relationship between cumulative emissions and average yearly temperature.
    
If I could have any data, I would summarize the cumulative total emissions from all countries, and map this to the total C02 in the air. I would then compare total CO2 in the air to the change in average yearly temperature for countries near the poles, in temperate regions, and near the equator. I would want to compare these countries in groups because I would want to demonstrate how climate change is distributed across the globe.

I would also want to demonstrate the warming of the oceans, as land temperature is highly dependent on elevation and ecosystems (for ex. urban areas are experiencing warming at a much faster rate than forested areas). I would like to collect data from oceans across the globe and measure the surface temperature, then map the change in yearly temperature over time in comparison to the total CO2 in the air.

Lastly, because correlation does not equal causation, I would like to have data which demonstrates what happens when humans take action to reduce their emissions. I would use chloro-fluorocarbons as a test case, demonstrating emissions of CFCs world-wide by year and the overall square area of ozone holes in the atmosphere.

## Language
This code is writen in python, with an additional snakemake pipeline.

## Purpose of the project
The goal is to demonstrate how GDP, emissions, and average yearly temperature are related.
The plots created in this project provide evidence of man-made climate change.

This software can also be used to generate other plots from CSV files.

**UsingLibraries/src/collect_data.py** 
Creates a clean_data function and a make_scatter function

**UsingLibraries/src/make_plot.py** 
Calls the get_fire_gdp_year_data() function and make_scatter() function.

**.github/workflows/test.yml***
Is a file specifying when to run continuous integration functional and unit testing.

**UsingLibraries/src/snakemake/snakefile***
Is a snakefile which will generate a four-panel plot for specified countries.

## How to install the software
1. Verify that you have python3. If you do not have python, you can install it using the instructions [here](https://www.python.org/downloads/)

2. Download desired dataset. Our team worked with Agrofood_co2_emissions.csv and IMF_GDP.csv, which can be found in the course google drive. Place in the source directory.

3. Install software: you will need to clone the repository and open it in your local environment. In your terminal, type:

```
git clone git@github.com:cu-swe4s-fall-2023/assignment-8-searching-and-test-driven-development-ggionet1
cd assignment-8-searching-and-test-driven-development-ggionet1

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

Here is an example of how to run the data within your terminal, assuming you are already in the UsingLibraries folder.

```
python3 src/plot_data.py --dataset1 "doc/Agrofood_co2_emission.csv" --dataset2 "doc/IMF_GDP.csv" --country1 'United States of America' --country2 'Mexico' --country3 'Canada' --country4 'Guatemala' --out_path "doc/Panel_Plot.png"
```

If you would like to generate multiple plots or would like to reproduce the plot in this readme, I recommend you use the snakefile located in the src folder. After downloading snakemake, you can run the snakefile with the following code from within the UsingLibraries folder:

```
snakemake --snakefile src/snakemake/snakefile -c -1
```


To run tests on each individual function, in terminal, run this file like so:
```
cd test/unit
python3 -m unittest test/unit/test_collect_data.py

```

To run a test on the overall functionality of this code, run this file like so from the UsingLibraries folder:
```
bash test/func/test_plot_data.py
```

## Change Log
