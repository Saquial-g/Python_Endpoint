import requests
import os
import zipfile

from flask import request

CacheFolder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cache")

def consumeAPI(data):
    URL = "https://rickandmortyapi.com/api/character"
    
    filters = False

    for k, v in data.items():
        if v:
            if filters:
                URL += "&"
            else:
                URL += "/?"
                filters = True

            URL += k + "=" + v

    print(URL)
    response = requests.get(URL)

    if response.status_code == 200:
        save(response)
        return "Information fetched and downloaded successfully", 200
    else:
        return "The requested information couldn't be found", 404


def save(response):
    if not os.path.isdir(CacheFolder):
        os.makedirs(CacheFolder)
        
    name = str(hash(response.content))
    jsonRoute = os.path.join(CacheFolder, name + ".json")
    zipRoute = os.path.join(CacheFolder, name + ".zip")

    with open(jsonRoute, "wb") as f:
        f.write(response.content)

        with zipfile.ZipFile(zipRoute, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
            zf.write(jsonRoute, arcname= name + ".json")
        
    