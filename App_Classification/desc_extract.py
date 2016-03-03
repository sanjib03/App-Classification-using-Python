#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import json
import os
import re
import requests
import sys

#Fetching data from iTunes website
link = 'https://itunes.apple.com/lookup?id=' + sys.argv[1] #1044202386

#Copying the content
resp = requests.get(link)

#Creating a json object using the text
d = json.loads(resp.text)

#Parsing thru the description and getting the description part
desc = (d["results"][0]["description"]).encode('utf-8').strip()

#Writing the description to a file
output_file = open("../Documents/App_Classification/"+sys.argv[1]+".txt","w")
output_file.write(desc)
output_file.close()
