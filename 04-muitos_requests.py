import requests
from pprint import pprint

def obter_request(url, params=None):
    """Faz uma requisição GET  e retorna a resposta em JSON"""
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as e:
        print(f"Erro no request: (e)")
        return None
    
def busca_id_estados():
    """obtém um dicionário de estados no formato {id_estado: nome_estado}"""

    url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"
    dados_estados = obter_request(url, params={"view": "nivelado"}) or []
    return {estado["UF-id"]: estado["UF-nome"] for estado in dados_estados}

def main():
   direct_estados = busca_id_estados()
   pprint(direct_estados) 

if __name__ == "__main__":
    main()