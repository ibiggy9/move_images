import os 
import time
import zipfile

while True:
    empty = []
    with os.scandir('/Users/user9231/downloads') as entries:
        for entry in entries:
            empty.append(entry.name)


    l = ['.zip']
    for i in empty:
        if any(word in i for word in l):
            with zipfile.ZipFile(f'/Users/user9231/downloads/{i}', 'r') as zip_ref:
                zip_ref.extractall('/Users/user9231/desktop/ecom/images/walmart/cookies/bp/banana/')
            time.sleep(1)
            os.rename(f'/Users/user9231/downloads/{i}', f'/Users/user9231/downloads/zip_grave/{i}')
    time.sleep(10)