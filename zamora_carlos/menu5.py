# Ejercicio 5. Elementos del M.R.U.
def agregar_primer_elemento():
    input("ingrese primer elemento:")
    print("se agrego primer elemento:")

def agregar_segundo_elemento():
    input("ingrese segundo elemento:")
    print("se agrego segundo elemento:")

def agregar_tercer_elemento():
    input("ingrese tercer elemento:")
    print("ingrese tercer elemento:")

opc=0
max==4
while(opc!=max):
    print("##############Menu############")
    print("#1. Agregar primer elemento: #")
    print("#2. Agregar segundo elemento:#")
    print("#3. Agregar tercer elemento: #")
    print("#4. Salir:                   #")
    print("##############################")
#fin_menu

#Mapeo de funciones
if (opc==1):
    agregar_primer_elemento()
if (opc==2):
    agregar_segundo_elemento()
if (opc==3):
    agregar_tercer_elemento()

print("Finalizar programa")

#fin_def
