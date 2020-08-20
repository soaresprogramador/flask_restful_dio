from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidades, Skill
import json

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {'id': '0',
     'nome': 'Paulo',
     'habilidades': ['Python', 'Flask']
     },

    {'id': '1',
     'nome': 'Marcos',
     'habilidades': ['Javascript', 'ReactJs']
     },
]


# devolve, altera e deleta um desenvolvedor pelo id
class Desenvolvedor(Resource):

    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} inexistente'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido, procure o administrador da API'
            response = {'status': 'erro', 'mensagem': mensagem}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status': 'sucesso', 'mensagem': 'Registro deletado'}


# lista os desenvolvedores e insere novo registro
class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]


api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/')
api.add_resource(Skill, '/habilidades/<int:id>/')

if __name__ == '__main__':
    app.run(debug=True)
