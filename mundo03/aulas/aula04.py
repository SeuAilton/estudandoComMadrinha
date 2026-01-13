pessoas = {"nome": "Preludio", "sexo": "M", "idade": 29}
print(pessoas)
print(pessoas["nome"])
print(pessoas["sexo"])
print(pessoas["idade"])
print(f"A pessoa {pessoas['nome']} tem {pessoas['idade']} anos.")
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
# del pessoas["sexo"]
pessoas["nome"] = "SeuAilton"
pessoas["peso"] = 60

for k in pessoas.keys():
  print(k)

for v in pessoas.values():
  print(v)

for k, v in pessoas.items():
  print(f"{k} = {v}")

pessoas2 = {
    "nomes": ["Preludio", "Madrinha", "Moka"], 
    "idades": [29, 25, 665]
    }

print(pessoas2.values())

pessoas3 = [
    {
      "nome": "Preludio",
      "idade": 29,
      "sexo": "M"
      },
    {
      "nome": "Madrinha",
      "idade": 25,
      "sexo": "F"
      },
    {
      "nome": "Moka",
      "idade": 665,
      "sexo": "M"
      }
    ]

print(pessoas3[0]["nome"], pessoas3[1]["nome"], pessoas3[2]["nome"])

estado = dict()
brasil = list()
for c in range(3):
  estado["uf"] = input("Unidade Federativa: ").strip()
  estado["sigla"] = input("Sigla do Estado: ").strip()
  brasil.append(estado.copy())
print(brasil)
for e in brasil:
  for k, v in e.items():
    print(f"O campo {k} tem valor {v}")
  for v in e.values():
    print(v, end=" ")
  print()

