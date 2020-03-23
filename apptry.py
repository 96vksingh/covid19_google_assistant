
from flask import Flask, request, jsonify, render_template
import requests

from urllib.parse import unquote
from datetime import datetime


import os

import tempfile
from six.moves.urllib.request import urlopen
from six import BytesIO




app = Flask(__name__)
app.config['INTEGRATIONS'] = ['ACTIONS_ON_GOOGLE']

# assist = Assistant(app, route='/tell')

# @assist.action("hashtag")
# def tell_data(any):
    

# @app.route('/')
# def index():
#     print("data")
#     r=requests.get('https://corona.lmao.ninja/all')
    
#     print(r.json())

#     return render_template('index.html')



@app.route('/')
def index():
    mm="India"
    r=requests.get("https://corona.lmao.ninja/countries")
    # url="https://corona.lmao.ninja/countries/"+mm
    # r=requests.get(url)
    print("up")
    # country=list(r.json()['country'])
    hh=r.json()
    con=[]
    for h in hh:
        temp=h['country']

        temp2=temp.upper()
        con.append(temp2)
        print(temp2)
    print(mm.upper())
    con.clear()
    if "India" not in con:
        print("something")
    else:
        print("anything")
    # print(hh)
    print("down")
    # cases=str(r.json()['cases'])
    # today_case=str(r.json()['todayCases'])
    # deaths=str(r.json()['deaths'])
    # today_death=str(r.json()['todayDeaths'])
    # recovered=str(r.json()['recovered'])
    # active=str(r.json()['active'])
    # critical=str(r.json()['critical'])
    # rarecase=str(r.json()['casesPerOneMillion'])
    # speechtext="In "+country+", total caes are "+cases+". Today "+today_case+" cases were found. Total deaths are "+deaths+". Total recovered cases are "+recovered+" and active cases are "+active+"."
    # ti="Updated "+country+" data"
    # print(speechtext)
    return True




# https://corona.lmao.ninja/countries




if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')



