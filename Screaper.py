# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 11:15:18 2020

@author: Robb
"""

import requests
from html.parser import HTMLParser

proxyList = list()

class TableParser(HTMLParser):
    temp = list()
    
    def __init__(self):
        HTMLParser.__init__(self)
        self.in_td = False

    def handle_starttag(self, tag, attrs):
        if tag == 'td':
            self.in_td = True
            if len(attrs) > 0:
                self.country = True
                if attrs[0][1] == "hx":
                    self.secure = True
                           
    def handle_data(self, data):
        if self.in_td:
            if "." in data:
                self.temp = list()
                self.temp.append(data)
            elif data.isnumeric():
                self.temp.append(data)
            elif self.country and len(self.temp) != 0:
                self.temp.append(data)
            if self.secure:
                self.temp.pop()
                self.temp.pop()
                self.temp.append(data)
                proxyList.append(self.temp)
                self.temp = list()            
                
    def handle_endtag(self, tag):
        self.in_td = False
        self.country = False
        self.secure = False

page = requests.get('https://free-proxy-list.net/')
s = page.content.decode(encoding="ascii", errors="ignore")

parser = TableParser()
parser.feed(s)

f = open("table.html", "w")
f.write("<table>")
for p in proxyList:
    f.write("<tr>")
    for i in p:
        f.write("<td>" + i + "</td>")
    f.write("</tr>")
f.write("</table>")
f.close()




