from flask import Flask
from flask_restful import Api
from recursos.academia import lojas,loja

app = Flask(__name__)
api = Api(app)

api.add_resource(lojas, '/academia')
api.add_resource(loja, '/academia/<string:shopping_id>')

if __name__ == '__main__':
    app.run(debug=True)