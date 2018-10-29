from flask import Flask, render_template, redirect, jsonify, json
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
import numpy as np
from flask_cors import CORS, cross_origin

engine = create_engine("sqlite:///stocks.sqlite")

Base = automap_base()
Base.prepare(engine, reflect=True)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/julie')
def julie():
    table = Base.classes.marketCap
    session = Session(engine)
    results = session.query(table).all()
    tableList = []
    for column in results:
        tableData = {}
        tableData["Company"] = column.Company
        tableData["Sector"] = column.Sector
        tableData["MktCap2013"] = column.MktCap2013
        tableData["Debt"] = column.Debt
        tableData["MktCap2018"] = column.MktCap2018
        tableData["Changevs2015"] = column.Changevs2015
        tableData["Change"] = column.Change
        tableData["Stake"] = column.Stake
        tableData["Latitude"] = column.Latitude
        tableData["Longitude"] = column.Longitude
        tableList.append(tableData)
    return render_template("julie.html", data = json.dumps(tableList))

@app.route('/elliot')
def elliot():
    table = Base.classes.histData
    session = Session(engine)
    results = session.query(table).all()
    tableList = []
    for column in results:
        tableData = {}
        tableData["Date"] = column.date
        tableData["Price"] = column.price
        tableList.append(tableData)
    return render_template("elliot.html", data = json.dumps(tableList))

@app.route('/nick')
def nick():
    return render_template("nick.html")

@app.route('/rose')
def rose():
    return render_template("rosev.html")

@app.route('/roseData')
def roseData():
    table = Base.classes.rose
    session = Session(engine)
    results = session.query(table).all()
    tableList = []
    for column in results:
        tableData = {}
        tableData["symbol"] = column.symbol
        tableData["name"] = column.name
        tableData["sector"] = column.sector
        tableData["price"] = column.price
        tableData["priceEarnings"] = column.priceEarnings
        tableData["dividendYield"] = column.dividendYield
        tableData["earningsShare"] = column.earningsShare
        tableData["yearTrailingLow"] = column.yearTrailingLow
        tableData["yearTrailingHigh"] = column.yearTrailingHigh
        tableData["cap"] = column.cap
        tableData["ebitda"] = column.ebitda
        tableData["priceSales"] = column.priceSales
        tableData["priceBook"] = column.priceBook
        tableList.append(tableData)
    return jsonify(tableList)

@app.route('/nickData')
def nickData():
    table = Base.classes.wL
    session = Session(engine)
    results = session.query(table).all()
    tableList = []
    for column in results:
        tableData = {}
        tableData["companyName"] = column.companyName
        tableData["sector"] = column.sector
        tableData["marCap2013"] = column.marCap2013
        tableData["marCap2018"] = column.marCap2018
        tableData["difference"] = column.difference
        tableData["percChange"] = column.percChange
        tableData["category"] = column.category
        tableData["Winner"] = column.Winner
        tableData["Loser"] = column.Loser
        tableList.append(tableData)
    return jsonify(tableList)

if __name__ == "__main__":
    app.run(debug=True)