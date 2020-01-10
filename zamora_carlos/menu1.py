import libreria
#Ejercicio N°1:Menu.
def agregar_nombre():
    input("ingrese nombre:")
    print("se agrego nombre")
def agregar_direccion():
    input("ingrese direccion:")
    print("se agrego direccion")

opc=0
max=3
while (opc!=max):
    print("######### MENU #########")
    print("#1. Agregar nombre:    #")
    print("#2. Agregar direccion: #")
    print("#3. Salir.             #")
    print("########################")
    opc=libreria.pedir_numero("Ingrese Opcion:", 1, 3)
#fin_menu

# Mapeo de funciones
    if(opc==1):
        agregar_nombre()
    if(opc==2):
        agregar_direccion()
print("Programa Finalizado")

#fin_def
