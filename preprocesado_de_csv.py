import os
import json

# Ya lo ejecuté, 

os.chdir("/home/hcastorp/Escritorio/proyecto celsius")

with open("celsius_proof_of_community_18.6.21-25.6.21.csv","r", encoding="utf-8",newline="") as archivo:
    encabezado = archivo.readline()
    rdo = []
    for linea in archivo.readlines() :
        indice = linea.index(",")
        dato = linea[indice+1:]
        parseado = json.loads(dato)
        parseado["tx"] = linea[:indice]
        rdo.append(parseado)

print(rdo[0].keys())
print(rdo[0]["BTC"].keys())
print(rdo[0]["BTC"]["totalInterestInUsd"])
print(rdo[0]["BTC"]["earningInterestInCel"])
print(rdo[0]["tx"])

with open("celsius_proof_of_community_18.6.21-25.6.21.json","w", encoding="utf-8",newline="") as archivo:
    json.dump(rdo,archivo,indent=4)
