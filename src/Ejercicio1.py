# Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':
# '$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje 
# de aviso si la divisa no está en el diccionario. Funcion que busca si dicha divisa 
# está o no en el diccionario.


def buscarDivisa(monedas:dict, divisa:str)-> bool:
    
    if divisa not in monedas:
        return False
    else:
        return True

if __name__ == "__main__":


    #ENTRADA
    divisa = input("Escribe una divisa: ")
    monedas = {"eruo": "€", "dolar": "$", "ye": "¥"}


    #PROCESO
    resultadoDivisa = buscarDivisa(monedas, divisa)

    #SALIDA
    print(resultadoDivisa)







