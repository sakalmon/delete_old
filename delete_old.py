import os
import re
import datetime


LIMIT = 14

path = '/home/steam/Backups/Valheim'

now = datetime.datetime.now()

regex = re.compile(r'(20\d\d)-(\d\d)-(\d\d)_(\d\d)-(\d\d)-(\d\d)')
matches = []
mbytes_deleted = 0

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
        
        if difference.days > LIMIT:
            print(os.path.join(path, file), end=' ')
            mbytes_deleted += os.stat(os.path.join(path, file)).st_size / 1000000

print(mbytes_deleted)



        

