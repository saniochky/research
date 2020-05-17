import json
import requests
import urllib.request
from lxml import etree
from config import API_KEY, INDEX_DICT, ISO, DEVELOPING_COUNTRIES


class GetData:
    """
    Class for representing data
    """

    def __init__(self, country=None, index=None, year=None):
        """
        Initializes new data
        :param country: str
        :param index: int
        :param year: inr
        """
        if country and index and year:
            assert 2 <= index <= 8, 'Index range must be from 2 to 8'

            self.country = country
            self.iso = DEVELOPING_COUNTRIES_ISO[self.country]
            self.index = INDEX_DICT[index]
            self.year = year
            self.api_key = API_KEY
            self.data = self.get_quandl()

    def get_quandl(self):
        """
        Gets data from Quandl
        :return: (None, float)
        """
        # Define the returning value and URL address
        value = None
        url = f'https://www.quandl.com/api/v3/datasets/WESV/{self.iso}_{self.index}.json?api_key={self.api_key}'

        try:
            # Get data in json format from URL
            with urllib.request.urlopen(url) as response:
                data = response.read()
                data = data.decode('utf-8')
                data = json.loads(data)
                data = data['dataset']['data']

            # Get needed value
            for el in data:
                if str(self.year) == el[0][0:4]:
                    value = el[1]
        except urllib.error.HTTPError:
            pass

        return value

    @staticmethod
    def get_quandl_year(country, index):
        """
        Gets available years for given country and data
        :param country:
        :param index:
        :return:
        """
        # Define the returning value and URL address
        value = []
        url = f'https://www.quandl.com/api/v3/datasets/WESV/{ISO[country]}_{INDEX_DICT[index]}.' \
              f'json?api_key={API_KEY}'

        # Get data in json format from URL
        try:
            with urllib.request.urlopen(url) as response:
                data = response.read()
                data = data.decode('utf-8')
                data = json.loads(data)
                data = data['dataset']['data']

            # Get all available years
            for el in data:
                value.append(el[0][0:4])
        except urllib.error.HTTPError:
            pass

        return value

    @staticmethod
    def get_cpi_table():
        """
        Gets data about CPI
        :return:
        """
        # State the URL address
        url = 'https://stats.areppim.com/listes/list_corruption.htm'

        # Get HTML table in text format from URL
        response = requests.get(url)
        text = response.text[6611:69292]
        text = text[:7] + text[163:61668] + text[-8:]

        # Make dictionary from HTML table
        table = etree.HTML(text).find("body/table")
        rows = iter(table)
        headers = [
            col.text for col in next(rows)
        ]
        new_table = {
            headers[0]: headers[1:-1]
        }

        for row in rows:
            values = [
                None if x == 'Â\xa0' else x for x in [col.text for col in row]
            ]
            new_table[values[0].lower()] = values[1:-1]

        return new_table

    def export_data(self):
        """
        Exports data
        :return: (None, float, int, dict)
        """
        return self.data
