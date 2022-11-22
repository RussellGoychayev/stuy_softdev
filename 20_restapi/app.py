from flask import Flask
import urllib.request, json

app = Flask(__name__)

@app.route("/")
def picture():
    #read key from file
    key = open("key_nasa.txt").read()
    #append to url string
    urlString = "https://api.nasa.gov/planetary/apod?api_key=" + key
    #make HTTP request to API using key
    jsonurl = urllib.request.urlopen(urlString)
    text = json.loads(jsonurl.read()) # <-- read from it    print(dict)
    return "hello"

if __name__ == '__main__':
    app.debug = True
    app.run()
