#! /usr/bin/python3
import re
import csv
from urllib.parse import unquote
from urllib.request import urlopen
html = urlopen("https://if.isuo.org/authorities/schools-list/id/626")
html_data = html.read().decode('utf-8')

table_list_regex = re.compile(r'<table class="zebra-stripe list">([\S\s]*?)</table>')
links_regex = re.compile(r'<a href="([\S\s]*?)">')

table_data_regex = re.compile(r'<table class="zebra-stripe">([\S\s]*?)</table>')
full_name_regex = re.compile(r'Повна назва:</th>\s*?<td>([\S\s]*?)</td>')
type_name_regex = re.compile(r'Тип ЗЗСО:</th>\s*?<td>([\S\s]*?)</td>')
manager_name_regex = re.compile(r'Директор:</th>\s*?<td>([\S\s]*?)</td>')
phone_number_regex = re.compile(r'Телефони:</th>\s*?<td>([\S\s]*?)</td>')
count_regex = re.compile(r'Кількість учнів:</th>\s*?<td>([\S\s]*?)</td>')
id_regex = re.compile(r'№ у системі:</th>\s*?<td>([\S\s]*?)</td>')
email_regex = re.compile(r'.before\(unescape\(\'([\S\s]*?)\'\)\)\.remove\(\)')
email_link_regex = re.compile(r'<a href="mailto:([\S\s]*?)">')

table = re.findall(table_list_regex, html_data)[0]
links = re.findall(links_regex, table)
with open('list3.csv', 'w') as csvfile:
    fieldnames = ["Id","Full Name","Type","Manager name", "Phone numbers","Count", "Email"]
    filewriter = csv.DictWriter(csvfile,fieldnames=fieldnames)
    filewriter.writeheader()
    for link in links:
        table = re.findall(table_data_regex,urlopen('https://if.isuo.org' + link)
            .read().decode('utf-8'))[0]

        id = re.findall(id_regex,table)[0]
        full_name = re.findall(full_name_regex,table)[0].replace("&quot;",'"')
        type_name = re.findall(type_name_regex,table)[0].replace("&quot;",'"')
        manager_name = re.findall(manager_name_regex,table)[0]
        phone_numbers = re.findall(phone_number_regex,table)[0].replace(',',';')
        count = re.findall(count_regex,table)[0]
        
        email = re.findall(email_regex,table)
        if len(email) != 0:
            email = re.findall(email_link_regex,unquote(email[0]))[0]
        else:
            email = ""    

        filewriter.writerow(
            {
                fieldnames[0] : id, 
                fieldnames[1] : full_name,
                fieldnames[2] : type_name,
                fieldnames[3] : manager_name,
                fieldnames[4] : phone_numbers,
                fieldnames[5] : count,
                fieldnames[6] : email
            }
        )