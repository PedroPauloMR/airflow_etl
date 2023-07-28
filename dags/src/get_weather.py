import requests
import datetime as dt
import os
import json


url = "https://weatherapi-com.p.rapidapi.com/current.json"

querystring = {"q":"53.1,-0.13"}

headers = {
	"X-RapidAPI-Key": "94b04a21a1msh01ceaf978869e81p1ed230jsnd34ffc127d18",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

if response.status_code == 200:
    json_data = response.json()
    file_name = str(dt.datetime.now().date()) + '.json'

    tot_name = os.path.join(os.path.dirname(  __file__ ), 'data', file_name)
    with open( tot_name, 'w') as outputfile:
        json.dump(json_data, outputfile)

else:
    print(response.status_code)
    print(' Error in API call ')