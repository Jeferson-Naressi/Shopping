from flask_restful import Resource, reqparse

lojasShopping = [
    {
        'shopping_id': 'smart',
        'nome': 'Smart Academia',
        'nota': 8.9,
        'valor': 119.99,
        'cidade': 'São Paulo'},
    {
        'shopping_id': 'nocaute',
        'nome': 'Nocaute Academia',
        'nota': 8.5,
        'valor': 99.99,
        'cidade': 'Osasco'},
    {
        'shopping_id': 'cross',
        'nome': 'Cross Life Academia',
        'notas': 9.0,
        'valor': 109.99,
        'cidade': 'Campinas'},
]

class lojas(Resource):
    def get(self):
        return {'academia': lojasShopping} #mudas dps no postman tbm

class loja(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('nota')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')

    def encontrarLojas(shopping_id):
        for loja in lojasShopping:
            if loja['shopping_id'] == shopping_id:
                return loja
        return None
    def get(self,shopping_id):
        lojas = loja.encontrarLojas(shopping_id)
        if lojas:
            return lojas
        return {'message':'Loja not found.'}, 404
    def post(self,shopping_id):
        dados = loja.argumentos.parse_args()
        nova_Loja = {'shopping_id': shopping_id, **dados}
        lojasShopping.append(nova_Loja)
        return nova_Loja,200

    def put(self,shopping_id):
        dados = loja.argumentos.parse_args()
        nova_Loja = {'shopping_id': shopping_id, **dados}
        lojasShopping = loja.encontrarLojas(shopping_id)

        if lojasShopping:
            lojasShopping.update(nova_Loja)
            return nova_Loja,200
        lojasShopping.append(nova_Loja)
        return nova_Loja,201
    def delete(self,shopping_id):
        global lojasShopping
        lojasShopping = [lojas for lojas in lojasShopping if lojas['shopping_id'] != shopping_id]
        return {'massage':'Loja Deletada'}