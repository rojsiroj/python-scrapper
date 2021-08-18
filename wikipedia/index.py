'''
Get Population data in Wikipedia.org and export to csv
https://github.com/rojsiroj
'''
import requests
from bs4 import BeautifulSoup
import csv

url = 'https://id.wikipedia.org/wiki/Daftar_negara_menurut_jumlah_penduduk'
website = requests.get(url)

soup = BeautifulSoup(website.text, 'html.parser')
first_table = soup.select_one('.wikitable')
# ignore the first and last element
table_rows = first_table.select('tr')[1:-1]
# defind csv and append the header
csv_data = []
csv_data.append(['rank', 'name', 'population', 'date', 'percentage', 'source'])
for row in table_rows:
    table_data = row.select('td')
    rank = table_data[0].text.strip()
    name = table_data[1].find('a').text
    population = table_data[2].text.strip()
    date = table_data[3].text.strip()
    percentage = table_data[4].text.strip()
    source = table_data[5].find('a', href=True)['href']
    # append to csv
    csv_data.append([rank, name, population, date, percentage, source])

# create csv file
with open('countries_population.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)