palabrasPositivas = ["ama", "gusta", "genial", "excelente", "bueno"]
palabrasNegativas = ["odia", "malo", "terrible", "decepcionante", "pésimo"]

coment = input("Ingrese el comentario: ").lower()
contadorpos = 0
contadorneg = 0
for corrido in palabrasPositivas:
    contadorpos += coment.count(corrido) 

for corrido in palabrasNegativas:
    contadorneg += coment.count(corrido)

if contadorpos > contadorneg:
    print("Sentimiento: Positivo")
elif contadorneg > contadorpos:
    print("Sentimiento: Negativo")
elif contadorpos == contadorneg:
    print("Sentimiento: Neutral")



