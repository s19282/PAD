import pandas as pd
import requests
from bs4 import BeautifulSoup
from random import randint
from time import sleep
import os

# z2
if os.path.exists('offers.csv'):
    os.remove('offers.csv')
baseurl = "https://www.otomoto.pl/osobowe?page="
pageNumber = 0
# vehicles = pd.DataFrame(
#     columns=['seller type', 'make', 'model', 'version', 'year', 'mileage', 'capacity', 'fuel', 'horse power',
#              'transmission', 'drive train', 'damaged', 'body type', 'seats', 'doors', 'color', 'first owner',
#              'serviced at aso', 'state', 'country', 'accident free', 'seller name', 'location'])

vehicles = pd.DataFrame()

while True:
    pageNumber = pageNumber + 1
    print("Page: ", pageNumber)
    page = requests.get(f"{baseurl}{pageNumber}")
    # sleep(randint(1, 10))
    soup = BeautifulSoup(page.text, 'html.parser')
    offers = soup.select('article div h2 a[href]')
    if pageNumber % 50 == 0:
        vehicles.to_csv('offers.csv', encoding='utf-8')

    try:
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

            newVehicle['price'] = vehicle.select('span.offer-price__number')[0].text.strip()
            newVehicle['currency'] = vehicle.select('span.offer-price__number span.offer-price__currency')[0].text.strip()
            newVehicle['priceDetails'] = vehicle.select('span.offer-price__details')[0].text.strip()
            newVehicle['location'] = vehicle.select('a.seller-card__links__link__cta')[0].text.strip()
            newVehicle['description'] = vehicle.select('div.offer-description__description')[0].text.strip()

            vehicles = vehicles.append(newVehicle, ignore_index=True)

    except Exception:
        vehicles.to_csv('offers.csv', encoding='utf-8')
        break
