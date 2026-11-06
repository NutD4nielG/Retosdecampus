import random
numero = random.randint(1,100)
intentos = 1

print("="*60)
print("\tAdivia el número secreto entre 1 y 100")
print("="*60)

while True:
    n = int(input(f"Intento {intentos} - Ingresa tú número: ")) 
    intentos += +1
    if n > numero:
        print("Pista: Tu numero es demasiado alto")
    elif n < numero:
        print("Pista: Tu número es demasido bajo")
    else:
        print("-"*80)
        print(f"\t¡Felicidades! Adivinaste el número {numero} en {intentos -1} intentos.")
        print("-"*80)
        break