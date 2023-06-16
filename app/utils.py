def get_population(country_dic):
  population_dic = {
    '1970': int(country_dic['1970 Population']),
    '1980': int(country_dic['1980 Population']),
    '1990': int(country_dic['1990 Population']),
    '2000': int(country_dic['2000 Population']),
    '2010': int(country_dic['2010 Population']),
    '2015': int(country_dic['2015 Population']),
    '2020': int(country_dic['2020 Population']),
    '2022': int(country_dic['2022 Population']),
  }

  return population_dic.keys(), population_dic.values()


def get_population_percentage(country_dic):
  # countries = []
  # population_percentage = []
  # for row in country_dic:
  #   countries.append(row['Country'])
  #   population_percentage.append(float(row['World Population Percentage']))
  # better do
  countries = list(map(lambda country: country['Country'], country_dic))
  population_percentage = list(
    map(lambda country: country['World Population Percentage'], country_dic))
  return countries, population_percentage


def population_by_counter(data, country):
  result = list(filter(lambda item: item['Country'] == country, data))
  return result
