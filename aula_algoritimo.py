# Implementação do algoritmo de ordenação por seleção
lista = [14975,64, 34, 25, 12, 22, 11, 90, -102, -1034, 12895]

def ordenar_lista_numeros(numeros: list) -> list:
    nova_lista_numeros = numeros.copy()
    
    for i in range(len(nova_lista_numeros)):
        for j in range(i+1, len(nova_lista_numeros)):
            if nova_lista_numeros[i] > nova_lista_numeros[j]:
                nova_lista_numeros[i], nova_lista_numeros[j] = nova_lista_numeros[j], nova_lista_numeros[i]


    return nova_lista_numeros

# Ordenando a lista
nova_lista = ordenar_lista_numeros(lista)
print("Lista ordenada com função personalizada:", nova_lista)