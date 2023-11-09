import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def clean_dataset(dataset1, dataset2,
                  country1, country2,
                  country3, country4,
                  out_path_data=None):
    """Output is a .csv file
    The file contains merged dataset made from dataset1 and dataset2
    The merged dataset is subset so that the column 'Area'
        contains only values in input_list

    Parameters
    ----------
    dataset1: a file with a .csv extension
        File containing a column 'Area' for countries,
        'Year', 'Average Temperature °C', and 'total_emission'
    dataset2: a file with a .csv extension
        File in wide format containing columns "Country",
        and column with years,
        year columns containing GDP data.
    country1:
        name of a country you are interested in
    country2:
        name of a country you are interested in
    country3:
        name of a country you are interested in
    country4:
        name of a country you are interested in
    out_path_data: the file path to output the dataset
        Must end in .csv

    Returns
    -------
    .csv file ready for plotting
    """
    try:
        data1_subset = pd.read_csv(dataset1)
    except FileNotFoundError:
        print("dataset1 file not found. Please check your path.")
        sys.exit(1)
    except pd.errors.EmptyDataError:
        print("dataset1 is empty")
        sys.exit(1)
    try:
        data2_wide = pd.read_csv(dataset2)
    except FileNotFoundError:
        print("dataset2 file not found. Please check your path.")
        sys.exit(1)
    except pd.errors.EmptyDataError:
        print("dataset2 is empty")
        sys.exit(1)
    countries = [str(country1), str(country2), str(country3), str(country4)]
    necessary_d1_columns = ['Area', 'Year', 'total_emission']
    for colname in necessary_d1_columns:
        if colname not in data1_subset.columns:
            raise ValueError(f"{colname} not a column in dataset1")
            sys.exit(1)
        else:
            continue
    if "Country" not in data2_wide.columns:
        raise ValueError(f"Country not a column in dataset2")
        sys.exit(1)
    data1_subset['Year'] = data1_subset['Year'].astype(int)
    for country in countries:
        if country not in data2_wide['Country'].values:
            raise ValueError(f"{country} not in dataset2")
            sys.exit(1)
        elif country not in data1_subset['Area'].values:
            raise ValueError(f"{country} not in dataset1")
            sys.exit(1)
        else:
            continue
    data2_wide_subset = data2_wide.loc[data2_wide['Country'].isin(countries)]
    data2_long_subset = pd.melt(data2_wide_subset,
                                id_vars=['Country'],
                                var_name='Year',
                                value_name='GDP')
    try:
        data2_long_subset['Year'] = data2_long_subset['Year'].astype(int)
    except ValueError:
        print("Year column in dataset2 could not be converted to integers")
        sys.exit(1)
    data2_long_subset['GDP'] = data2_long_subset['GDP'].replace('...', np.nan)
    try:
        data2_long_subset['GDP'] = data2_long_subset['GDP'].str.replace(
            ',', '').astype(float)
    except ValueError:
        print("GDP values in dataset2 could not be converted to floats")
        sys.exit(1)
    merged_data = pd.merge(data1_subset,
                           data2_long_subset,
                           left_on=['Area', 'Year'],
                           right_on=['Country', 'Year'], how="inner")
    merged_data['cumulative_emission'] = merged_data.groupby(
        'Area')['total_emission'].cumsum()
    if out_path_data is not None:
        if isinstance(out_path_data, str) is False:
            raise ValueError("out_path must be a string")
            sys.exit(1)
        elif not out_path_data.endswith(".csv"):
            raise ValueError("out_path must end in .csv")
            sys.exit(1)
        try:
            merged_data.to_csv(out_path_data, index=False)
        except FileNotFoundError:
            print("Path not found for out_path")
            sys.exit(1)


