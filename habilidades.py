from flask_restful import Resource
from flask import request
import json


lista_habilidades = [{'id': 0,
                      'habilidade': 'Python'
                      },
                     {'id': 1,
                      'habilidade': 'Java'
                      },
                     {'id': 2,
                      'habilidade': 'Flask'
                      },
                     {'id': 3,
                      'habilidade': 'Javascript'
                      },
                     {'id': 4,
                      'habilidade': 'PHP'
                      }]


class Habilidades(Resource):
    def get(self):
        return lista_habilidades

    def post(self):
        dados = json.loads(request.data)
        posicao = len(lista_habilidades)
        dados['id'] = posicao
        lista_habilidades.append(dados)
        return lista_habilidades[posicao]


class Skill(Resource):
    def get(self, id):
        try:
            response = lista_habilidades[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} inexistente'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido, procure o administrador da API'
            response = {'status': 'erro', 'mensagem': mensagem}
        return response

    def put(self, id):
        dadosSkill = json.loads(request.data)
        lista_habilidades[id] = dadosSkill
        return dadosSkill

    def delete(self, id):
        lista_habilidades.pop(id)
        return {'status': 'sucesso', 'mensagem': 'Registro deletado'}
