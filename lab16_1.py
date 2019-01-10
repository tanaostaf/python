#! /usr/bin/python3
import re
import csv
from urllib.request import urlopen
html = urlopen("http://www.codeabbey.com/index/user_ranking")
body_pattern = re.compile(
    r"<table class=\"table table-striped table-bordered full-width ranking-table\">([\s\S]*)</table>")
a_pattern = re.compile(r'<a href="[\s\S]*?>([\s\S]*?)</a>')
html_data = html.read().decode('utf-8')

body_text = re.findall(body_pattern, html_data)

trs = re.findall(re.compile(r"<tr class=\"centered none\">([\S\s\n]*?)</tr>"), body_text[0])
with open('list1.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for tr in trs:
        tds = re.findall(re.compile(r'<td>([\S\s\n]*?)</td>'), tr)
        if not tds:
            continue
        tds[2] = re.findall(a_pattern, tds[2])[0]
        data = [tds[0], tds[2], tds[3],
                re.findall(re.compile(r'<span class="rank rank\d+">([\S\s\n]*?)</span>'), tds[4])[0], tds[5].replace(",",""), tds[7]]
        filewriter.writerow(data)