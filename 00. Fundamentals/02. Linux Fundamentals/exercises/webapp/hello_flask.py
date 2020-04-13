'''
  09/01/2015
  Author: Makerbro
  Platforms: Raspberry Pi (Raspbian)
  Language: Python
  File: application.py
  ------------------------------------------------------------------------
  Description: 
  Simple example of using Flask to run a simple webserver that renders a 
  simple page with a "Hello World" message.
  ------------------------------------------------------------------------
  Please consider buying products from ACROBOTIC to help fund future
  Open-Source projects like this! We'll always put our best effort in every
  project, and release all our design files and code for you to use. 
  https://acrobotic.com/
  ------------------------------------------------------------------------
  License:
  Beerware License; if you find the code useful, and we happen to cross 
  paths, you're encouraged to buy us a beer. The code is distributed hoping
  that you in fact find it useful, but  without warranty of any kind.
'''
from flask import Flask         # Import the Flask class from the flask module

# The function is given a name which is also used to generate URLs 
def hello_world():              
    return 'Hello World!'

app = Flask(__name__)           # Instantiate a Flask object

app.add_url_rule('/', 'home', view_func=hello_world)

# use the run() function to run the local server with our application
if __name__ == '__main__':
#    app.run()                  # Only accessible from this machine
    app.run(host='0.0.0.0')     # Accessible from the outside world
