from get_data import GetData


year = '2013'
country = 'ukraine'

data_1 = GetData(country, 2, year)
data_1 = data_1.export_data()

data_2 = GetData().get_cpi_table()
data_2 = data_2[country][data_2['Country'].index(year)]

print(f'Bribery index (% of gift or informal payment requests during public transactions) in {year}:')
print(data_1)

print('\n')

print(f'CPI in {year}:')
print(data_2)
