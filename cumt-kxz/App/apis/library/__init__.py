from flask_restful import Api

from App.apis.library.library_api import Library

library_api = Api(prefix='/lib')

library_api.add_resource(Library, '/book')