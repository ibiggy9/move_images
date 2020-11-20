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
            with zipfile.ZipFile(f'path to /downloads/{i}', 'r') as zip_ref:
                zip_ref.extractall('path to desired folder for your images to go')
            time.sleep(1)
#arbitrary folder for trash because I couldnt find the trash folder in the file system on a mac. Could also use os.system(rm-r) 
#if you want them to be deleted.
            os.rename(f'path to downloads/{i}', f'/downloads/zip_grave/{i}')
    time.sleep(10)
