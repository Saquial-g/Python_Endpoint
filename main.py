import requestProcessing as rp
import flask as fl
import os
import io
import time

from flask import after_this_request

app = fl.Flask(__name__)

@app.route("/")
def main_page():
    return "please use an endpoint to gather information."

#Process GET request for character information
@app.route("/character")
def GETcharaReq():
    data = {}

    data["name"] = fl.request.args.get('name')
    data["status"] = fl.request.args.get('status')
    data["species"] = fl.request.args.get('species')
    data["type"] = fl.request.args.get('type')
    data["gender"] = fl.request.args.get('gender')
    
    result = rp.consumeAPI(data)
        
    if result[1] == 200:
        response = fl.send_file(
            io.BytesIO(result[2][1]),
            as_attachment=True,
            download_name= result[2][0] + ".zip"
        )

        return response, result[1]
    else:
        return result[0], result[1]

@app.route("/character", methods=['POST'])
def POSTcharaReq():
    if fl.request.content_type == "application/json":
        content = fl.request.get_json()
        data = {}
        print(content)

        data["name"] = content.get("name")
        data["status"] = content.get("status")
        data["species"] = content.get("species")
        data["type"] = content.get("type")
        data["gender"] = content.get("gender")
        
        result = rp.consumeAPI(data)
        
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
