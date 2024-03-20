# Esto es un comentario de una línea 
# Todo lo que va después es ignorado
# por el interprete de python 

# Variables: Espacio de memoria, con nmbre, donde guardo valores
# Los nombres de variables deben se cortos, descriptivos, NO TENER ESPACIOS
# EN BLANCO ni caracteres especiales, no deben empezar por número

# Descriptivo significa que representa la categoría del dato que quiero guardar
# números (enteros, reales), cadenas de carácteres (string), booleanos (True, False)
# caracteres.

variable = 1

variable = 'Hola'

variable = True

variable = 'a'

variable = 3.14159265365

# Para asignar un valor a la variable se una el operador =



# Operadores: Mecanismo para obtener un dato a partir de otros datos.
# Los datos que intervienen se llaman operadores 

# Aritmeticos: + - / %
# De comparación: Retornan True or False. < > >= <= == !=
# Los de lógica boolana: AND OR. Retornan True o False de a cuerdo a una 
# tabla de verdad. Los operadores siempre son booleanos (True or False)

a = True
b = False 

print (a and b)

# Los operadores booleanos y de comparación son muy utilizados al
# definir condiciones 


# Estructura de contro del código: En general un programa se ejecuta
# línea por línea de forma secuencial. Se puede romper esa secuencialidad
#empleando un conjunto de sentencias que permite:
# 1 seleccionar la ejecucion de un bloque de código
# 2 repetir la ejecución de un bloque de codigo
# 3 seleccionar entre ejecutar un bloque de codigo u otro bloque de codigo
# de esa manera podemos romper la secuencialidad

# sentencia if. si se cumpla una condición (se evlua como true)
#se ejecuta un bloque de codigo

print("Linea 1")
print("Linea 2")
#2
if 5>3:
    print("se muestra si la condición es verdadera")
    
if True: #se ejecuta
    print ("HOLA")

if 5>8 or 3<7:
    print("jiji")
    
#3
if 5>8 or 3>7:
    print("chao")
else:
    print("no chao")
    
    
entrada = int(input("Cuantos años tiene?"))

if entrada<18:
    print("Es menor de edad")
else:
    print("Mayor de edad")
    
#Taller 2 cree un programa en phyton que genere un numero aleatorio
#entre 1 y 6. Si el numero es 7, imprima ganó, si no imprimir deje el juego.