import json
import requests

token = 'token'
url = 'https://api.github.com/user'
user = 'user'


def buscar_dados():
    login = requests.Session()
    login.auth = (user, token)
    dados = json.loads(login.get(url).text)
    response = {'ID': dados['id'],
                'Login': dados['login'],
                'Nome': dados['name'],
                'Local': dados['location'],
                'E-mail': dados['email']}
    for i in response:
        print(i, ':', response[i])


if __name__ == '__main__':
    buscar_dados()
