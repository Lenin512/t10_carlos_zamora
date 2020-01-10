import libreria
#Ejercicio N°6: Menu... Elementos de la Dinamica
def agregar_primera_variable():
    input("ingrese primer elemento:")
    print("se agrego el prmer elemento:")

def agregar_segunda_variable():
    input("ingrese el segundo elemento:")
    print("se agrego segundo elemento:")

def agregar_tercera_variable():
    input("ingrese la segunda etapa:")
    print("se agrego la segunda etapa:")

opc=0
max=4
while( opc != max ):
    #1. Impresion del menu
    print("############Menu##############")
    print("#1. Agregar primera varible: #")
    print("#2. Agregar segunda variable:#")
    print("#3. Agregar tercera variable:#")
    print("#4. Salir:                   #")
    print("##############################")


    #2. Eleccion de la opcion del menu
    opc= libreria.pedir_numero("Ingrese la opcion",1,4)


    #3. Mapeo de las opciones
    if ( opc ==1 ):
          agregar_primera_variable()
    if (opc==2):
         agregar_segunda_variable()
    if (opc==3):
         agregar_tercera_variable()

#fin_menu
print("fin del programa")

#fin_def
