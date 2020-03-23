
from flask import Flask, request, jsonify, render_template

from urllib.parse import unquote

from flask_assistant import ask, tell, event, build_item, Assistant
# import matplotlib.pyplot as plt
import os
import json
import requests

app = Flask(__name__)
app.config['INTEGRATIONS'] = ['ACTIONS_ON_GOOGLE']

assist = Assistant(app, route='/tell')


# @assist.action("hashtag")
# def tell_data(any):



@assist.action("covid19")
def say_hashtag(any):

    r=requests.get("https://corona.lmao.ninja/countries")
    hh=r.json()
    con=[]
    for h in hh:
        temp=h['country']
        temp2=temp.upper()
        con.append(temp2)



    mm=""
    for ss in any: 
        p=ss.capitalize()
        mm=mm+p
    print(mm)



    if mm not in con:
        # labels = 'Cases', 'Deaths', 'Recovered'
        # sizes = [, 30, 45, 10]
        r=requests.get("https://corona.lmao.ninja/all")
        cases=str(r.json()['cases'])
        deaths=str(r.json()['deaths'])
        recovered=str(r.json()['recovered'])
        updated=str(r.json()['updated'])
        speechtext="I couldn't get the country name. Here is the global data of covid'19. Overall cases are "+cases+" with total deaths of "+deaths+" and recovered patients are "+recovered+"."

        return tell(speechtext).card(
            text=speechtext,
            title='Updated global data'
        )
    else:
        url="https://corona.lmao.ninja/countries/"+mm
        r=requests.get(url)
        country=str(r.json()['country'])
        cases=str(r.json()['cases'])
        today_case=str(r.json()['todayCases'])
        deaths=str(r.json()['deaths'])
        today_death=str(r.json()['todayDeaths'])
        recovered=str(r.json()['recovered'])
        active=str(r.json()['active'])
        critical=str(r.json()['critical'])
        rarecase=str(r.json()['casesPerOneMillion'])
        speechtext="In "+country+", total cases are "+cases+". Today "+today_case+" cases were found. Total deaths are "+deaths+" and total recovered cases are "+recovered+". Active cases are "+active+"."
        ti="Updated "+country+" data"
        return tell(speechtext).card(
            text=speechtext,
            title=ti
        )

    

    

@assist.prompt_for('any', intent_name='covid19')
def prompt_color(any):
    speech = "Sorry I didn't catch that. What did you say?"
    return ask(speech)



    
    
    





if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))



