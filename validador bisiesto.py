ano = int(input("Ingrese un año: "))

if ano % 400 == 0:
    print(f"El año {ano} es Bisiesto")
elif ano % 100 == 0:
    print(f"El año {ano} no es Bisiesto")
elif ano % 4 != 0:
        print(f"El año {ano} no es Bisiesto")
else:
    ano % 4 == 0
    print(f"El año {ano} es Bisiesto")
