#! /usr/bin/python3
import re
import csv
from urllib.request import urlopen
html = urlopen("https://price.ua/catc839t14.html")
notebookі_regex = re.compile(
    r'<div class="product-block type2 ga_container [\S\s\n]*?>([\S\s\n]*?)</a></div>')
name_regex = re.compile(r'target="_blank">([\S\s]*?)<\/a>')
descriptions_regex = re.compile(r'([\S\s]*?)<div class="short-descr-line">\s*([\S\s]*?)<span class="fbold">([\S\s]*?)</span>[\S\s]*?</div>')
price_regex = re.compile(r'<div class="price-wrap"><span class="price"><span class="from">от</span>([\S\s]*?)<span class="uah">')
price_one_market = re.compile(r'<a class="price one-shop ga_card_mdl_price active-go"[\S\s]*?rel="nofollow">([\S\s]*?)<span class="uah">')
html_data = html.read().decode('utf-8')

notebooks = re.findall(notebookі_regex, html_data)
with open('list2.csv', 'w') as csvfile:
    fieldnames = ["Name","Price","Details"]
    filewriter = csv.DictWriter(csvfile,fieldnames=fieldnames)
    filewriter.writeheader()
    for notebook in notebooks:
        price = re.findall(price_regex,notebook)
        if len(price) == 0:
            price = re.findall(price_one_market,notebook)
        price = int(price[0].replace(" &nbsp;",'').replace(u"\xa0",''))
        if not(10000 < price and price < 20000):
            continue
        name = re.findall(name_regex,notebook)[0].replace("&quot;",'"')
        descriptions_raw = re.findall(descriptions_regex, notebook)
        descriptions = ""
        for description_raw in descriptions_raw:
            descriptions += " " + (description_raw[1] + description_raw[2])
        filewriter.writerow(
            {
                fieldnames[0] : name, 
                fieldnames[1] : price,
                fieldnames[2] : descriptions
            }
        )