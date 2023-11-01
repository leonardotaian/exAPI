import json, requests

id = int(input("Personagem: "))

url = f"https://rickandmortyapi.com/api/character/{id}"

resp = requests.get(url)

conteudo = json.loads(resp.content)

if resp.status_code == 200:
    print(f"Nome do personagem {id}: {conteudo['name']}")
else: 
    print(f"Personagem não encontrado")