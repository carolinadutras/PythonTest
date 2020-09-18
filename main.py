#!/usr/bin/python3

# TO DO
# 1- download file - ok
# 2- unzip file - ok
# 3- parses data based on single URL - ok
# 4- Writes down to stdout the JSON content - ok

import urllib.request
import zipfile
import csv
import json

print('downloading file...')

arquivo, headers = urllib.request.urlretrieve ("https://www.jodidata.org/_resources/files/downloads/gas-data/jodi_gas_csv_beta.zip", "jodi_gas_csv_beta.zip")

print('unziping file...')

zippedFile = zipfile.ZipFile('./jodi_gas_csv_beta.zip' )

print('unzipping...')
unzippedFile = zippedFile.extractall()
print(unzippedFile)
zippedFile.close()

print('opening file...')

with open('./jsonOUTPUT.json', 'w') as jsonFile:
    with open('./jodi_gas_beta.csv', 'r') as csvFile:
        csvReader = csv.DictReader(csvFile)
        for rows in csvReader:
            jsonFile.write(json.dumps(rows, indent=4))
            print(json.dumps(rows, indent=4))