from flask import Flask, render_template
import urllib.request, json

app = Flask(__name__)

@app.route("/")
def picture():
    #read key from file
    key = open("key_nasa.txt").read()
    #append to url string
    url_string = "https://api.nasa.gov/planetary/apod?api_key=" + key
    #make HTTP request to API using key
    jsonurl = urllib.request.urlopen(url_string)
    #store JSON file as text
    text = json.loads(jsonurl.read())
    #get src for main.html
    src_string = text["url"]
    return render_template("main.html", src = src_string)

if __name__ == '__main__':
    app.debug = True
    app.run()
