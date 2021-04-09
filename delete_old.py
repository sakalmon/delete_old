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
