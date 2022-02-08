lista=[]
texto=str(input("Escriba su mensaje: "))
def creador_de_oracion(texto):
        if      "what" in texto or "who" in texto or "why" in texto or "how" in texto:
                texto_2=f"{texto.capitalize()}?"
                return texto_2
        else:  
                texto_1=f"{texto.capitalize()}."
                return texto_1
while True:
        if texto !="termina":
                lista.append(creador_de_oracion(texto))
                texto=str(input("Escriba su mensaje: "))
                continue
        else: texto=="termina"
        break
mensaje_completo=" ".join(lista)
print(mensaje_completo)
