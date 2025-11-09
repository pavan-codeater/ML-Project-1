from flask import Flask
from housing.logger import logging
from housing.exception import HousingException
import sys
app=Flask(__name__)

@app.route("/",methods=["GET"])
def index():
    try:
        raise Exception("I am testing Custom Exception")
    except Exception as e:
        housing=HousingException(e,sys)
        logging.info(housing.error_message)
        logging.info("we are testing logger package")
    return "House Price prediction Project"

if __name__ == "__main__":
    app.run(debug=True)