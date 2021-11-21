from bs4 import BeautifulSoup as bs  # HTML data structure
import requests
from random import randint
from time import sleep

# Bilbo mckenna

# URl to web scrap from.
# in this example we web scrap graphics cards from Newegg.com
# https://www.daft.ie/property-for-sale/dublin?pageSize=20&from=0
URL = 'https://www.daft.ie/property-for-sale/dublin?pageSize=20&from='

for page in range(1, 1):
    # pls note that the total number of
    # pages in the website is more than 5000 so i'm only taking the
    # first 10 as this is just an example

    req = requests.get(URL + str(page) + '/')
    soup = bs(req.text, 'html.parser')

    titles = soup.find_all('div', attrs={'class', 'head'})

    sleep(randint(2, 10))


# # name the output file to write to local disk
# out_filename = "daft_try.csv"
# # header of csv file to be written
# headers = "brand, product_name, shipping \n"
#
# # opens file, and writes headers
# f = open(out_filename, "w")
# f.write(headers)
#
# # loops over each product and grabs attributes about
# # each product
# for container in containers:
#     # Finds all link tags "a" from within the first div.
#     make_rating_sp = container.div.select("a")
#
#     # Grabs the title from the image title attribute
#     # Then does proper casing using .title()
#     brand = make_rating_sp[0].img["title"].title()
#
#     # Grabs the text within the second "(a)" tag from within
#     # the list of queries.
#     product_name = container.div.select("a")[2].text
#
#     # Grabs the product shipping information by searching
#     # all lists with the class "price-ship".
#     # Then cleans the text of white space with strip()
#     # Cleans the strip of "Shipping $" if it exists to just get number
#     shipping = container.findAll("li", {"class": "price-ship"})[0].text.strip().replace("$", "").replace(" Shipping", "")
#
#     # prints the dataset to console
#     print("brand: " + brand + "\n")
#     print("product_name: " + product_name + "\n")
#     print("shipping: " + shipping + "\n")
#
#     # writes the dataset to file
#     f.write(brand + ", " + product_name.replace(",", "|") + ", " + shipping + "\n")
#
# f.close()  # Close the file
