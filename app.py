from flask import Flask
from flask_restful import Api
from recursos.shopping import lojas,loja

app = Flask(__name__)
api = Api(app)

api.add_resource(lojas, '/shopping')
api.add_resource(loja, '/shopping/<string:shopping_id>')

if __name__ == '__main__':
    app.run(debug=True)