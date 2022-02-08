import math
usuario=float(input("Escriba el numero:"))
def even_or_odd(residuo):
    cociente=usuario/2
    residuo=usuario-2*math.floor(cociente)
    if residuo==0:
        return "Par"
    else:
        return "Impar"
print(even_or_odd(usuario))