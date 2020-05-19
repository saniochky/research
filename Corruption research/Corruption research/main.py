import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import geopandas as gpd
from config import DEVELOPING_COUNTRIES, QUANDL, ISO, QUANDL_YEARS
from get_data import GetData

cpi_table = None


def cpi_info(country, year):
    """
    Gets information about CPI in specific country in specific year
    :param country: str
    :param year: str
    :return: (str, None)
    """
    value = np.nan

    if country in DEVELOPING_COUNTRIES:
        value = cpi_table[country][cpi_table['Country'].index(year)]
        if type(value) == str:
            value = float(value)

    return value


def get_year(country, index):
    """
    Gets information about available years to get data
    for specific country
    :param country: str
    :param index: int
    :return: list
    """
    return GetData().get_quandl_year(country, index)


def get_data(country, index, year):
    """
    Gets required data about a specific country/countries in a specific year
    :param index: str
    :param country: (str, list)
    :param year: str
    :return: (str, list, None)
    """
    # Define variables
    error = "Sorry, there is not data about this country this year"
    data = None

    # Define what type of data should be displayed
    # Single data
    if type(country) == str:
        if index == '1':
            data = cpi_info(country, year)
        else:
            data = GetData(country, int(index), year).export_data()

        # Display data
        if data is None:
            print('\n')
            print(error)
        else:
            print('\n')
            print('\\' * (len(str(data)) + 10))
            print('\\' * 4, str(data), '\\' * 4)
            print('\\' * (len(str(data)) + 10))

    # Visualize data about all countries
    elif country == DEVELOPING_COUNTRIES:
        print('\nPlease wait up to two minutes...')
        visualize_map(create_dataframe(index, year), index, year)

    # Visualize data about specific countries
    else:
        print('\nPlease wait few seconds...')
        visualize_bar(country, index, year)


def visualize_bar(countries, index, year):
    """
    Visualizes Cdata about several countries as a bar plot
    :param countries: list
    :param index: str
    :param year: str
    :return: None
    """
    # define variables
    if index == '1':
        description = 'The Corruption Perceptions Index (CPI) is an index published annually by ' \
                      'Transparency International since 1995, which ranks countries \n"by their ' \
                      'perceived levels of public sector corruption, as determined by expert ' \
                      'assessments and opinion surveys"  • Author: Oleksandr Dubas'
        title = f'CPI in {year}'
    else:
        description = 'The information is provided by Quandl • https://www.quandl.com/ • Author: Oleksandr Dubas'
        title = f'{QUANDL[int(index)]} in {year}'

    # Make list of available data
    if countries:
        values = []
        objects = []
        for country in countries:
            if index == '1':
                value = cpi_info(country, year)
            else:
                value = GetData(country, int(index), year).export_data()

            if value is not None:
                objects.append(country.upper())
                values.append(value)

        # Create bar plot if data exists
        if objects:
            y_pos = np.arange(len(objects))

            plt.barh(y_pos, values, align='center', alpha=1)
            plt.yticks(y_pos, objects)
            plt.xlabel(description)
            plt.title(title)

            for i, v in enumerate(values):
                plt.text(v, i, str(v))

            # Display bar plot
            plt.show()

        # Print massage if there is no available data
        else:
            print("There is no information about these countries this year")
    else:
        print("There is no information about these countries this year")


def create_dataframe(index, year):
    """
    Creates pandas dataframe that will be used in visualization
    :param index: str
    :param year: str
    :return: dataframe
    """
    # Define variables
    data = {
        'Country Name': [],
        'Country Code': [],
        year: []
    }

    # Create datafreme
    for country in ISO:
        if index == '1':
            value = cpi_info(country, year)
        else:
            value = GetData(country, int(index), year).export_data()
            if value is None:
                value = np.nan
        data['Country Name'].append(country)
        data['Country Code'].append(ISO[country])
        data[year].append(value)

    df = pd.DataFrame(data, columns=['Country Name', 'Country Code', year])

    return df


def visualize_map(df, index, year):
    """
    Visualizes data about all countries on a map
    :param df: dataframe
    :param index: str
    :param year: str
    :return:
    """
    # Define variables
    shapefile = 'ne_10m_admin_0_countries_lakes.shp'
    colors = 10
    cmap = 'OrRd'
    figsize = (16, 10)
    if index == '1':
        title = f'CPI in {year}'
        description = 'The Corruption Perceptions Index (CPI) is an index published annually by ' \
                      'Transparency International since 1995, which ranks countries \n"by their ' \
                      'perceived levels of public sector corruption, as determined by expert ' \
                      'assessments and opinion surveys"  • Author: Oleksandr Dubas'
    else:
        title = f'{QUANDL[int(index)]} in {year}'
        description = 'The information is provided by Quandl • https://www.quandl.com/ • Author: Oleksandr Dubas'

    # Create geopandas dataframe
    gdf = gpd.read_file(shapefile)[['ADM0_A3', 'geometry']].to_crs('+proj=robin')

    # Merge both data frames
    merged = gdf.merge(df, left_on='ADM0_A3', right_on='Country Code')

    # Create a map using matplotlib
    ax = merged.dropna().plot(column=year, cmap=cmap, figsize=figsize,
                              scheme='quantiles', k=colors, legend=True, edgecolor='black')

    merged[merged.isna().any(axis=1)].plot(ax=ax, color='lightgrey', hatch='///', edgecolor="black")

    ax.set_title(title, fontdict={'fontsize': 20}, loc='left')
    ax.annotate(description, xy=(0.1, 0.1), size=12, xycoords='figure fraction')

    ax.set_axis_off()
    ax.set_xlim([-1.5e7, 1.7e7])
    ax.get_legend().set_bbox_to_anchor((.12, .4))

    # Display map
    plt.show()