def plot_data(dataset, country1,
              country2, country3,
              country4, out_path=None):
    """Output a four panel graph in a .png file

    Parameters
    ----------
    dataset: .csv file containing the following columns
        'Area' for countries,
        'Year'
        'GDP'
        'Average Temperature °C'
        'total_emission'
        'cumulative_emission'
    input_list: a list of countries
    out_path: the location where to store the .png file
        Must have a .png extension
    country1:
        name of a country you are interested in
    country2:
        name of a country you are interested in
    country3:
        name of a country you are interested in
    country4:
        name of a country you are interested in
    Returns
    -------
    a dataset ready for plotting
    """
    try:
        dataset_csv = pd.read_csv(dataset)
    except FileNotFoundError:
        print("dataset file not found. Please check your path.")
        sys.exit(1)

    necessary_df_columns = ['Area', 'Year', 'GDP', 'Average Temperature °C',
                            'total_emission', 'cumulative_emission']
    for colname in necessary_df_columns:
        if colname not in dataset_csv.columns:
            raise ValueError(f"{colname} not a column in dataset")
            sys.exit(1)
        else:
            continue

    input_list = [str(country1), str(country2), str(country3), str(country4)]
    for country in input_list:
        if country not in dataset_csv['Area'].values:
            raise ValueError(f"{country} not in dataset")
            sys.exit(1)

    fig, axes = plt.subplots(2, 2)
    fig.set_size_inches(10, 5)
    # Figure 1
    num_colors = len(input_list)
    colors = plt.cm.viridis(np.linspace(0, 1, num_colors))
    for i, country in enumerate(input_list):
        country_data = dataset_csv[dataset_csv['Area'] == country]
        axes[0, 0].plot(country_data['Year'],
                        country_data[f'Average Temperature °C'],
                        label=country, color=colors[i])
    axes[0, 0].set_xlabel('Year')
    axes[0, 0].set_ylabel('Average Temperature °C')
    axes[0, 0].set_title('Average Temperature by Year', loc='left')
    axes[0, 0].spines['top'].set_visible(False)
    axes[0, 0].spines['right'].set_visible(False)
    axes[0, 0].legend(fontsize=8, labelspacing=0.4)
    # Figure 2
    for i, country in enumerate(input_list):
        country_data = dataset_csv[dataset_csv['Area'] == country]
        axes[0, 1].scatter(country_data['Year'],
                           country_data['total_emission'],
                           label=country, color=colors[i])
    axes[0, 1].set_xlabel('Year')
    axes[0, 1].set_ylabel('Total Emission')
    axes[0, 1].set_title('Total CO2 Emission by Year')
    axes[0, 1].spines['top'].set_visible(False)
    axes[0, 1].spines['right'].set_visible(False)
    axes[0, 1].legend(fontsize=8, labelspacing=0.4)
    # Figure 3
    f3 = axes[1, 0].scatter(dataset_csv['GDP'],
                            dataset_csv['total_emission'],
                            c=dataset_csv['Year'],
                            cmap='viridis', s=10)
    plt.colorbar(f3, label='Year')
    axes[1, 0].set_xlabel('GDP Output')
    axes[1, 0].set_ylabel('Emission Output')
    axes[1, 0].set_title('GDP Output and Emissions Output')
    axes[1, 0].spines['top'].set_visible(False)
    axes[1, 0].spines['right'].set_visible(False)
    # Figure 4
    country_data_f4 = dataset_csv[dataset_csv['Area'] == country2]
    axes[1, 1].scatter(country_data_f4['cumulative_emission'],
                       country_data_f4[f'Average Temperature °C'],
                       label=input_list[1], color=colors[1])
    axes[1, 1].set_xlabel('Cumulative Emissions')
    axes[1, 1].set_ylabel('Avg Temperature °C')
    axes[1, 1].set_title(
        f"Cumulative Emissions and Avg. Temp. in {country2}", )
    axes[1, 1].spines['top'].set_visible(False)
    axes[1, 1].spines['right'].set_visible(False)

    for i, ax in enumerate(axes.ravel()):
        ax.text(-0.1, 1.1, f'({chr(97 + i)})',
                transform=ax.transAxes, size=12, weight='bold')

    plt.tight_layout()
    plt.show()
    if out_path is not None:
        if isinstance(out_path, str) is False:
            raise ValueError("out_path must be a string")
            sys.exit(1)
        elif not out_path.endswith(".png"):
            raise ValueError("out_path must end in .png")
            sys.exit(1)
        try:
            plt.savefig(out_path, dpi=100)
        except FileNotFoundError:
            print("Path not found for out_path")
            sys.exit(1)
