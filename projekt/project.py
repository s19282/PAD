import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

# z2
baseurl = "https://www.otomoto.pl/osobowe"

# vehicles = pd.DataFrame(
#     columns=['seller type', 'make', 'model', 'version', 'year', 'mileage', 'capacity', 'fuel', 'horse power',
#              'transmission', 'drive train', 'damaged', 'body type', 'seats', 'doors', 'color', 'first owner',
#              'serviced at aso', 'state', 'country', 'accident free', 'seller name', 'location'])

vehicles = pd.DataFrame()

page = requests.get(baseurl)
soup = BeautifulSoup(page.text, 'html.parser')
offers = soup.select('article div h2 a[href]')

for offer in offers:
    offerLink = offer['href']
    offerHTML = requests.get(offerLink).text
    vehicle = BeautifulSoup(offerHTML, 'html.parser')
    data = vehicle.select('ul li.offer-params__item')

    newVehicle = {}

    for param in data:
        value = ''
        try:
            value = param.select('div a')[0].text.strip()
        except IndexError:
            value = param.select('div')[0].text.strip()

        match param.select('span')[0].text:
            case 'Oferta od':
                newVehicle['seller type'] = value
            case 'Marka pojazdu':
                newVehicle['make'] = value
            case 'Model pojazdu':
                newVehicle['model'] = value
            case 'Wersja':
                newVehicle['version'] = value
            case 'Rok produkcji':
                newVehicle['year'] = value
            case 'Pojemność skokowa':
                newVehicle['capacity'] = value
            case 'Rodzaj paliwa':
                newVehicle['fuel'] = value
            case 'Moc':
                newVehicle['horse power'] = value
            case 'Skrzynia biegów':
                newVehicle['transmission'] = value
            case 'Napęd':
                newVehicle['drive train'] = value
            case 'Uszkodzony':
                newVehicle['damaged'] = value
            case 'Typ nadwozia':
                newVehicle['body type'] = value
            case 'Liczba drzwi':
                newVehicle['doors'] = value
            case 'Liczba miejsc':
                newVehicle['seats'] = value
            case 'Kolor':
                newVehicle['color'] = value
            case 'Pierwszy właściciel':
                newVehicle['first owner'] = value
            case 'Serwisowany w ASO':
                newVehicle['serviced at aso'] = value
            case 'Stan':
                newVehicle['state'] = value

    vehicles = vehicles.append(newVehicle, ignore_index=True)
print(vehicles)
vehicles.to_csv('offers.csv', index=False, encoding='utf-8')

