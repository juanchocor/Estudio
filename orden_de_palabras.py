'''te dan n palabras. Algunas palabras pueden repetirse. 
Para cada palabra, genere su número de apariciones. 
El orden de salida debe corresponder con el orden de entrada de aparición de la palabra. 
Consulte el ejemplo de entrada/salida para obtener más aclaraciones.

Nota: Cada línea de entrada termina con un carácter "\n" .

Restricciones:

La suma de las longitudes de todas las palabras no excede
Todas las palabras están compuestas únicamente de letras minúsculas en inglés.

Formato de entrada

La primera línea contiene el número entero,.
El siguienteCada línea contiene una palabra.

Formato de salida

Producciónlíneas.
En la primera línea, genere el número de palabras distintas de la entrada.
En la segunda línea, genere el número de apariciones de cada palabra distinta según su aparición en la entrada.'''


from collections import OrderedDict

N = int(input())

appearances = OrderedDict()

for _ in range(N):
    word = input().strip()
    appearances[word] = appearances.get(word, 0) + 1
    
print(len(appearances))

print(*appearances.values())

'''Este código utiliza un diccionario (apariciones) para contar las apariciones de cada palabra.
Luego, imprime el número de palabras distintas y el número de 
apariciones de cada palabra en el orden en que aparecieron en la entrada.
La función strip() se utiliza para eliminar cualquier espacio en blanco alrededor de las palabras.'''