import requests

from django.test import TestCase
from rest_framework.test import RequestsClient


class TestApiVough(TestCase):
    """Classe de testes unitários das rotas

    Instructions:
        Para executar os testes, basta executar no terminal o comando:
        python manage.py test
    """

    def test_get_org_existente(self):
        client = RequestsClient()
        response = client.get('http://localhost:8000/api/orgs/instruct-br')
        self.assertEqual(response.status_code, 200)

    def test_get_org_inexistente(self):
        client = RequestsClient()
        response = client.get('http://localhost:8000/api/orgs/abcderfsd12321233')
        self.assertEqual(response.status_code, 404)

    def test_get_quantidade_orgs(self):
        client = RequestsClient()
        insert_org_1 = client.get('http://localhost:8000/api/orgs/instruct-br')
        insert_org_2 = client.get('http://localhost:8000/api/orgs/microsoft')
        response = client.get('http://localhost:8000/api/orgs/')
        tamanho = len(response.json())
        self.assertEqual(tamanho, 2)

    def test_get_delete_orgs(self):
        client = RequestsClient()
        insert_org_1 = client.get('http://localhost:8000/api/orgs/instruct-br')
        insert_org_2 = client.delete('http://localhost:8000/api/orgs/instruct-br')
        response = client.get('http://localhost:8000/api/orgs/')
        tamanho = len(response.json())
        self.assertEqual(tamanho, 0)


