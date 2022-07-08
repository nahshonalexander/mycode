
import json
from flask import Flask, jsonify, redirect, request, url_for


app = Flask(__name__)

classinfo = [
    {
        "name": "LB",
        "skill level": "outstanding",
        "spirit animal": "Elephant",
        "super power": "Needle Projection",
    },
    {
        "name": "Mabel",
        "skill level": "phenomenal",
        "spirit animal": "Leopard",
        "super power": "Organic Constructs",
    },
    {
        "name": "Pat",
        "skill level": "pleasant",
        "spirit animal": "Albatross",
        "super power": "Prehensile Hair",
    },
    {
        "name": "Shon",
        "skill level": "pleasing",
        "spirit animal": "Alligator",
        "super power": "Prehensile Tail",
    }
]

@app.route("/", methods=["GET", "POST"])
def index():
    return jsonify(classinfo)


@app.route("/api/classinfo/",  methods=['GET'])
def get_classinfo():

    return jsonify(classinfo)


@app.route("/api/classinfo-details/", methods=['GET'])
def find_classinfo():
    details = {
        "name": "Shon",
        "skill level": "pleasing",
        "spirit animal": "GOD",
        "super power": "ALL KNOWING",
    }
    return jsonify(details)


@app.route("/newstudent", methods=["GET", "POST"])
def addjson():
    # request.method
    # request.form
    # request.arg

    data = request.json

    # data will contain the incoming json content
    data_conv = json.loads(data)

    # data conv is now a python object

    # classinfo.append(data_conv)
    # ah ok, here's the only issue
    # you're passing in the data, you're converting from json back to python... but you don't add it to the dictionary

    classinfo.append(data_conv)
    print(data_conv)

    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)

