import os
import pathlib
import re
import datetime


path = '/home/steam/Backups/Valheim'

today = datetime.date.today()
today_string = today.strftime('%Y-%m-%d')
regex = re.compile(today_string))

matches = []

for file in os.listdir(path):
	if regex.search(file):
		matches.append(file)

print(today.strftime('%Y-%m-%d'))
print(today_string)
