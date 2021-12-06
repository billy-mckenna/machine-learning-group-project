from bs4 import BeautifulSoup as bs  # HTML data structure
import requests
from random import randint
from time import sleep
import csv

# URL = 'https://www.daft.ie/property-for-sale/dublin?pageSize=20&from=0'
URL = 'https://www.daft.ie/property-for-sale/dublin?pageSize=20&from='

price_list = []
location_list = []
beds_list = []
baths_list = []
square_area_list = []
type_list = []

Price_list = []
Location_list = []
Beds_list = []
Baths_list = []
Square_area_list = []
Type_list = []

# All the Dublin zones, 6W si given the number 25 int eh clean data
Dublin_zones = ['1', '2', '3', '4', '5', '6', '6W', '7', '8', '9', '10', '11',
                '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24']

fieldnames = ['Price', 'Location', 'Beds', 'Baths', 'Square Area', 'Type']


def write_to_csv(list_input, name):
    # The scraped info will be written to a CSV here.
    try:
        with open(name, "a",  newline='') as fopen:  # Open the csv file.
            csv_writer = csv.writer(fopen)
            csv_writer.writerow(list_input)
    except:
        return False


# Write headers to two csv files
write_to_csv(fieldnames, './data/raw_data/daft_data.csv')
write_to_csv(fieldnames, './data/raw_data/daft_data_clean.csv')
num_pages = 2
for page in range(0, num_pages):
    print(page)
    # get the info on each page then move onto the next one
    p = 20*page # 20 items per page
    req = requests.get(URL + str(p))
    soup = bs(req.text, 'html.parser')

    # get target and feature values for each advert
    for title_block in soup.find_all('div', attrs={'data-testid': 'title-block'}):
        flag_missing_value = False
        # only save record if it has a price, give N/A if missing feature
        price = title_block.find('div', attrs={'data-testid': 'price'})
        price_item = price.get_text().strip()
        if price_item[0] == '€':
            temp = price_item.split('€')
            temp[1] = temp[1].replace(',', '')
            clean_price = int(temp[1])
            price_list.append(price_item)
            location = title_block.find('p', attrs={'data-testid': 'address'})
            beds = title_block.find('p', attrs={'data-testid': 'beds'})
            baths = title_block.find('p', attrs={'data-testid': 'baths'})
            square_area = title_block.find('p', attrs={'data-testid': 'floor-area'})
            ptype = title_block.find('p', attrs={'data-testid': 'property-type'})
            if location is None:
                location_item = 'N/A'
                location_list.append('N/A')
                flag_missing_value = True
            else:
                location_item = location.get_text().strip()
                location_list.append(location_item)
                temp = location_item.split(',')
                temp = temp[len(temp) - 1]
                temp = temp.split()
                for zone in Dublin_zones:
                    if len(temp) > 1:
                        if temp[1] == zone:
                            if zone == '6W':
                                clean_location = 25
                            else:
                                clean_location = int(temp[1])
                            break
                        elif zone == Dublin_zones[len(Dublin_zones) - 1]:
                            clean_location = 'N/A'
                            flag_missing_value = True
                    else:
                        clean_location = 'N/A'
                        flag_missing_value = True
            if beds is None:
                beds_item = 'N/A'
                beds_list.append('N/A')
                flag_missing_value = True
            else:
                beds_item = beds.get_text().strip()
                temp = beds_item.split()
                num_beds = int(temp[0])
                beds_list.append(beds_item)
            if baths is None:
                baths_item = 'N/A'
                baths_list.append('N/A')
                flag_missing_value = True
            else:
                baths_item = baths.get_text().strip()
                temp = baths_item.split()
                num_baths = int(temp[0])
                baths_list.append(baths_item)
            if ptype is None:
                ptype_item = 'N/A'
                type_list.append('N/A')
                flag_missing_value = True
            else:
                ptype_item = ptype.get_text().strip()
                if ptype_item == 'Semi-D':
                    num_ptype = 1
                elif ptype_item == 'Apartment':
                    num_ptype = 2
                elif ptype_item == 'Bungalow':
                    num_ptype = 3
                elif ptype_item == 'Terrace':
                    num_ptype = 4
                elif ptype_item == 'End of Terrace':
                    num_ptype = 5
                elif ptype_item == 'Detached':
                    num_ptype = 6
                elif ptype_item == 'Site':
                    num_ptype = 7
                    flag_missing_value = True
                type_list.append(ptype_item)
            if square_area is None:
                square_area_item = 'N/A'
                square_area_list.append('N/A')
                flag_missing_value = True
            elif ptype_item != 'Site':
                square_area_item = square_area.get_text().strip()
                temp = square_area_item.split()
                if flag_missing_value is False:
                    num_square_area = int(temp[0])
                    square_area_list.append(square_area_item)
            else:
                flag_missing_value = True
                square_area_item = 'N/A'
                square_area_list.append('N/A')
            write_to_csv([price_item, location_item, beds_item, baths_item, square_area_item, ptype_item], './data/raw_data/daft_data.csv')
            if flag_missing_value == False:
                write_to_csv([clean_price, clean_location, num_beds, num_baths, num_square_area, num_ptype], "./data/raw_data/daft_data_clean.csv")
    sleep(randint(2, 10))


print(price_list); print(len(price_list))
print(location_list); print(len(location_list))
print(beds_list); print(len(beds_list))
print(baths_list); print(len(baths_list))
print(square_area_list); print(len(square_area_list))
print(type_list); print(len(type_list))


