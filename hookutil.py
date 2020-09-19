# Standard library
from configparser import ConfigParser
import logging
from typing import Dict

# 3rd party modules
from flask import Flask, request
from werkzeug.exceptions import BadRequest

# Internal modules
from scriptmanager import run_script

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level="INFO"
    )

config = ConfigParser()
config.read("serverconfig.ini")
HOST = config["DEFAULT"]["HOST"]
PORT = config["DEFAULT"]["PORT"]
API_KEY = config["DEFAULT"]["API_KEY"]

app = Flask(__name__)


@app.route("/health")
def health():
    return "Ok!"


@app.route("/", methods=["POST"])
def hook():
    data = json_controller("APIKey", "script")
    if(data["APIKey"] == API_KEY):
        run_script(data["script"])
    return "Ok!", 200


def json_controller(*keys) -> Dict:
    data = request.get_json()
    for key in keys:
        if key not in data:
            raise BadRequest("Malformed json")
    return data


if __name__ == "__main__":
    app.run(host=HOST, port=PORT)
