import libreria
#Ejercicio4:Menu . Clasificacion de algunas Matrices
def agregar_primera_matriz():
    input("ingerse primera matriz:")
    print("se agrego nombre de a primera matrz:")
def agregar_segunda_matriz():
    input("ingrese segunda matriz:")
    print("se agrego nombre de la segunda matriz:")
def agregar_tercera_matriz():
    input("ingrese nombre de la tercera matriz:")
    print("se agrego nombre de la tercera matriz:")

opc=0
max==4

while (opc!=max):
    print("###############Menu############")
    print("#1. Agregar la primera matriz:#")
    print("#2. Agregar la segunda matriz:#")
    print("#3. Agregar la tercera matriz:#")
    print("#4. Salir:                    #")
    print("###############################")

# Eleccion de la opcion del menu
opc=libreria.perdir_numero("Ingrese Opcion:",1,4)

# Mapeo de las funciones
if (opc==1):
        agregar_primera_matriz()
if (opc==2):
        agregar_segunda_matriz()
if (opc==3):
        agregar_tercera_matriz()

print("Programa finalizado")

#fin_def
