#!/usr/bin/python3

import requests
import json
from pprint import pprint

URL = "http://127.0.0.1:2224/"

newStudent = {
    "name": "HELL IN A HAND-BASKET",
    "skill level": "Pissing people off",
    "spirit animal": "Doggie...Poop",
    "super power": "THE ULTIMATE TROLL"

}

# json.dumps takes a python object and returns it as a JSON string
newStudent = json.dumps(newStudent)
                                                                   # don't need to json.dumps twice
post_resp = requests.post(URL + "newstudent", json=newStudent)     #json.dumps(newStudent))

# pretty-print the response back from our POST request
pprint(post_resp.text)

