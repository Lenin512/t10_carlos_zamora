import libreria
#Ejercicio N°2: Clasificacion de las etapas de la Historia

def agregar_primera_etapa():
    input("ingrese la primera etapa:")
    print("se agrego primera etapa:")

def agregar_segunda_etapa():
    input("ingrese la segunda etapa:")
    print("se agrego la segunda etapa:")

def agregar_tercera_etapa():
    input("ingrese la tercera etapa:")
    print("se agrego la tercera etapa:")


opc=0
max=4
while( opc != max ):
    #1. Impresion del menu
    print("###########Menu############")
    print("#1. Agregar primera etapa:#")
    print("#2. Agregar segunda etapa:#")
    print("#3. Agregar tercera etapa:#")
    print("#4. Salir:                #")
    print("###########################")


    #2. Eleccion de la opcion del menu
    opc= libreria.pedir_numero("Ingrese la opcion",1,6)


    #3. Mapeo de las opciones
    if ( opc ==1 ):
         agregar_primera_etapa()
    if (opc==2):
         agregar_segunda_etapa()
    if (opc==3):
         agregar_tercera_etapa()

#fin_menu
print("fin del programa")

#fin_def
