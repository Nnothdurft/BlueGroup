from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import PyMongo
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
import numpy

engine = create_engine("sqlite:///test.sqlite")

Base = automap_base()
Base.prepare(engine, reflect=True)
table13 = Base.classes.tests

session = Session(engine)

app = Flask(__name__)
# mongo = PyMongo(app, uri="mongodb://localhost:27017/test")

results = session.query(table13.test1).all()
all_names = list(np.ravel(results))
print(all_names)
# everything = []
# print(results)
# for thing in results:
#     thisThing = {}
#     thisThing["test1"] = results.test1
#     thisThing["test2"] = results.test2
#     everything.append(thisThing)

# @app.route('/')
# def test():
#     results = session.query(table13).all()
#     everything = []
#     print(results)
#     for thing in results:
#         thisThing = {}
#         thisThing["test1"] = results.test1
#         thisThing["test2"] = results.test2
#         everything.append(thisThing)
#     # everything = list(np.ravel(results))
#     return jsonify(everything)
# def index():
#     data = {}
#     headers = []
#     count = 0
#     testdb = mongo.db.histData
#     files = ["2013.csv", "2014.csv", "2015.csv", "2016.csv", "2017.csv", "2018.csv"]
#     for f in files:
#         with open("S&P.csv") as csvFile:
#             reader = csv.reader(csvFile)
#             for row in reader:
#                 if count == 0:
#                     headers = row
#                 else:
#                     print(row[1])
#                     row[1] = row[1].replace(",", "")
#                     data = {headers[0]:row[0],headers[1]:float(row[1])}
#                     if testdb.find({headers[0]:row[0]}):
#                         testdb.update_one({headers[0]:row[0]}, {"$set":data}, upsert=True)
#                     else:
#                         testdb.insert_one(data)
#                 count += 1
#     newData = mongo.db.test.find()
#     results = []
#     for item in newData:
#         print(item)
#         results.append(item)
#     # data = JSONEncoder().encode(results)
#     # with open("data.json", "w") as outFile:
#     #     json.dump(data, outFile)
#     data = results
#     print(data)
#     return render_template("index.html", data = data)

@app.route('/loadCSV')
def loadCSV():
    data = {}
    with open("Unit Rebuild.csv") as csvFile:
        csvData = csv.reader(csvFile)
        for item in csvData.iteritem:
            print(item)
    return data

if __name__ == "__main__":
    app.run(debug=True)