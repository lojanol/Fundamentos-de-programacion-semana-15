# crear el diccionario con informacion imaginaria ingresado por el usuario
informacion_personal={
    "nombre": input("ingrese el nombre del ususario:"),
    "edad":int (input("ingrese la edad del ususario:")),
    "ciudad":input("ingrese la ciudad del ususario:"),
    "profesion":input("ingrese la profesion del usuario")
}

# verificar si la clave "telefono" existe en el diccionario agregar si no existe
if"telefono" not in informacion_personal:
    telefono=informacion_personal["telefono"]=input("ingrese el numero de telefono:")

# eliminar la clave "edad" del diccionario
del informacion_personal["edad"]
# imprimir el diccionario
print("diccionario final:",informacion_personal)