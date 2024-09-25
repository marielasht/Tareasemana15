
nombre = input('¿Cómo te llamas? ')
edad = input('¿Cuántos años tienes? ')
ciudad = input('¿Cuál es tu Ciudad? ')
profesion = input('¿Cuál es su profesion? ')
persona = {'nombre': nombre, 'edad': edad, 'ciudad': ciudad, 'profesion': profesion}
print(persona['nombre'], 'tiene', persona['edad'], 'años, vive en', persona['ciudad'], 'y su profesion es', persona['profesion'])
# 1. Crear diccionario utilizando llaves {} y especificando pares clave-valor
#separados por dos puntos:
mi_diccionario={"nombre":"Juan","edad":30,"ciudad":"Tena","profesion":"Sistemas","telefono":"0980525431"}

#Puedes acceder a los valores de un diccionario utilizando su clave. Por ejemplo:
nombre = mi_diccionario["nombre"]
edad = mi_diccionario["edad"]
ciudad = mi_diccionario["ciudad"]
profesion = mi_diccionario["profesion"]
telefono = mi_diccionario["telefono"]
# 2.Accede al valor asociado con la clave "ciudad" y modifícalo con una ciudad diferente.
mi_diccionario["ciudad"] = "Tena"
if ciudad in mi_diccionario:
    print(f'La clave {ciudad} está y el valor asociado es: {mi_diccionario[ciudad]}')
print("¿la clave 'ciudad'?")
print(mi_diccionario["ciudad"])
ciudad = input('¿Modifique el nombre de la ciudad? ')
mi_diccionario = {
    "ciudad": ' ' + ciudad, }
clave = 'ciudad'
try:
    print(f'El valor modificado de {clave} es: {mi_diccionario[clave]}')  # se ejecutará correctamente
except:
    print(f'La clave {clave} no se encuentra en el diccionario')
# 2.1 Puedes cambiar el valor asociado a una clave en un diccionario de la siguiente manera:
mi_diccionario["ciudad"] = "Pastaza"

# 2.2Agrega una nueva clave-valor al diccionario que represente la "profesion" de la persona.
mi_diccionario["profesion"] = "Sistemas"

if profesion in mi_diccionario:
    print(f'La clave {profesion} está y el valor asociado es: {mi_diccionario[profesion]}')
print("¿la nueva clave 'profesion'?")
print(mi_diccionario["profesion"])
profesion = input('¿Aguegue el nombre de la profesion? ')
mi_diccionario = {
    "profesion": ' ' + profesion, }
clave = 'profesion'
try:
    print(f'El valor ingresado de {clave} es: {mi_diccionario[clave]}')  # se ejecutará correctamente
except:
    print(f'La clave {clave} no se encuentra en el diccionario')
print("¿Representa la profesion de la persona?")
print(mi_diccionario["profesion"])

# 3. Verifica si la clave "telefono" existe en el diccionario. Si no existe,
# agrégala con un número de teléfono ficticio.

mi_diccionario["telefono"] = " 0 "
if telefono in mi_diccionario:
    print(f'La clave {telefono} está y el valor asociado es: {mi_diccionario[telefono]}')
print("¿la clave 'telefono'existe en el diccionario?")
clave = 'telefono'
try:
    print(f'La clave {telefono} está y el valor asociado es: {mi_diccionario[telefono]}')
except:
    print(f'La clave {clave} no se encuentra en el diccionario')
print("¿Agregue un numero de 'telefono' ficticio?")
telefono = input('¿Ingrese el numero del telefono? ')
mi_diccionario = {
    "telefono": ' ' + telefono, }
clave = 'telefono'
try:
    print(f'El valor ingresado para {clave} es: {mi_diccionario[clave]}')  # se ejecutará correctamente
except:
    print(f'La clave {clave} no se encuentra en el diccionario')

# 4. Elimina la clave "edad" del diccionario, ya que esa información no es necesaria.
#Puedes eliminar un par clave-valor de un diccionario utilizando la palabra clave del
#seguido de la clave que deseas eliminar. Por ejemplo:
# Creamos un dicionario con los elementos
mi_diccionario = {
        "nombre": "Juan",
        "edad": 30,
        "ciudad": "Tena",
        "profesion": "Sistemas",}
edad = mi_diccionario["edad"]
# Eliminamos el segundo elemento
del mi_diccionario["edad"]
print("Eliminamos el segundo elemento, e imprime:")
print(mi_diccionario) # Imprime

#Imprime el diccionario resultante después de realizar todas las operaciones.
for clave, valor in mi_diccionario.items():
    print(f"Clave:{clave},Valor: {valor}")

