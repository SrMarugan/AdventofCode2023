from itertools import product

def generar_combinaciones(parte_resortes, lista_numerica):
    # Encontrar índices de resortes rotos desconocidos ('?')
    indices_desconocidos = [i for i, char in enumerate(parte_resortes) if char == '?']

    # Generar todas las posibles combinaciones de resortes operativos (.) y rotos (#) para los desconocidos
    combinaciones = product(['.', '#'], repeat=len(indices_desconocidos))

    # Contar el número de combinaciones válidas
    combinaciones_validas = 0

    for combinacion in combinaciones:
        nueva_fila = list(parte_resortes)
        
        # Reemplazar los resortes desconocidos con la combinación actual
        for indice, valor in zip(indices_desconocidos, combinacion):
            nueva_fila[indice] = valor
        
        # Verificar si la combinación cumple con la lista numérica
        grupos = ''.join(nueva_fila).split('.')
        grupos = [len(grupo) for grupo in grupos if grupo]

        if grupos == lista_numerica:
            combinaciones_validas += 1

    return combinaciones_validas


with open(file="input12.txt") as file:
    resultado = 0
    lines = file.readlines()
    for line in lines:
        # Separar en código del puzzle y codigo de numero
        line = line.strip().split(" ")
        input_codigo = line[0]
        input_numerica = line[1]

        # Comprobar que cumplen con el input del número e ir sumando si es acierto
        resultado += generar_combinaciones(input_codigo, [int(num) for num in input_numerica.split(',')])

    print(resultado)
