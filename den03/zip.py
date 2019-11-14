import zipfile

with zipfile.ZipFile("Python_course-master.zip", 'r') as zipobj:
    for file in zipobj.filelist:
        print(file)



import urllib
import requests


requests.get(url, headers={})

urllib