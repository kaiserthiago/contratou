import algoliasearch_django as algoliasearch
from algoliasearch_django import AlgoliaIndex
from django.apps import AppConfig


class ContratouConfig(AppConfig):
    name = 'contratou'

    def ready(self):
        Profissional = self.get_model('Profissional')
        algoliasearch.register(Profissional, ProfissionalIndex)


class ProfissionalIndex(AlgoliaIndex):
    fields = ('id', 'nome', 'cpf', 'rg', 'orgao_expeditor', 'data_nascimento', 'logradouro', 'complemento',
              'cidade', 'uf', 'cep', 'email', 'telefone', 'foto', 'area')
    settings = {'searchableAttributes': ['area', ]}
    index_name = 'profissional_index'
