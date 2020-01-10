
import libreria
#Ejercicio N°8:Menu.
def agregar_primer_tipo_de_funciones_trigonometricas():
    input("ingrese nombre:")
    print("se agrego nombre")
def agregar_segundo_tipo_de_funciones_trigonometricas():
    input("ingrese direccion:")
    print("se agrego direccion")

opc=0
max=3
while (opc!=max):
    print("######################## MENU ##########################")
    print("#1. Agregar primer tipo de funciones trigonometricas:  #")
    print("#2. Agregar segundo tipo de funciones trigonometricas: #")
    print("#3. Salir.                                             #")
    print("########################################################")
    opc=libreria.pedir_numero("Ingrese Opcion:", 1, 3)
#fin_menu

# Mapeo de funciones
    if(opc==1):
        agregar_primer_tipo_de_funciones_trigonometricas()
    if(opc==2):
        agregar_segundo_tipo_de_funciones_trigonometricas()
print("Programa Finalizado")

#fin_def
