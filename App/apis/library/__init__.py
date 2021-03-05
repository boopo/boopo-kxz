from flask_restful import Api

from App.apis.library.library_api import Library, OnShelf, BookImage

library_api = Api(prefix='/lib')

library_api.add_resource(Library, '/book')
library_api.add_resource(OnShelf, '/status')
library_api.add_resource(BookImage, '/image')

library_api.add_resource(libraryList, '/libraryList')
library_api.add_resource(libraryHistoryList, '/libraryHistoryList')
library_api.add_resource(libraryFavorite, '/libraryFavorite')