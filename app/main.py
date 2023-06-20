import utils
import read_csv
import charts
import pandas as pd


def run():
  
  df = pd.read_csv('data.csv')
  df = df[df['Continent']== 'Africa']
  countries = df['Country'].values
  percentage = df['World Population Percentage'].values
  charts.generate_py_chart(countries, percentage)
  
 
  data = read_csv.read_csv('data.csv')
  data = list(filter(lambda item: item['Continent'] == 'South America', data))
  # labels, values = utils.get_population_percentage(data)
  
  country = input('Type Country: ')
  result = utils.population_by_counter(data, country)
  if len(result) > 0:
    country_data = result[0]
    labels, values = utils.get_population(country_data)
    charts.generate_bar_chart(country, labels, values)
    
if __name__ == '__main__':
  run()
