'''
A Web application that shows Google Maps around schools, using
the Flask framework, and the Google Maps API.
'''

from flask import Flask, render_template, abort
from flask import json
import requests
from flask import request,Response

app = Flask(__name__)

swaggerHostName = "http://sawgger_service:8080"

class School:
    def __init__(self, key, name, lat, lng):
        self.key  = key
        self.name = name
        self.lat  = lat
        self.lng  = lng

schools = (
    School('hv',      'Happy Valley Elementary',   37.9045286, -122.1445772),
    School('stanley', 'Stanley Middle',            37.8884474, -122.1155922),
    School('wci',     'Walnut Creek Intermediate', 37.9093673, -122.0580063)
)
schools_by_key = {school.key: school for school in schools}


@app.route("/")
def index():
    return render_template('index.html', schools=schools)

@app.route("/plot")
def crimeMarkers():
    return render_template('plotters.html', schools=schools)

@app.route("/<school_code>")
def show_school(school_code):
    school = schools_by_key.get(school_code)
    if school:
        return render_template('map.html', school=school)
    else:
        abort(404)
        
        
@app.route('/crimeSearch', methods = ['POST'])
def crimeSearch():
    clusteredCrimeList = []
    userData = request.get_json(silent=True)
    
    #print(userData)
    #print(userData['latitude'])
    #print(userData['longitude'])
    
    url = swaggerHostName + '/cloudmesh/crime_finder/crimes?latitude='+str(userData['latitude'])+'&longitude='+str(userData['longitude'])+'&radius='+str(userData['radius'])
    responseR = requests.get(url,headers={"Content-Type": "application/json"})
    
     #Response object
    response = Response()
    response.headers["status"] = 200
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    data=json.dumps(responseR.json())
    dataRead=json.loads(data)
    '''
    for crime in dataRead:
        print(kmeans_predic_clusterr(crime['date'],crime['arrested'],crime['domestic'],crime['primary_description']))
        crime['clustered']='true'
        clusteredCrimeList.append(crime)
    '''
    response.data=json.dumps(dataRead)
    
    return response


@app.route('/crimeList', methods = ['GET'])
def crimeList():
    crime_list = {}

    url = swaggerHostName + '/cloudmesh/crime_finder/crimes/list'
    responseR = requests.get(url, headers={"Content-Type": "application/json"})
    data = json.dumps(responseR.json())
    dataRead = json.loads(data)
    for row in dataRead:
        crime_list[row['primaryType']] = (row['index'], row['primaryType_display'])

     #Response object
    response = Response()
    response.headers["status"] = 200
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    data=json.dumps(crime_list)
    response.data=data
    
    return response


@app.route('/crimeByMonth', methods=['GET'])
def crimeByMonth():

    url = swaggerHostName + '/cloudmesh/crime_finder/crimes/byday?no_of_types=10'
    responseR = requests.get(url, headers={"Content-Type": "application/json"})
    #data = json.dumps(responseR.json())

    # Response object
    response = Response()
    response.headers["status"] = 200
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    data = json.dumps(responseR.json())
    response.data = data

    return response

@app.route('/crimeByYear', methods=['GET'])
def crimeByYear():

    url = swaggerHostName + '/cloudmesh/crime_finder/crimes/byyear?no_of_types=10'
    responseR = requests.get(url, headers={"Content-Type": "application/json"})
    #data = json.dumps(responseR.json())

    # Response object
    response = Response()
    response.headers["status"] = 200
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    data = json.dumps(responseR.json())
    response.data = data

    return response


#app.run(host='localhost', port=5050,debug=False)
app.run(host='0.0.0.0', port=5050,debug=False)


