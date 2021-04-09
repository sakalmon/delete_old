import os
import re
import datetime


LIMIT = 14

path = '/home/steam/Backups/Valheim'

now = datetime.datetime.now()

regex = re.compile(r'(20\d\d)-(\d\d)-(\d\d)_(\d\d)-(\d\d)-(\d\d)')
matches = []
mbytes_deleted = 0
count = 0

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
            count += 1
            file_to_delete = os.path.join(path, file)
            print(file_to_delete)
            #os.remove(file_to_delete)
            mbytes_deleted += os.stat(file_to_delete).st_size / 1000000 # Get size of file and convert to Megabytes
            mbytes_deleted = round(mbytes_deleted)

print(f'{count} files deleted ({mbytes_deleted}MB).')



        

