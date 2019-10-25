'''
myapi.py 
- simple program to demo using a web API with requests Python module
- secondary function to demo how to write out received data to an HTML file 
'''
# Api Key = a0d9813bde0a43a29c5d778eacaab47d
import requests
import json
import pprint

# Find APIs at - https://apilist.fun/
# some will require an API key, boo hiss!

# cool geo example
# https://geo-info.co/?ref=apilist.fun
# example - https://geo-info.co/43.65,-79.40

# cool funny example
# https://funtranslations.com/api/chef
# https://api.funtranslations.com/translate/chef.json?text=I%20like%20upper%20canada%20college

# For any indentation errors, make sure there are no tabs (\t) by doing 
# a full replace of \t with 4 actual spaces

def writeHTML(data):
    myfile = open("myapi.html","w")
    myfile.write("<h1>JSON file returned by API call</h1>")
    myfile.write("<p>Copy and paste to <a href='https://jsoneditoronline.org/'>JSON editor</a> for pretty format.</p>")
    myfile.write(data)
    myfile.close()

def main():
    response = requests.get("https://geo-info.co/43.65,-79.40")
    if (response.status_code == 200):
        my_open_bbc_page = requests.get(response).json()
        my_article = my_open_bbc_page["articles"]
        my_results = []
        for ar in my_article:
            my_results.append(ar["title"])
        for i in range(len(my_results)):
            print(i + 1, my_results[i])
    else:
        data = "Error has occured"
        writeHTML(data)                
main()

