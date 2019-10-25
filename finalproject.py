import gmplot
import geopy.distance
import os
import requests
import gmaps
import urllib.request
import json

def conversion(apiKey, address):
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'
           .format(address.replace(' ','+'), apiKey))
    try:
        response = requests.get(url)
        resp_json = response.json()
        lat = resp_json['results'][0]['geometry']['location']['lat']
        lng = resp_json['results'][0]['geometry']['location']['lng']
    except:
        print('ERROR: {}'.format(address))
        lat = 0
        lng = 0
    return lat, lng

def conversion2(apiKey, address):
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'
           .format(address.replace(' ','+'), apiKey))
    try:
        response = requests.get(url)
        resp_json = response.json()
        lat2 = resp_json['results'][0]['geometry']['location']['lat']
        lng2 = resp_json['results'][0]['geometry']['location']['lng']
    except:
        print('ERROR: {}'.format(address))
        lat = 0
        lng = 0
    return lat2, lng2

def distancemeasure(home, target):
    geopy.distance.vincenty(home, target).km

def directions(home, target, movement):
    # endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
    # apikey = 'AIzaSyDcD5Aoda6GhubM21FBSnPL_c5YJCE0XW8'
    # nav_request = 'origin={}&destination={}&key={}'.format(home,target,apikey)
    # request = endpoint + nav_request
    # response = urllib.request.urlopen(request).read()
    # directions = json.loads(response)
    print("This function is currently unavailable")
if __name__ == '__main__':
    apikey = 'AIzaSyDcD5Aoda6GhubM21FBSnPL_c5YJCE0XW8'

    while True:
        print("Please type your address in the format: number road, city, province") 
        address = input("")
        lat, lng = conversion(apikey, address)
        print('{} Coordinates:\nLatitude:  {}°\nLongitude: {}°'.format(address,lat,lng))
        basemap = gmplot.GoogleMapPlotter(lat, lng, 13)

        print("Please type the address of the target location in the format: number road, city, province")
        location = input("")
        lat2, lng2 = conversion2(apikey, location)
        print('{} Coordinates:\nLatitude:  {}°\nLongitude: {}°'.format(location,lat2,lng2))

        print("1. See the map")
        print("2. Find the distance")
        print("3. Get directions")
        choice = int(input("Please select your choice "))

        if choice == 1:
            latlist = lat, lat2
            lnglist = lng, lng2
            basemap.scatter(latlist, lnglist, '# FF0000', size = 200, marker = False )
            basemap.draw("/Users/homework/desktop/gitrepo/y10coding/map.html")
            print("Opening the map, please note the black dots represent the locations you have selected")
            os.system("open map.html")
            input("Press enter to restart the code")
            os.system("clear")
        elif choice ==2:
            home = (lat, lng)
            target = (lat2, lng2)
            print(target)
            distance = distancemeasure(home, target)
            myfile = open("distance.html","w")
            myfile.write("""
            <html>

              <head>
                <title> Distance </title>
                <style>
                body {
                    background-color: #0000ff
                }
                .button {
                    background-color: #4CAF50;
                    border: none;
                    color: white;
                    padding: 15px 25px;
                    text-align: center;
                    font-size: 16px;
                    cursor: pointer;
                }

                .button:hover {
                    background-color: green;
                }
                </style>

              </head>

              <body>
                <center><h1>Measure Distance</h1></center>
                <center><h1>The distance is """+str(distance)+""" km between the two points.</h1></center>

              </body>

            </html>""")
            myfile.close()
            print("Note if the distance is too small the website will say none")
            os.system("open distance.html")
            input("Press enter to restart the code")
            os.system("clear")
        elif choice ==3:
            home = (lat, lng)
            target = (lat2, lng2)
            print("1. Driving")
            print("2. Biking")
            print("3. Walking")
            print("4. Transit")
            mode = int(input("What mode of transport will you be taking today? "))
            if mode == 1:
                print("You are driving today")
                movement = 'driving'
                directions(home,target,movement)
            elif mode == 2:
                print("You are biking today")
                movement = 'biking'
                directions(home,target,movement)
            elif mode == 3:
                print("You are walking today")
                movement = 'walking'
                directions(home,target,movement)
            elif mode == 4:
                print("You are taking transit today")
                movement = 'transit'
                directions(home,target,movement)
            else:
                print("This is not a valid option")
            input("Press enter to restart the code")
            os.system("clear")
        else:
            print("This is not a valid choice")
            input("Press enter to restart the code")
            os.system("clear")





