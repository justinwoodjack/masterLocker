## 
##
## http service that runs continously, and serves up a json-array of results from a mongoDB
## see the readme for more information
##
import os
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import pymongo

#This is used to produce a properly formated json-array,
from bson.json_util import dumps

port = int(os.environ.get('PORT', '8080'))

#port options for webServer
from tornado.options import define, options
define("port", default=port, help="run on the given port", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [(r"/(\w+)", RequestHandler)]
		mongohq_url = 'mongodb://pull:pull@dharma.mongohq.com:10014/app16815592'
		connection = pymongo.Connection(mongohq_url)
		db = connection.app16815592
        tornado.web.Application.__init__(self, handlers, debug=True)


def getMONGO():
	coll = self.application.db.location
    urlInput = str(urlInput)
        query = {}
        mongoResults = coll.find( query, {"_id":0} )
        if mongoResults:
        	results = (dumps(mongoResults))
            return(results)
        else:
            return("No Results")



class RequestHandler(tornado.web.RequestHandler):
    def get(self, urlInput):
        
        if urlInput == "home":
        	#return html
        elif urlInput == "get"
            self.write( getMONGO() )
        else:
            self.set_status(404)
            self.write({"error": "word not found"})



if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()



