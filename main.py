import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import geopandas as gpd
import slug
from config import DEVELOPING_COUNTRIES, QUANDL, ISO
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


# ////*************---------------//////
# 456646657 ///////////******        ////-
# 2005647545149 9999+ ///////*+21313


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
    if type(country) == str:
        if index == '1':
            data = cpi_info(country, year)
        else:
            data = GetData(country, int(index), year)
            data = data.export_data()
    elif country == DEVELOPING_COUNTRIES:
        if index == '1':
            visualize_map_cpi(year)
        else:
            visualize_map_quandl(index, year)
    else:
        if index == '1':
            visualize_bar_cpi(country, year)
        else:
            visualize_bar_quandl(country, index, year)
            pass


def visualize_bar_cpi(countries, year):
    """

    :param countries:
    :param year:
    :return:
    """
    if countries:
        values = []
        objects = []
        for country in countries:
            value = cpi_info(country, year)
            if value is not None:
                objects.append(country.upper())
                values.append(value)

        if objects:
            y_pos = np.arange(len(objects))

            plt.barh(y_pos, values, align='center', alpha=1)
            plt.yticks(y_pos, objects)
            plt.xlabel('CPI')
            plt.title(f'CPI in {year} year')

            for i, v in enumerate(values):
                plt.text(v, i, str(v))

            plt.show()
        else:
            print("There is no information about these countries this year")
    else:
        print("There is no information about these countries this year")


def visualize_bar_quandl(countries, index, year):
    if countries:
        values = []
        objects = []
        for country in countries:
            value = GetData(country, int(index), year).export_data()
            if value is not None:
                objects.append(country.upper())
                values.append(float(value))

        if objects:
            y_pos = np.arange(len(objects))

            plt.barh(y_pos, values, align='center', alpha=1)
            plt.yticks(y_pos, objects)
            plt.xlabel(QUANDL[int(index)])
            plt.title(f'Year {year}')

            for i, v in enumerate(values):
                plt.text(v, i, str(v))

            plt.show()
        else:
            print("There is no information about these countries this year")
    else:
        print("There is no information about these countries this year")


def visualize_map_cpi(year):
    """

    :param year:
    :return:
    """
    shapefile = 'ne_10m_admin_0_countries_lakes.shp'
    colors = 10
    cmap = 'OrRd'
    figsize = (16, 10)
    cols = ['Country Name', 'Country Code', year]
    title = f'CPI in year {year}'

    description = '''
     The Corruption Perceptions Index (CPI) is an index published annually by Transparency International since 1995, which ranks countries
    "by their perceived levels of public sector corruption, as determined by expert assessments and opinion surveys"  • Author: Oleksandr Dubas'''.strip()

    gdf = gpd.read_file(shapefile)[['ADM0_A3', 'geometry']].to_crs('+proj=robin')

    data = {
        'Country Name': [],
        'Country Code': [],
        year: []
    }

    for country in ISO:
        value = cpi_info(country, year)
        data['Country Name'].append(country.upper())
        data['Country Code'].append(ISO[country])
        data[year].append(value)

    df = pd.DataFrame(data, columns=['Country Name', 'Country Code', year])

    merged = gdf.merge(df, left_on='ADM0_A3', right_on='Country Code')
    ax = merged.dropna().plot(column=year, cmap=cmap, figsize=figsize, scheme='quantiles', k=colors, legend=True, edgecolor='black')

    merged[merged.isna().any(axis=1)].plot(ax=ax, color='lightgrey', hatch='///', edgecolor="black")

    ax.set_title(title, fontdict={'fontsize': 20}, loc='left')
    ax.annotate(description, xy=(0.1, 0.1), size=12, xycoords='figure fraction')

    ax.set_axis_off()
    ax.set_xlim([-1.5e7, 1.7e7])
    ax.get_legend().set_bbox_to_anchor((.12, .4))

    plt.show()


def visualize_map_quandl(index, year):
    """

    :param index:
    :param year:
    :return:
    """
    pass


def first_choose():
    """
    Lets the user choose the type of information he wats to get
    :return: str
    """
    # Define variables
    user_choice = None
    available_choices = ['1', '2']
    text = 'Would you like to know information about separate country \n' \
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
    available_choices = ['1', '2', '3', '4', '5', '6', '7', '8']
    text = '\nWhat information you would like to know? \n' \
           '1. Corruption Perceptions Index (https://en.wikipedia.org/wiki/Corruption_Perceptions_Index)\n' \
           '2. Bribery index (% of gift or informal payment requests during public transactions) \n' \
           '3. Percent of firms choosing corruption as their biggest obstacle \n' \
           '4. Percent of firms expected to give gifts to public officials "to get things done" \n' \
           '5. Percent of firms expected to give gifts to secure government contract \n' \
           '6. Percent of firms identifying corruption as a major constraint \n' \
           '7. Percent of firms identifying the courts system as a major constraint \n' \
           '8. Value of gift expected to secure a government contract (% of contract value) \n'
    repeat = 'Type number from 1 to 8: '

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
    text_1 = 'Type a country you would like to know about: '
    text_2 = 'Type countries you would like to know about. (If you want choose all, type \'all\') \n' \
             'When finished just type \'proceed\' \n'
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
            if user_choice.lower() not in available_choices or user_choice.lower() in countries:
                user_choice = input(error)
            else:
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
    available_choices_1 = [str(x) for x in range(1995, 2019)]
    text_1 = 'Choose a year between 1995 and 2018: '

    # Define the available choices
    if index == '1':
        available_choices = available_choices_1
        text = text_1
    elif index != '1' and type(country) == str:
        available_choices = get_year(country, int(index))
        text = 'Choose a year. Available years: \n' \
               f'{" ".join(available_choices)} \n'
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
        available_choices = sorted(available_choices, key=lambda x: years_dict[x])
        text = 'Choose a year. Available years \n' \
               '(The first available year has less data, the last one has more): \n' \
               f'{" ".join(available_choices)} \n'

    # Get user`s choice
    while user_choice not in available_choices:
        user_choice = input(text)

    return user_choice


def main():
    """
    Main function to interact with user
    :return: (str, None)
    """
    # Define variables
    intro = "This program is made to help in researching about \n" \
            "Corruption in Developing countries in comparison with Ukraine"
    note = "The list of all available countries is in config.py \n" \
           "Some information about specific countries or specific years \n" \
           "May be missing \n"
    no_data = "Sorry, there is not data about this country this year"

    print(intro)
    print('NOTE')
    print(note)

    global cpi_table
    cpi_table = GetData().get_cpi_table()
    first_choice = first_choose()
    second_choice = second_choose()
    third_choice = third_choose(int(first_choice))
    fourth_choice = fourth_choose(third_choice, second_choice)
    get_data(third_choice, second_choice, fourth_choice)


if __name__ == '__main__':
    main()
