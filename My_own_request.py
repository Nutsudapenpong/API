import requests 
import json
import os

if __name__ == "__main__":

    url = 'http://127.0.0.1:8080/'
    filename = 'papture.png'
    file = {'file': open(filename, 'rb')}
    x = requests.post(url, files = file)

    print(x.text)