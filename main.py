#!/usr/bin/python3

# if you are using OSX you may recive a error 

#If you have installed Python 3.6 on OSX and are getting the 
#"SSL: CERTIFICATE_VERIFY_FAILED" error when trying to connect to an 
#https:// site, it's probably because Python 3.6 on OSX has no certificates at all, 
#and can't validate any SSL connections. This is a change for 3.6 on OSX, and requires a post-install 
#step, which installs the certifi package of certificates. 
#This is documented in the ReadMe, which you should find at /Applications/Python\ 3.6/ReadMe.rtf

#The ReadMe will have you run this post-install script, which just installs certifi: /Applications/Python\ 3.6/Install\ Certificates.command

# to do
# 1- download file - ok
# 2- unzip file
# 3- parses data based on single URL

# 4- Writes down stdout a new line delimited (\n) JSON series-by-series representation of the input CSV


import urllib.request
import zipfile
import csv
import json

# download file odi_gas_csv_beta.zip
print('downloading file...')

arquivo, headers = urllib.request.urlretrieve ("https://www.jodidata.org/_resources/files/downloads/gas-data/jodi_gas_csv_beta.zip", "jodi_gas_csv_beta.zip")


# print('unziping file...')

# zippedFile= zipfile.ZipFile('./jodi_gas_csv_beta.zip' )

# print('unzipping...')
# unzippedFile= zippedFile.extractall()

# print(unzippedFile)
# zippedFile.close()

zippedFile = zipfile.ZipFile('./jodi_gas_csv_beta.zip')

print('UNZIPPING FILE')
zippedFile.extractall()
zippedFile.close()


print('opening file...')

# csvFile = open('./jodi_gas_beta.csv', 'r')
# print (csvfile)
# csvFile.close
data = {}
with open('./jodi_gas_beta.csv', 'r') as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows in csvReader:
        print(rows)

print(data)
#csvFile = open('./jodi_gas_beta.csv', 'r')