import os
import re
import datetime


path = '/home/steam/Backups/Valheim'

file =  'Mames_2021-04-07_11-00-01.db'

full_path = os.path.join(path, file)

now = datetime.datetime.now()
yesterday = datetime.datetime(2021, 3, 23)
difference = now - yesterday
print(now)
print(yesterday)
print(difference.days)

regex = re.compile(r'(20\d\d)-(\d\d)-(\d\d)')
matches = []

for file in os.listdir(path):

    if regex.search(file):
        
        match = regex.search(file)
        
        year = match.group(1)
        month = match.group(2)
        day = match.group(3)

        file_date = datetime.datetime(year, month, day)
        print(year, month, day)
        

