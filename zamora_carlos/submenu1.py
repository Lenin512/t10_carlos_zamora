import libreria
#Ejercicio N°1:Menu.

def primer_nombre():
    x=libreria.pedir_nombre("ingrese el primer nombre:")
    print("x")
    contenido= x + "-"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("se guardo los datos")

def segundo_nombre():
    y=libreria.pedir_nombre("ingrese el segndo nombre:")
    print("y")
    contenido= y + "-"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("se guardo los datos")

def agregar_nombres():
    print("######### MENU #########")
    print("#1. Primer nombre:    #")
    print("#2. Segundo nombre: #")
    print("#3. Salir.             #")
    print("########################")
    opc=libreria.pedir_numero("Ingrese Opcion:", 1, 3)
    if (opc==1):
        primer_nombre()
    if(opc==2):
        segundo_nombre()


def agregar_direccion():
    input("ingrese direccion:")
    print("se agrego direccion")

opc=0
max=3
while (opc!=max):
    print("######### MENU #########")
    print("#1. Agregar nombres:    #")
    print("#2. Agregar direccion: #")
    print("#3. Salir.             #")
    print("########################")
    opc=libreria.pedir_numero("Ingrese Opcion:", 1, 3)
#fin_menu

# Mapeo de funciones
    if(opc==1):
        agregar_nombres()
    if(opc==2):
        agregar_direccion()
print("Programa Finalizado")

#fin_def
