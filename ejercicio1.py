import os
import msvcrt
import csv
sala_de_cine = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
while True:
    
    print(f"""\t>>>Pantalla<<<
        ================""")

    for x in range(len(sala_de_cine)):
        
        print(x+1,f"\t{sala_de_cine[x]}")
    print("\t================")

    print(">>>Menu<<<")
    print("1) Mostrar asientos")
    print("2) comprar entrada")
    print("3) mostrar ventas realizadas")
    print("4) Generar archivo CSV")
    print("5) salir.")
    opc = int(input("seleccione opcion en pantalla: "))
    os.system('cls')
    if opc == 1:
        pass
    elif opc == 2:
        pass
    elif opc == 3:
        pass
    elif opc == 4:
        pass
    else:
        break
