from flask_restful import Resource, reqparse

lojasShopping = [
    {
        'shopping_id': 'Marisa',
        'nome': 'Marisa',
        'nota': 4.9,
        'telefone': 11985476321,
        'piso': 1 },
    {
        'shopping_id': 'Pernambucanas',
        'nome': 'Pernambucanas',
        'nota': 4.8,
        'telefone': 11965428379,
        'piso': 0 },
    {
        'shopping_id': 'Kadu',
        'nome': 'Kadu',
        'nota': 4.1,
        'telefone': 1185427619,
        'piso': 1 },
]

class lojas(Resource):
    def get(self):
        return {'loja': lojasShopping}

class loja(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('nota')
    argumentos.add_argument('telefone')
    argumentos.add_argument('piso')

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
        return {'message':'Loja Deletada'}