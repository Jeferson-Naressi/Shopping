from flask_restful import Resource, reqparse

academias = [
    {
        'academia_id': 'smart',
        'nome': 'Smart Academia',
        'nota': 8.9,
        'valor': 119.99,
        'cidade': 'São Paulo'},
    {
        'academia_id': 'nocaute',
        'nome': 'Nocaute Academia',
        'nota': 8.5,
        'valor': 99.99,
        'cidade': 'Osasco'},
    {
        'academia_id': 'cross',
        'nome': 'Cross Life Academia',
        'notas': 9.0,
        'valor': 109.99,
        'cidade': 'Campinas'},
]

class Academias(Resource):
    def get(self):
        return {'academia': academias}

class Academia(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')

    def encontrarAcademia(academia_id):
        for academia in academias:
            if academia['academia_id'] == academia_id:
                return academia
        return None
    def get(self,academia_id):
        academia = Academia.encontrarAcademia(academia_id)
        if academia:
            return academia
        return {'message':'Academia not found.'}, 404
    def post(self,academia_id):
        dados = Academia.argumentos.parse_args()
        nova_academia = {
            'academia_id': academia_id,
            'nome': dados['nome'],
            'estrelas': dados['nome'],
            'diaria': dados['diaria'],
            'cidade': dados['cidade'],
        }
        academias.append(nova_academia)
        return nova_academia,200

    def put(self,academia_id):
        dados = Academia.argumentos.parse_args()
        nova_academia = {'academia_id': academia_id, **dados}
        academia = Academia.encontrarAcademia(academia_id)

        if academia:
            academia.update(nova_academia)
            return nova_academia,200
        academias.append(nova_academia)
        return nova_academia,201
    def delete(self,academia_id):
        global academias
        academias = [academia for academia in academias if academia['academia_id'] != academia_id]
        return {'massage':'Academia Deletada'}