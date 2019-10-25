import requests
import json
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'OmFlZDI5OGJlZjY0YzkzNTk5OGIwYTZlZWQ3NWQwZjY5'
security_api = intrinio_sdk.SecurityApi()

def writeHTML(data):
    myfile = open("playerAPI.html","w") # use "a" to "append"
    
    ############### CSS
    
    myfile.write("""
    <html>

      <head>
        <title> MY PAGE </title>
      </head>

      <body>
        <font size="3" color="red">This is some text!</font>
        <font size="2" color="blue">This is some text!</font>
        <font face="verdana" color="green">This is some text!</font>
        <h1>Welcome to My Soccer Home Page</h1>

        <p>Go to <a href='https://apilist.fun/api/the-sports-db'>The Sports DB</a> for API Info.</p>

        <h1 style="background-color:DodgerBlue;">Here is player you requested</h1>

        <p>Player name: """+ data+"""</p>

        <p style="font-family:verdana">This is a paragraph.</p>

        <p style="font-family:'Courier New'">This is another paragraph.</p>

      </body>

    </html>""")


    ################# CSS
    myfile.close()

def main():

    identifier = 'AAPL'
    start_date = '2018-01-01' 
    end_date = '2019-01-01'
    frequency = 'daily' 
    page_size = 100 
    next_page = '' 

    try:
        api_response = security_api.get_security_stock_prices(identifier, start_date=start_date, end_date=end_date, frequency=frequency, page_size=page_size, next_page=next_page)
        data = pprint(api_response)
        writeHTML(data)
    except ApiException as e:
        print("Exception when calling SecurityApi->get_security_stock_prices: %s\r\n" % e)

main()