import os
import datetime
import pymongo
from mongodb import db
from bson.json_util import dumps
from bson.json_util import loads
import ast
from urlparse import urlparse, parse_qs  #url parsing for query

import pprint


def getMONGO():
	coll = db.events
	mongoResults = coll.find({},{'_id':0})
	if mongoResults:
	    results = dumps(mongoResults)
	    return(results)
	else:
	    return('No Results')

def postNewUser(data):
	coll = db.users
	coll.insert(data)
	return("Successful mongodb upload bitches!!! ")

def getLiveMONGO():
	data=[]
	coll = db.events
	query = coll.distinct('name')
	queryDate = datetime.datetime.utcnow() - datetime.timedelta(seconds = 60)
	print(queryDate)
	for person in query:
		personinfo = coll.find({'name': person, 'date':{'$gt':queryDate}},{'_id': 0}).sort('date',1).limit(1)
		getResults = dumps(personinfo)
		try:
			data.append( ast.literal_eval(getResults)[0] )
		except IndexError:
			s=1#print('index error!!!')
	if data:
	    return( dumps(data) )
	else:
	    return( str(queryDate) + "     No results" )



def getCurrentMONGO():
	data=[]
	coll = db.events	
	query = coll.distinct('name')
	for person in query:
		personinfo = coll.find({'name': person},{'_id': 0}).sort('date',1).limit(1)
		getResults = dumps(personinfo)
		data.append( ast.literal_eval(getResults)[0] )
	if data:
	    return( dumps(data) )
	else:
	    return( 'No Results' )


def getTailsMONGO():
	coll = db.events
	mongoResults = coll.find({},{'_id':0})
	if mongoResults:
	    results = dumps(mongoResults)
	    return(results)
	else:
	    return('No Results')

def postLocation(newLocation):
	coll = db.events
	newLocation['date'] = datetime.datetime.utcnow()
	coll.insert(newLocation)
	return("Successful mongodb upload bitches!!! ")

def dumpallpoints():
	data=[]
	coll = db.events
	for point in db.events.find():
		data.append( point )

	if data:
		return( dumps(data) )
	else:
		return( 'No Results' )