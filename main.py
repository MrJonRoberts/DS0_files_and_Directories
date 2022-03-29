import os
from datetime import datetime
# directories:

def convertDate(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y')
    return formated_date

directory = r".\UPLOADS\JRO"
with os.scandir(directory) as dirList:
    for file in dirList:
        name = file.name
        modifiedTime = convertDate(file.stat().st_mtime)
        size = os.path.getsize(file)
        fileType = os.path.splitext(name)[1]
        # line wraps - is all 1 line
        print(f'{name}\t\t Last Modified: {modifiedTime} \t\t{(size/1024)}kb \t\t{fileType}')