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
    table = Base.classes.histData
    session = Session(engine)
    results = session.query(table).all()
    tableList = []
    for column in results:
        tableData = {}
        tableData["Date"] = column.Date
        tableData["Price"] = column.Price
        tableList.append(tableData)
    return jsonify(tableList) #render_template("index.html", data = json.dumps(tableList))

@app.route('/year2013')
def year2013():
    table = Base.classes.year2013
    session = Session(engine)
    results = session.query(table).all()
    tableList = []
    for column in results:
        tableData = {}
        tableData["constituents"] = column.constituents
        tableData["companyName"] = column.companyName
        tableData["sector"] = column.sector
        tableData["industryGroup"] = column.industryGroup
        tableData["industry"] = column.industry
        tableData["subIndustry"] = column.subIndustry
        tableData["dividendAdjustedSplitAdjustedClosingStockPrice"] = column.dividendAdjustedSplitAdjustedClosingStockPrice
        tableData["bevEbitdaMultiples"] = column.bevEbitdaMultiples
        tableData["priceEarningsMultiples"] = column.priceEarningsMultiples
        tableData["priceTangibleBook"] = column.priceTangibleBook
        tableData["dividendYield"] = column.dividendYield
        tableData["marketCapitalization"] = column.marketCapitalization
        tableData["headquarterLocation"] = column.headquarterLocation
        tableData["actual2018"] = column.actual2018
        tableData["estimated2018"] = column.estimated2018
        tableData["actual2017"] = column.actual2017
        tableData["estimated2017"] = column.estimated2017
        tableData["actual2016"] = column.actual2016
        tableData["estimated2016"] = column.estimated2016
        tableData["actual2015"] = column.actual2015
        tableData["estimated2015"] = column.estimated2015
        tableData["actual2014"] = column.actual2014
        tableData["estimated2014"] = column.estimated2014
        tableList.append(tableData)
    return jsonify(tableList)

@app.route('/year2014')
def year2014():
    table = Base.classes.year2014
    session = Session(engine)
    results = session.query(table).all()
    tableList = []
    for column in results:
        tableData = {}
        tableData["constituents"] = column.constituents
        tableData["companyName"] = column.companyName
        tableData["sector"] = column.sector
        tableData["industryGroup"] = column.industryGroup
        tableData["industry"] = column.industry
        tableData["subIndustry"] = column.subIndustry
        tableData["dividendAdjustedSplitAdjustedClosingStockPrice"] = column.dividendAdjustedSplitAdjustedClosingStockPrice
        tableData["bevEbitdaMultiples"] = column.bevEbitdaMultiples
        tableData["priceEarningsMultiples"] = column.priceEarningsMultiples
        tableData["priceTangibleBook"] = column.priceTangibleBook
        tableData["dividendYield"] = column.dividendYield
        tableData["marketCapitalization"] = column.marketCapitalization
        tableData["headquarterLocation"] = column.headquarterLocation
        tableData["actual2018"] = column.actual2018
        tableData["estimated2018"] = column.estimated2018
        tableData["actual2017"] = column.actual2017
        tableData["estimated2017"] = column.estimated2017
        tableData["actual2016"] = column.actual2016
        tableData["estimated2016"] = column.estimated2016
        tableData["actual2015"] = column.actual2015
        tableData["estimated2015"] = column.estimated2015
        tableData["actual2014"] = column.actual2014
        tableData["estimated2014"] = column.estimated2014
        tableList.append(tableData)
    return jsonify(tableList)

@app.route('/year2015')
def year2015():
    table = Base.classes.year2015
    session = Session(engine)
    results = session.query(table).all()
    tableList = []
    for column in results:
        tableData = {}
        tableData["constituents"] = column.constituents
        tableData["companyName"] = column.companyName
        tableData["sector"] = column.sector
        tableData["industryGroup"] = column.industryGroup
        tableData["industry"] = column.industry
        tableData["subIndustry"] = column.subIndustry
        tableData["dividendAdjustedSplitAdjustedClosingStockPrice"] = column.dividendAdjustedSplitAdjustedClosingStockPrice
        tableData["bevEbitdaMultiples"] = column.bevEbitdaMultiples
        tableData["priceEarningsMultiples"] = column.priceEarningsMultiples
        tableData["priceTangibleBook"] = column.priceTangibleBook
        tableData["dividendYield"] = column.dividendYield
        tableData["marketCapitalization"] = column.marketCapitalization
        tableData["headquarterLocation"] = column.headquarterLocation
        tableData["actual2018"] = column.actual2018
        tableData["estimated2018"] = column.estimated2018
        tableData["actual2017"] = column.actual2017
        tableData["estimated2017"] = column.estimated2017
        tableData["actual2016"] = column.actual2016
        tableData["estimated2016"] = column.estimated2016
        tableData["actual2015"] = column.actual2015
        tableData["estimated2015"] = column.estimated2015
        tableData["actual2014"] = column.actual2014
        tableData["estimated2014"] = column.estimated2014
        tableList.append(tableData)
    return jsonify(tableList)

