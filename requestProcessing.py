import requests
import os
import zipfile
import flask as fl

CacheFolder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cache")

# Connects with the API with a GET request using the provided data
def consumeAPI(URL, data):
    filters = False

    # Generates the URL with the given parameters
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
        zipF = save(response)
        try:
            return "Information gathered successfuly", 200, zipF
        except FileNotFoundError:
            return "File not found in the specified directory", 404
        
    else:
        return "The requested information couldn't be found", 404

# Save the fetched information in a JSON file inside a ZIP file and get the byte data
def save(response):
    if not os.path.isdir(CacheFolder):
        os.makedirs(CacheFolder)
        
    name = str(hash(response.content))
    jsonRoute = os.path.join(CacheFolder, name + ".json")
    zipRoute = os.path.join(CacheFolder, name + ".zip")

    with open(jsonRoute, "wb") as f:
        f.write(response.content)

    with zipfile.ZipFile(zipRoute, "x", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        zf.write(jsonRoute, arcname= name + ".json")

    zipData = ""
    with open(zipRoute, "rb") as zf:
        zipData = zf.read()

    os.remove(jsonRoute)
    os.remove(zipRoute)

    return name, zipData