def first_choose():
    """
    Lets the user choose the type of information he wats to get
    :return: str
    """
    # Define variables
    user_choice = None
    available_choices = ['1', '2']
    text = '\nWould you like to know information about separate country \n' \
           'or visualize some information about two or more? \n' \
           'Type \'1\' or \'2\': '

    # Get user`s choice
    while user_choice not in available_choices:
        user_choice = input(text)

    return user_choice


def second_choose():
    """
    Lets the user choose what information he wants to get
    :return: str
    """
    # Define variables
    user_choice = None
    available_choices = [str(x) for x in range(1, 9)]
    text = '\nWhat information you would like to know? \n' \
           f'1. {QUANDL[1]}\n' \
           f'2. {QUANDL[2]}\n' \
           f'3. {QUANDL[3]}\n' \
           f'4. {QUANDL[4]}\n' \
           f'5. {QUANDL[5]}\n' \
           f'6. {QUANDL[6]}\n' \
           f'7. {QUANDL[7]}\n' \
           f'8. {QUANDL[8]}\n'
    repeat = '\nType number from 1 to 8: '

    print(text)

    # Get user`s choice
    while user_choice not in available_choices:
        user_choice = input(repeat)

    return user_choice


def third_choose(mode):
    """
    Lets the user choose what country/countries he wants to get information about
    :param mode: str
    :return: (str, list)
    """
    # Define variables
    user_choice = ''
    countries = []
    available_choices = DEVELOPING_COUNTRIES.copy()
    text_1 = '\nType a country you would like to know about: '
    text_2 = '\nType countries you would like to know about one by one. \n' \
             'When finished just type \'proceed\' \n' \
             'If you want choose all countries, type \'all\' \n'
    repeat = 'Done! What next? '
    error = 'Sorry, there is not information about this country. Try again: '

    # Define whether choose one country or many
    if mode == 1:

        # Get user`s choice
        while user_choice.lower() not in available_choices:
            user_choice = input(text_1)

        return user_choice.lower()

    elif mode == 2:

        # Get user`s choice
        user_choice = input(text_2)

        while user_choice.lower() != 'all' and user_choice.lower() != 'proceed':
            if user_choice.lower() not in available_choices:
                user_choice = input(error)
            else:
                if user_choice.lower() not in countries:
                    countries.append(user_choice.lower())
                user_choice = input(repeat)

        if user_choice == 'all':
            return available_choices
        else:
            if len(countries) > 1:
                return countries
            else:
                print('You have chosen not enough countries \n')
                third_choose(mode)


def fourth_choose(country, index):
    """
    Lets the user choose what year he wants to get information about
    :param country: (str, list)
    :param index: (str)
    :return: str
    """
    # Define variables
    user_choice = None
    error = 'Sorry, there is no available data for this country'

    # Define the available choices
    if index == '1':
        available_choices = [str(x) for x in range(1995, 2019)]
        text = '\nChoose a year between 1995 and 2018: '
    else:
        if type(country) == str:
            value = get_year(country, int(index))
            available_choices = [x for x in value]
            text = f'\nChoose a year. Available years: {" ".join(available_choices)} \n'
        else:
            if country == DEVELOPING_COUNTRIES:
                available_choices = QUANDL_YEARS[int(index)]
                if available_choices:
                    text = f'\nChoose a year. Available years: {" ".join(available_choices)} \n' \
                           '(The first available year has least data, the last one has the most): '
            else:
                # Get available years to show data
                years_dict = {}

                for c in country:
                    value = GetData().get_quandl_year(c, int(index))
                    for year in value:
                        if year in years_dict:
                            years_dict[year] += 1
                        else:
                            years_dict[year] = 1

                available_choices = [x for x in years_dict]
                if available_choices:
                    available_choices = sorted(available_choices, key=lambda x: years_dict[x])
                    text = f'\nChoose a year. Available years: {" ".join(available_choices)} \n' \
                           '(The first available year has least data, the last one has the most): '

    # Get user`s choice
    if available_choices:
        if type(country) == list:
            print('\nNOTE: Information about some countries may not be shown.\n'
                  'It means that data is missing in the source.')
        while user_choice not in available_choices:
            user_choice = input(text)
    else:
        print(error)

    return user_choice


def main():
    """
    Main function to interact with user
    :return: (str, None)
    """
    # Define variables
    intro = "\nThis program is made to help in researching about \n" \
            "Corruption in Developing countries in comparison with Ukraine \n"
    note = "The list of all available countries is in config.py \n" \
           "Some information about specific countries or specific years \n" \
           "May be missing"

    # Print start information
    print(intro)
    print('NOTE \n')
    print(note)

    # Create CPI table
    global cpi_table
    cpi_table = GetData().get_cpi_table()

    # Make screenplay
    def screenplay():
        repeat = None
        choice = '\nWould you like to know something more (y/n)? '
        mode = first_choose()
        sort = second_choose()
        country = third_choose(int(mode))
        year = fourth_choose(country, sort)
        if year:
            get_data(country, sort, year)

        while repeat != 'y' and repeat != 'n':
            repeat = input(choice)

        if repeat == 'y':
            screenplay()

    # Start
    screenplay()


if __name__ == '__main__':
    main()
