import os
import re
import datetime


path = '/home/steam/Backups/Valheim'

file =  'Mames_2021-04-07_11-00-01.db'

full_path = os.path.join(path, file)

now = datetime.datetime.now()

regex = re.compile(r'(20\d\d)-(\d\d)-(\d\d)_(\d\d)-(\d\d)-(\d\d)')
matches = []

for file in os.listdir(path):

    if regex.search(file):

        match = regex.search(file)
        
        year = int(match.group(1))
        month = int(match.group(2))
        day = int(match.group(3))
        hour = int(match.group(4))
        minute = int(match.group(5))
        second = int(match.group(6))

        file_date = datetime.datetime(year, month, day, hour=hour, minute=minute, second=second)
        difference = now - file_date
        
        if difference.days > 14:
            print(file)
        

