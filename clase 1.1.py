#tuplas
#listas/arrays/arreglos
#diccionarios

#una tupla es una variable que permite almacenar varios datos inmutables(no pueden modificarse una ves creados)

mi_tupla= (1,"jesus",99.6)
# print(mi_tupla[1])


print(mi_tupla[1:2])
#una lista es similar a un atupla con la diferencia fundamental de qe permite modificar los datos una ves creados:
mi_lista=["cadena de texto", 15,2.8,"jesus",30]
# print(mi_lista[0])
mi_lista[0]="hola"
# print(mi_lista[0])

mi_lista.append(999)
mi_lista.remove(15)
mi_lista.pop(0)
# print(mi_lista)


#los diccionarios permiten utilizar una clave para declarar y acceder a un valor
mi_diccionario={"x":"123"}
print(mi_diccionario["x"])
persona_0= {"nombre":"juan", "nacionalidad":"aleman","peso":"74"}
persona_1= {"nombre":"oscar", "nacionalidad":"mexicana","peso":"69"}

print(persona_1)

