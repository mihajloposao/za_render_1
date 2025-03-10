import os
from flask import Flask, request,url_for,redirect
from qr_obrada_smestanje import web_scraping
import requests


app = Flask(__name__)

@app.route("/qr",methods=["POST"])
def qr():
    povratna = request.json 
    qr = povratna.get("qr")
    response = requests.post("https://mihajlo22.pythonanywhere.com/upis",json=web_scraping(qr))
    if response.status_code == 200:
        return {'rezultat': "USPEŠNO SKENIRANJE"}
    else:
        return "",response.status_code

@app.route("/",methods=["GET"])
def home():
    return "RADI"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
