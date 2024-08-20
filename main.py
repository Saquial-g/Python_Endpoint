import requestProcessing as rp
import flask as fl
import os
import io

from flask import after_this_request

app = fl.Flask(__name__)

@app.route("/")
def main_page():
    return "please use an endpoint to gather information."

#-----------------------------------------------------------------------------------------------------

#Processes GET request for character information
@app.route("/character")
def GETcharaReq():
    filters = {}

    filters["name"] = fl.request.args.get('name')
    filters["status"] = fl.request.args.get('status')
    filters["species"] = fl.request.args.get('species')
    filters["type"] = fl.request.args.get('type')
    filters["gender"] = fl.request.args.get('gender')
    
    URL = "https://rickandmortyapi.com/api/character"
    result = rp.consumeAPI(URL, filters)
        
    if result[1] == 200:
        response = fl.send_file(
            io.BytesIO(result[2][1]),
            as_attachment=True,
            download_name= result[2][0] + ".zip"
        )

        return response, result[1]
    else:
        return result[0], result[1]

#Processes POST requests for character information
@app.route("/character", methods=['POST'])
def POSTcharaReq():
    if fl.request.content_type == "application/json":
        content = fl.request.get_json()
        filters = {}
        print(content)

        filters["name"] = content.get("name")
        filters["status"] = content.get("status")
        filters["species"] = content.get("species")
        filters["type"] = content.get("type")
        filters["gender"] = content.get("gender")
        
        URL = "https://rickandmortyapi.com/api/character"
        result = rp.consumeAPI(URL, filters)
        
        if result[1] == 200:
            response = fl.send_file(
                io.BytesIO(result[2][1]),
                as_attachment=True,
                download_name= result[2][0] + ".zip"
            )

            return response, result[1]
        else:
            return result[0], result[1]
    else:
        return "Content-Type not supported.", 415

#-----------------------------------------------------------------------------------------------------

#Processes GET request for location information
@app.route("/location")
def GETlocReq():
    filters = {}

    filters["name"] = fl.request.args.get('name')
    filters["type"] = fl.request.args.get('type')
    filters["dimension"] = fl.request.args.get('dimension')
    
    URL = "https://rickandmortyapi.com/api/location"
    result = rp.consumeAPI(URL, filters)
        
    if result[1] == 200:
        response = fl.send_file(
            io.BytesIO(result[2][1]),
            as_attachment=True,
            download_name= result[2][0] + ".zip"
        )

        return response, result[1]
    else:
        return result[0], result[1]

#Processes POST requests for location information
@app.route("/location", methods=['POST'])
def POSTlocReq():
    if fl.request.content_type == "application/json":
        content = fl.request.get_json()
        filters = {}
        print(content)

        filters["name"] = content.get("name")
        filters["type"] = content.get("type")
        filters["dimension"] = content.get("dimension")
        
        URL = "https://rickandmortyapi.com/api/location"
        result = rp.consumeAPI(URL, filters)
        
        if result[1] == 200:
            response = fl.send_file(
                io.BytesIO(result[2][1]),
                as_attachment=True,
                download_name= result[2][0] + ".zip"
            )

            return response, result[1]
        else:
            return result[0], result[1]
    else:
        return "Content-Type not supported.", 415

#-----------------------------------------------------------------------------------------------------

#Processes GET request for episode information
@app.route("/episode")
def GETepiReq():
    filters = {}

    filters["name"] = fl.request.args.get('name')
    filters["episode"] = fl.request.args.get('episode')
    
    URL = "https://rickandmortyapi.com/api/episode"
    result = rp.consumeAPI(URL, filters)
        
    if result[1] == 200:
        response = fl.send_file(
            io.BytesIO(result[2][1]),
            as_attachment=True,
            download_name= result[2][0] + ".zip"
        )

        return response, result[1]
    else:
        return result[0], result[1]

#Processes POST requests for episode information
@app.route("/episode", methods=['POST'])
def POSTepiReq():
    if fl.request.content_type == "application/json":
        content = fl.request.get_json()
        filters = {}
        print(content)

        filters["name"] = content.get("name")
        filters["episode"] = content.get("episode")
        
        URL = "https://rickandmortyapi.com/api/episode"
        result = rp.consumeAPI(URL, filters)
        
        if result[1] == 200:
            response = fl.send_file(
                io.BytesIO(result[2][1]),
                as_attachment=True,
                download_name= result[2][0] + ".zip"
            )

            return response, result[1]
        else:
            return result[0], result[1]
    else:
        return "Content-Type not supported.", 415


if __name__ == '__main__':
    app.run(port=5000,debug=True) 