@app.route('/year2016')
def year2016():
    table = Base.classes.year2016
    session = Session(engine)
    results = session.query(table).all()
    tableList = []
    for column in results:
        tableData = {}
        tableData["constituents"] = column.constituents
        tableData["companyName"] = column.companyName
        tableData["sector"] = column.sector
        tableData["industryGroup"] = column.industryGroup
        tableData["industry"] = column.industry
        tableData["subIndustry"] = column.subIndustry
        tableData["dividendAdjustedSplitAdjustedClosingStockPrice"] = column.dividendAdjustedSplitAdjustedClosingStockPrice
        tableData["bevEbitdaMultiples"] = column.bevEbitdaMultiples
        tableData["priceEarningsMultiples"] = column.priceEarningsMultiples
        tableData["priceTangibleBook"] = column.priceTangibleBook
        tableData["dividendYield"] = column.dividendYield
        tableData["marketCapitalization"] = column.marketCapitalization
        tableData["headquarterLocation"] = column.headquarterLocation
        tableData["actual2018"] = column.actual2018
        tableData["estimated2018"] = column.estimated2018
        tableData["actual2017"] = column.actual2017
        tableData["estimated2017"] = column.estimated2017
        tableData["actual2016"] = column.actual2016
        tableData["estimated2016"] = column.estimated2016
        tableData["actual2015"] = column.actual2015
        tableData["estimated2015"] = column.estimated2015
        tableData["actual2014"] = column.actual2014
        tableData["estimated2014"] = column.estimated2014
        tableList.append(tableData)
    return jsonify(tableList)

@app.route('/year2017')
def year2017():
    table = Base.classes.year2017
    session = Session(engine)
    results = session.query(table).all()
    tableList = []
    for column in results:
        tableData = {}
        tableData["constituents"] = column.constituents
        tableData["companyName"] = column.companyName
        tableData["sector"] = column.sector
        tableData["industryGroup"] = column.industryGroup
        tableData["industry"] = column.industry
        tableData["subIndustry"] = column.subIndustry
        tableData["dividendAdjustedSplitAdjustedClosingStockPrice"] = column.dividendAdjustedSplitAdjustedClosingStockPrice
        tableData["bevEbitdaMultiples"] = column.bevEbitdaMultiples
        tableData["priceEarningsMultiples"] = column.priceEarningsMultiples
        tableData["priceTangibleBook"] = column.priceTangibleBook
        tableData["dividendYield"] = column.dividendYield
        tableData["marketCapitalization"] = column.marketCapitalization
        tableData["headquarterLocation"] = column.headquarterLocation
        tableData["actual2018"] = column.actual2018
        tableData["estimated2018"] = column.estimated2018
        tableData["actual2017"] = column.actual2017
        tableData["estimated2017"] = column.estimated2017
        tableData["actual2016"] = column.actual2016
        tableData["estimated2016"] = column.estimated2016
        tableData["actual2015"] = column.actual2015
        tableData["estimated2015"] = column.estimated2015
        tableData["actual2014"] = column.actual2014
        tableData["estimated2014"] = column.estimated2014
        tableList.append(tableData)
    return jsonify(tableList)

@app.route('/year2018')
def year2018():
    table = Base.classes.year2018
    session = Session(engine)
    results = session.query(table).all()
    tableList = []
    for column in results:
        tableData = {}
        tableData["constituents"] = column.constituents
        tableData["companyName"] = column.companyName
        tableData["sector"] = column.sector
        tableData["industryGroup"] = column.industryGroup
        tableData["industry"] = column.industry
        tableData["subIndustry"] = column.subIndustry
        tableData["dividendAdjustedSplitAdjustedClosingStockPrice"] = column.dividendAdjustedSplitAdjustedClosingStockPrice
        tableData["bevEbitdaMultiples"] = column.bevEbitdaMultiples
        tableData["priceEarningsMultiples"] = column.priceEarningsMultiples
        tableData["priceTangibleBook"] = column.priceTangibleBook
        tableData["dividendYield"] = column.dividendYield
        tableData["marketCapitalization"] = column.marketCapitalization
        tableData["headquarterLocation"] = column.headquarterLocation
        tableData["actual2018"] = column.actual2018
        tableData["estimated2018"] = column.estimated2018
        tableData["actual2017"] = column.actual2017
        tableData["estimated2017"] = column.estimated2017
        tableData["actual2016"] = column.actual2016
        tableData["estimated2016"] = column.estimated2016
        tableData["actual2015"] = column.actual2015
        tableData["estimated2015"] = column.estimated2015
        tableData["actual2014"] = column.actual2014
        tableData["estimated2014"] = column.estimated2014
        tableList.append(tableData)
    return jsonify(tableList)

if __name__ == "__main__":
    app.run(debug=True)